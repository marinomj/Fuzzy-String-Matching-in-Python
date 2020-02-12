


from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import pandas as pd


dataDirectory = '~/Desktop/'
showFile = pd.read_excel(dataDirectory + 'TV Shows.xlsx', 'Sheet1')

s1 = pd.DataFrame(showFile['Source_1']).dropna() 
s2 = pd.DataFrame(showFile['Source_2']).dropna()


source1 = []
similarity = []
for i in s1.Source_1:
        ratio = process.extract( i, s2.Source_2, limit=1)
        source1.append(ratio[0][0])
        similarity.append(ratio[0][1])

s1['Source_2'] = pd.Series(source1)
s1['similarity'] = pd.Series(similarity)
s1.head(3)


source2 = []
similarity = []
for i in s2.Source_2:
        ratio = process.extract( i, s1.Source_1, limit=1)
        source2.append(ratio[0][0])
        similarity.append(ratio[0][1])

s2['Source_1'] = pd.Series(source2)
s2['similarity'] = pd.Series(similarity)
s2.head(3)




"""
compare = pd.MultiIndex.from_product([s1['Source_1'],s2['Source_2']]).to_series()

def metrics(tup):
    return pd.Series([fuzz.ratio(*tup),
                      fuzz.token_sort_ratio(*tup)],
                     ['ratio', 'token'])

op = compare.apply(metrics)
op.to_csv(dataDirectory + 'tvshows.csv')

op1 = compare.apply(metrics).unstack().idxmax().unstack(0)
op1.to_csv(dataDirectory + 'tvshows1.csv')

compare.apply(metrics).unstack(0).idxmax().unstack(0)
"""



"""
actual_email = []
similarity = []
for i in hr.full_name:
        ratio = process.extract( i, it.username, limit=1)
        actual_email.append(ratio[0][0])
        similarity.append(ratio[0][1])
hr['actual_email'] = pd.Series(actual_email)
hr['actual_email'] = hr['actual_email'] + '@giantbabybibs.org'
hr['similarity'] = pd.Series(similarity)
hr.head(3)
"""
