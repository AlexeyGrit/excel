import pandas as pd

# Создаем JSON
data = {'имя': ['Иван', 'Мария', 'Сергей'], 'возраст': [24, 25, 26]}
df = pd.DataFrame(data)

# Сохранил
df.to_excel('output.xlsx', index=False, header=True)