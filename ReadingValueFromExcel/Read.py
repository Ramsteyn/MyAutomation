import xlrd

# creating object of the Work_book class
wk = xlrd.open_workbook("C:/Users/ramadhma/Selenium/Book1.xls")

# Finding number of sheets in a Excel
print(wk.nsheets)

# Finding Number of  rows and columns in Excel by Index
print("Output using sheetIndex")
ws = wk.sheet_by_index(0)
print(ws.nrows)
print(ws.ncols)

#FindingNumber of  rows and columns in Excel by SheetName
print("Out using sheetName")
ws1 = wk.sheet_by_name("Sheet1")
print(ws.nrows)
print(ws.ncols)

# Finding values in cell of sheet
print("Value in a Cell")
wc = ws.cell(0,0)
print(wc.value)
