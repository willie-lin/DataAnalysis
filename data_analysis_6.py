import pandas as pd

df1 = pd.DataFrame({
    'Year':[2001, 2002, 2003, 2004],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [59,55,65,55]})
df2 = pd.DataFrame({
    'Year':[2001, 2002, 2003, 2004],
    'Int_rate': [2, 3, 2, 2],
    'US_GDP_Thousands': [50,55,65,55]})
    # index = [2001, 2002, 2003, 2004]}))


df3 = pd.DataFrame({
    'Year':[2001, 2002, 2003, 2004],
    'Unemployment': [7, 8, 9, 6],
    'Low_tier_HPI': [50, 52, 50, 53]})


df4 = pd.merge(df1, df2, on='Year')
# df4 = pd.merge(df1, df2, on='Year', how='left')
# df4.setindex("Year", inplace=True)

print(df4)
#
# print()
df1.set_index('Year', inplace=True)
df3.set_index('Year', inplace=True)
joined = df1.join(df3)

print(joined)

# merged = pd.merge(df1, df3, on='Year')
# merged.set_index('Year',inplace=True)
#
# print(merged)

