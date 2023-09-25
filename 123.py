from pathlib import Path
import pandas as pd
file_path = Path(‘C:\Users\User\Desktop\test\test_1’).resolve()
data = pd.read_excel(file_path)
data.to_json(‘result.json’)