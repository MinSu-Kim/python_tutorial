import matplotlib
from pprint import pprint as pp

# 컬러 이름과 헥사코드 확인하여 Dictionary Comprehesions(Dictionary 표현식)을 이용하여 출력
{print(name,':',hex) for name, hex in matplotlib.colors.cnames.items()}
print()

file_info = {name:hex for name, hex in matplotlib.colors.cnames.items()}
#pprint는 Dictionary 타입을 예쁘게(?) 정렬해서 표시
pp(file_info)