from class_student_mgn.student import Student
from class_student_mgn.student_mgn import StudentManagement


def show_menu():
    try:
        return int(input("1. 학생목록, 2. 학생 추가, 3. 학생 수정, 4. 학생 삭제, 5. 종료 [1-5] 번호를 입력하세요."))
    except ValueError as e:
        print("숫자 [1-5]값만 가능")
        exit(0)


def add_std_info():
    std_info = get_std_info("번호 성명 국어 영어 수학을 입력하세요. ex)최영민 90 90 90 >> ")
    userdict = {}
    userdict['no'] = int(std_info[0])
    userdict['name'] = std_info[1]
    userdict['score'] = {'국어': int(std_info[2]), '영어': int(std_info[3]), '수학': int(std_info[4])}
    return Student(userdict)


def update_std_info(students):
    res = input("수정할 학생번호를 입력하세요. >>")
    find_std = students.find_student(Student(no=int(res)))
    std_info = get_std_info("수정할 국어 영어 수학을 입력하세요. ex)90 90 90 >> ")
    userdict = {}
    userdict['no'] = find_std.no
    userdict['name'] = find_std.name
    userdict['score'] = {'국어': int(std_info[0]), '영어': int(std_info[1]), '수학': int(std_info[2])}
    return Student(userdict)


def get_std_info(msg):
    res = input(msg)
    std_info = res.split()
    return std_info


if __name__ == "__main__":
    students = StudentManagement()

    while True:
        res = show_menu()
        if res == 1:
            students.show_std_list()
        elif res == 2:
            students.add_std_info(add_std_info())
        elif res == 3:
            students.show_std_list()
            upstd = update_std_info(students)
            students.update_std_info(upstd)
        elif res == 4:
            students.show_std_list()
            res = input("삭제할 학생번호를 입력하세요. >>>>")
            del_std = Student(no=int(res))
            find_std = students.find_student(del_std)
            print(find_std)
            students.delete_std(find_std)
        else:
            students.std_list_write_file()
            break;
    print("프로그램 종료")
