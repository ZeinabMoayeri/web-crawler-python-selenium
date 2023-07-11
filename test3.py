import pandas as pd
df = pd.read_csv('files_diza - Copy of all_together.csv')

for item in df['sizedetail']:
    if item == 'nan':
        continue
    else:
        print(item)