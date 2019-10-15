import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Open("C:\\Users\\JST-0602\\Desktop\\test.xlsx")
ws = wb.ActiveSheet

print(ws.Cells(1,1).Value)
ws.Cells(1,2).Value = "is"
ws.Range('C1').Value = "good"

ws.Range('C1').Interior.ColorIndex = 10
ws.Range('A2:C2').Interior.ColorIndex = 27

for i in range(0, 11):
    ws.Cells(i + 3, 1).Value = i
    ws.Cells(i + 3, 2).Value = i * i
    ws.Cells(i + 3, 3).Value = "="
    ws.Cells(i + 3, 4).Value = ws.Cells(i + 3, 1).Value + ws.Cells(i + 3, 2).Value


# excel.Quit()