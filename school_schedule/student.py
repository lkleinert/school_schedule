class Student:
    def __init__(self, name, grade_level, class_list):
        self.name = name
        self.grade_level = grade_level
        self.class_list = class_list

    def add_class(self, class_name):
        self.class_list.append(class_name)
        #optional return

    def get_num_classes(self):
        return len(self.class_list)
        #need to return value here--> not changing an attribute

    def summary(self):
        print(f'{self.name} is a {self.grade_level}\n Classlist: {self.get_num_classes()}')


