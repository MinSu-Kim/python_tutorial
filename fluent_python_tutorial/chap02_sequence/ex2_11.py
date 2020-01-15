invoice = """
0           12              27  
2020-02-08  PyCascades      2020
2020-02-18  PyCon Namibia   2020
2020-03-27  PyCon SK        2020
2020-04-02  PyCon Italia    2020
2020-04-17  Django Day      1990
"""

DATE = slice(0, 12)
TITLE = slice(12, 27)
YEAR = slice(27, None)

line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[DATE], item[TITLE], item[YEAR])