from school_schedule.student import Student
import pytest 

#nominal case
def test_check_attributes_of_instance_created():
    #arrange
    name = "Bob"
    grade_level = "junior"
    class_list = ["math", "science", "biology"]

    #act
    bob = Student(name, grade_level, class_list)

    #assert
    assert bob.name == name
    assert bob.grade_level == grade_level
    assert bob.class_list == class_list
    assert len(bob.class_list) == 3

#edge case
def test_raise_error_if_parameter_type_invalid():
    #act, alternate set-up with keyword args
    bob = Student(name = "bob", grade_level = "junior", class_list = 0)

    #assert
    with pytest.raises(AttributeError): bob.class_list.append("social studies")

#nominal case
def test_add_class_modifies_attribute():
    #arrange
    bob = Student(name = "Bob", grade_level = "junior", class_list = ["math", "science", "biology"])

    #act
    bob.add_class("gym")
    #assert
    assert len(bob.class_list) == 4

#nominal case
def test_get_num_classes_returns_classes_if_not_empty():
    #arrange
    bob = Student(name = "Bob", grade_level = "junior", class_list = ["math", "science", "biology"])
    #act
    result = bob.get_num_classes()
    #assert
    result == 3
 


