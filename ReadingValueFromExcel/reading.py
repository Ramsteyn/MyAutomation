import xlrd

# creating object of the Work_book class
wk = xlrd.open_workbook("C:/Users/ramadhma/Selenium/Book1.xls")

ws = wk.sheet_by_name("Sheet1")

r=ws.nrows
c=ws.ncols

# Reading Values in File using loop
for i in range(0,r):
    for j in range(0,c):
       wc=ws.cell(i,j)
       print(wc.value)