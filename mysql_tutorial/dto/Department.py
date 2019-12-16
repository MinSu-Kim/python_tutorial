class Department():
    def __init__(self):
        self.__deptno = None
        self.__deptname = None
        self.__floor = None

    @property
    def deptno(self):  # getter
        return self.__deptno

    @deptno.setter
    def deptno(self, deptno):  # setter  getter먼저 선언 후 선언해야 됨.
        self.__deptno = deptno

    @property
    def deptname(self):
        return self.__deptname

    @deptname.setter
    def deptname(self, deptname):
        self.__deptname = deptname

    @property
    def floor(self):
        return self.floor

    @floor.setter
    def floor(self, floor):
        self.__floor = floor

    def __str__(self):
        return '[{} {} {}]'.format(self.__deptno, self.__deptname, self.__floor)


class Department2:
    def __init__(self, deptno=None, deptname=None, floor=None):
        self.__deptno = deptno
        self.__deptname = deptname
        self.__floor = floor

    def __repr__(self):
        return '[{} {} {}]'.format(self.__deptno, self.__deptname, self.__floor)


if __name__ == "__main__":
    dept = Department()
    dept.deptno = 2
    dept.deptname = '개발'
    dept.floor = 20
    print(dept)

    deptList2 = [Department2(),
                 Department2(deptno=1),
                 Department2(deptno=1, deptname='영업'),
                 Department2(deptno=1, deptname='영업', floor=8)]
    for obj in deptList2:
        print(obj)
