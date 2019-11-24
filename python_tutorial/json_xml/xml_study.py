xml_data = """<?xml version="1.0" encoding="UTF-8" ?>
<사용자정보>
    <이름>홍길동</이름>
    <나이>25</나이>
    <거주지>서울</거주지>
    <신체정보>
        <키 unit="cm">175.4</키>
        <몸무게 unit="kg">71.2</몸무게>
    </신체정보>
    <취미>등산</취미>
    <취미>자전거타기</취미>
    <취미>독서</취미>
</사용자정보> 
"""
print(xml_data)

import xmltodict

dict_data = xmltodict.parse(xml_data, xml_attribs=True)
print(dict_data['사용자정보']['이름'],  dict_data['사용자정보']['신체정보'])
print(dict_data['사용자정보']['신체정보']['키']['@unit'])
print(dict_data['사용자정보']['신체정보']['키']['#text'])

dict_data = xmltodict.parse(xml_data)

user_name = dict_data['사용자정보']['이름']
body_data = dict_data['사용자정보']['신체정보']

height = body_data['키']['#text']
height_unit = body_data['키']['@unit']

weight = body_data['몸무게']['#text']
weight_unit = body_data['몸무게']['@unit']

print("[사용자 {0}의 신체정보]".format(user_name))
print("*키: {0}{1}".format(height, height_unit))
print("*몸무게: {0}{1}".format(weight, weight_unit))


dict_data2 = xmltodict.parse(xml_data, xml_attribs=False)
print(dict_data2)