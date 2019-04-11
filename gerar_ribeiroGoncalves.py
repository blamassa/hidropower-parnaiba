import pandas as pd
import numpy as np

ts = pd.read_csv('vazoes_C_34060000.csv', encoding='latin1', error_bad_lines=False, delimiter=';', index_col=False, decimal=",")
ts['Data'] = pd.to_datetime(ts['Data'],infer_datetime_format=True)

ts['Mes'] = ts['Data'].dt.day
ts['Ano'] = ts['Data'].dt.year


# Concertando os meses 31
ts['Mes'] = np.where(ts['Mes'] != 31, ts['Mes'], 10 )
ts['mesStr'] = ts['Mes'].replace({1: 'Jan',
                   2: 'Feb',
                   3: 'Mar',
                   4: 'Apr',
                   5: 'May',
                   6: 'Jun',
                   7: 'Jul',
                   8: 'Aug',
                   9: 'Sep',
                  10: 'Oct',
                  11: 'Nov',
                  12: 'Dec'})
to_csv = ts[['Mes','Ano','Media']]
to_csv.columns = ['month', 'year', 'vazao']
# Adding col data_ticks
to_csv['data_ticks'] = to_csv['year'].astype('str') + '-' + to_csv['month'].astype('str')
to_csv.sort_values(['year','month']).to_csv('ribeiroGon.csv')

