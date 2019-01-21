import pandas as pd

df1 = pd.DataFrame({
    'HPI':[80, 85, 88, 85],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': ['50,55,65,55']},
    index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({
    'HPI':[80, 85, 88, 85],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': ['50,55,65,55']},
    index = [2004, 2005, 2006, 2007])

df3 = pd.DataFrame({
    'HPI':[80, 85, 88, 85],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': ['50,55,65,55']},
    index = [2008, 2009, 2010, 2011])


# print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))
df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

print()
joined = df1.join(df3)

print(joined)
