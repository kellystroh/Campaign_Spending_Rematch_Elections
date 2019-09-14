import pandas as pd
import numpy as np
import scipy as sp
import scipy.stats as stats

results_raw = pd.read_csv('data/dime.csv', low_memory=False)

col_list = ['election', 'cycle', 'Cand.ID', 'ICPSR', 'name', 'lname', 'fname','party', 
            'state', 'seat', 'district', 'Incum.Chall', 'num.givers', 'num.givers.total', 'cand.gender',
            'total.disbursements', 'total.pc.contribs', 'contribs.from.candidate', 'total.receipts',
            'total.indiv.contrib', 'total.pac.contribs', 'ran.general','gen.elec.stat', 
            'gen.elect.pct', 'winner', 'district.partisanship']

results = results_raw.loc[:, col_list]
results = results[results['ran.general']==1]
results = results[~results['gen.elect.pct'].isna()]
results = results[results.seat == 'federal:house']

results['race_ID'] = results['cycle'].astype(str) + "-"+ results['district'].astype(str)

num_cand = results.race_ID.value_counts()
num_cand_df = pd.DataFrame()
num_cand_df = num_cand[num_cand>1]
results = results[results['race_ID'].isin(num_cand_df.reset_index()['index'])]
results = results[results['gen.elect.pct'] != '?? ']

results.loc[:,'gen.elect.pct'] = results['gen.elect.pct'].astype(float).copy()
results = results[results['gen.elect.pct']>0]
# edit for consistency
results.loc[13800, 'gen.elect.pct'] = 48.01
results.loc[23340, 'gen.elect.pct'] = 45.01

# find indices of top 2 candidates per race 
top2_cand = results.groupby('race_ID')['gen.elect.pct'].nlargest(2)

# make dictionary with values equal to set of names of top 2 candidates 
cand_pair_dct = {}
for pair in top2_cand.index:
    cand_id = results.loc[pair[1], 'Cand.ID']
    if pair[0] not in cand_pair_dct:
        cand_pair_dct[pair[0]] = []
    cand_pair_dct[pair[0]].append(cand_id)

cand_pair_dct2 = {}
for pair in top2_cand.index:
    cand_id = results.loc[pair[1], 'ICPSR']
    if pair[0] not in cand_pair_dct2:
        cand_pair_dct2[pair[0]] = []
    cand_pair_dct2[pair[0]].append(cand_id)

results.loc[:,'top2'] = results['race_ID'].copy().apply(lambda x: cand_pair_dct[x])

from itertools import chain
rev_dict = {}
for key, value in cand_pair_dct.items():
    rev_dict.setdefault(str(value), set()).add(key)
rematch_sets = [sorted(values) for key, values in rev_dict.items() if len(values) > 1]

rematch_cand = [list(values) for values in cand_pair_dct2.values()]

rematch_race_id = []
for y in rematch_sets:
    for x in y:
        rematch_race_id.append(x)

rematch_cand_id = []
for y in rematch_cand:
    for x in y:
        rematch_cand_id.append(x)    

rematch_cand_id = list(set(rematch_cand_id))

results = results[results['ICPSR'].isin(rematch_cand_id)]

results.to_csv('data/candidate_df.csv' , index=False)