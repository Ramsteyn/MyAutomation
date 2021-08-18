import xlwt
# Object of workbook
wk = xlwt.Workbook()
ws = wk.add_sheet("testing")
ws.write(0,0,"What is it")
ws.write(0,1,"What fuck")

#Saving workBook
wk.save("C:/Users/ramadhma/Selenium/PythonWrite.xlsx")