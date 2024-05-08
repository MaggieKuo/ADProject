import pandas as pd
df = pd.read_excel('ta_feng_pchome_sample.xlsx', engine='openpyxl')
df.to_parquet('ta_feng_pchome_sample.parquet', index=False)