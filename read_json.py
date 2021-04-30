import pandas as pd
import json
# contact_url=str(input('Pls input your "list of contact" link:\n'))
contact_url='https://raw.githubusercontent.com/nguyenhoangthangbt/json2/main/contacts_sample.json'
df = pd.read_json(contact_url)
print(df['phone'])