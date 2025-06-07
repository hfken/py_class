import openpyxl
from openpyxl.styles import Font,Side,Border
excel=openpyxl.load_workbook(r'./file/excel/data.xlsx')
sheet=excel['Sheet1']
sheet['D1']='nihao'
excel.save(r'./file/excel/out.xlsx')