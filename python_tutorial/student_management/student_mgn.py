"""
list, tuple, dictionary, set에서 하나를 선택하여 아래 프로그램을 작성하시오.
--> dictionary, 하나
student_management 패키지를 추가
학생 정보는 : 학생번호, 학생명, 국어, 영어, 수학
출력 결과 : 1, 김승영, 90, 90, 90, 270, 90.0
1. 학생목록, 2. 학생 추가, 3. 학생 수정, 4. 학생 삭제, 5. 종료 메뉴 추가
2. 프로그램 수행 시 먼저 student_list.txt 파일을 읽어와 수행
3. 각각 메뉴별 수행되도록 작성
4. 종료 시 학생목록이 student_list.txt에 저장
5. 프린트하여 제출하세요.
"""


def showMenu():
    try:
        res = int(input("1. 학생목록, 2. 학생 추가, 3. 학생 수정, 4. 학생 삭제, 5. 종료 [1-5] 번호를 입력하세요."))
        return res
    except ValueError as e:
        print("숫자 [1-5]값만 가능")
        exit(0)


# std_list = [[1, '김승영', 90, 90, 90],[2, '지재삼', 80, 90, 80]]
std_list = []
file_name = "std_list.txt"


def std_list_read_file():
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            std = line.strip().split(',')
            std_list.append(std)


def std_list_write_file(std_list):
    global file_name
    with open(file_name, 'w', encoding='utf-8') as f:
        for std in std_list:
            format_string = "{},{},{},{},{}\n".format(std[0], std[1], std[2], std[3], std[4])
            f.write(format_string)


def show_std_list():
    print("{:3} {:4} {:3} {:3} {:3} {:4} {:>4}".format('번호', '성명', '국어', '영어', '수학', '총점', '평균'))
    for std in std_list:
        total = int(std[2]) + int(std[3]) + int(std[4])
        avg = total/float(3)
        std_info = "{:3d} {:5} {:3d}  {:3d}   {:3d}   {:3d} {:7.2f}".format(int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4]), total, avg)
        print(std_info)


def add_std_info():
    std_info = get_std_info("성명 국어 영어 수학을 입력하세요. ex)최영민 90 90 90 >> ")
    std_info.insert(0, len(std_list) + 1)
    std_list.append(std_info)


def get_std_info(msg):
    res = input(msg)
    std_info = res.split()
    # std_info.insert(0, len(std_list) + 1)
    return std_info


def update_std_info():
    show_std_list()
    res = input("수정할 학생번호를 입력하세요. >>")
    for std in std_list:
        if res == std[0]:
            std_info = get_std_info("수정할 국어 영어 수학을 입력하세요. ex)90 90 90 >> ")
            std_info.insert(0, std[0])
            std_info.insert(1, std[1])
            std_list.remove(std)
            std_list.insert(int(std[0])-1, std_info)
            break


def delete_std_info():
    show_std_list()
    res = input("삭제할 학생번호를 입력하세요. >>")
    for std in std_list:
        if res == std[0]:
            std_list.remove(std)
            break


if __name__ == "__main__":
    std_list_read_file()
    while True:
        res = showMenu()
        if res == 1:
            show_std_list()
        elif res == 2:
            add_std_info()
        elif res == 3:
            update_std_info()
        elif res == 4:
            print("학생 삭제")
            delete_std_info()
        else:
            std_list_write_file(std_list)
            break;
    print("프로그램 종료")