import openpyxl
from openpyxl.styles import Font,Side,Border
excel=openpyxl.load_workbook(r'./file/excel/data.xlsx')
sheet=excel['Sheet1']
side=Side(border_style='thin',color='00FF9900')
sheet['D1']='nihao'
sheet['D1'].border=Border(top=side,bottom=side)
sheet['D1'].font=Font(bold=True,italic=True)
excel.save(r'./file/excel/out.xlsx')