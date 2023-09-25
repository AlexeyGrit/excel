import pandas as pd

# Создаем JSON
data = {'имя': ['Кирилл', 'Леша'], 'возраст': [25, 24]}
df = pd.DataFrame(data)

# Сохранил
df.to_excel('output.xlsx')