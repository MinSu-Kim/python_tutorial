import pandas as pd

# HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url ='./sample.html'

# HTML 웹페이지의 표(table)를 가져와서 데이터프레임으로 변환 
tables = pd.read_html(url)

print("# 표(table)의 개수 확인")
print(len(tables))
print()

print("# tables 리스트의 원소를 iteration하면서 각각 화면 출력")
for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print()

print("# 파이썬 패키지 정보가 들어 있는 두 번째 데이터프레임을 선택하여 df 변수에 저장")
df = tables[1] 

print("# 'name' 열을 인덱스로 지정")
df.set_index(['name'], inplace=True)
print(df)