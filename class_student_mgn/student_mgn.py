import json
import os

from class_student_mgn.student import Student


class StudentManagement():
    def __init__(self):
        self.file_name = "stdlist.txt"
        self.std_list = self.std_list_read_file()

    def std_list_read_file(self):
        list_std = []
        if os.path.isfile(self.file_name):
            with open(self.file_name, 'r', encoding='utf-8') as f:  # json_xml 형태의 파일 load
                x = json.load(f)
                # return json.loads(x)
            [list_std.append(Student(std)) for std in json.loads(x)]
            return list_std
        else:
            return list_std

    def std_list_write_file(self):
        json_student = json.dumps(self.std_list, ensure_ascii=False, default=json_default)
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(json_student, f, ensure_ascii=False)

    def add_std_info(self, student): # std = Student(no=1, name='김승영', score=[90, 90, 90])
        self.std_list.append(student)

    def update_std_info(self, student):
        self.std_list[self.std_list.index(student)] = student

    def delete_std(self, student):
        del self.std_list[self.std_list.index(student)]

    def show_std_list(self):
        [print(std) for std in self.std_list]

    def find_student(self, std):
        print(self.std_list.index(std))
        return self.std_list[int(self.std_list.index(std))]

    def get_std_list(self):
        return self.std_list


def json_default(obj):
    try:
        return obj.__json__()
    except AttributeError:
        raise TypeError("{} can not be JSON encoded".format(type(obj)))