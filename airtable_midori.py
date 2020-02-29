from airtable import Airtable
import pandas as pd

airtable = Airtable('apph68V1U671SqRvx', 'Production Kitchen',api_key = 'keyn8MW3BtD2ucvSf')
records = airtable.get_all(view='Production overview')
labels_midori = pd.DataFrame.from_records((r['fields'] for r in records))
print(df.head)