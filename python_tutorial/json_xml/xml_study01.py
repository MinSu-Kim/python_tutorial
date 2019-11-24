import xmltodict

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

if __name__ == "__main__":
    print(xml_data)

    dict_data = xmltodict.parse(xml_data, xml_attribs=True) # xml_attribs=True 기본값
    print(type(dict_data))# ㅐ OrderedDict 입력한 순서대로 순서를 갖는 딕셔너리 데이터
    print(dict_data)

    print("dict_data['사용자정보']['이름'] = {}".format(dict_data['사용자정보']['이름']))
    print("dict_data['사용자정보']['신체정보'] = {}".format(dict_data['사용자정보']['신체정보']))
    print("dict_data['사용자정보']['신체정보']['키']['@unit'] = {}".format(dict_data['사용자정보']['신체정보']['키']['@unit']))
    print("dict_data['사용자정보']['신체정보']['키']['#text'] = {}".format(dict_data['사용자정보']['신체정보']['키']['#text']))