import pandas as pd
import openpyxl

book=openpyxl.Workbook()

heet = book.active

sheet['A1'] = 'a'
sheet['A2'] = '10'

book.save("test.xlsx")
book.close()

data = pd.read_excel('test.xlsx')
data.to_json('output.json')

