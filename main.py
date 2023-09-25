import pandas as pd
data = pd.read_excel('tetes.xlsx')
data.to_json('tetes_result.json')