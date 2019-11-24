import xmltodict

from python_tutorial.json_xml.xml_study01 import xml_data

if __name__ == "__main__":
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

    # xml_attribs=False 속성을 이용하여 XML형식의 데이터를 딕셔너리로 변환
    dict_data2 = xmltodict.parse(xml_data, xml_attribs=False)
    print(type(dict_data2))
    print(dict_data2)