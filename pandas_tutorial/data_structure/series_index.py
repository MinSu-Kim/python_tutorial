import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print("리스트를 시리즈로 변환하여 변수 sr에 저장", sr, sep='\n', end='\n\n')

print("인덱스를 별도로 정의하지 않으면, 디폴트로 정수형 위치 인덱스(0, 1, 2, ∙∙∙)가 자동 지정")
print(type(sr.index), sr.index, sep='\n')
print(type(sr.values), sr.values, sep='\n')
print()
print("인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장")
[print(idx, val) for idx, val in sr.items()]