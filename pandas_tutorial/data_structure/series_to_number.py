import pandas as pd

student1 = pd.Series({'국어':100, '영어':80, '수학':90})
print(student1)
print()

print("# 학생의 과목별 점수를 200으로 나누기")
percentage = student1 / 200

print(percentage)
print(type(percentage))