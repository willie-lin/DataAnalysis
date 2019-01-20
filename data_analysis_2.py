import pandas as pd

df = pd.read_csv('data/YALE-NHPI.csv')

# print(df)
# print(df.head())
# df.set_index('Date', inplace=True)
#
# df.to_csv('newcsv2.csv')
#
# df = pd.read_csv('newcsv2.csv')
# print(df.head())
#
# df = pd.read_csv('newcsv2.csv', index_col=0)
# print(df.head())
#
# df.columns = ['Austin_HPI']
# print(df.head())
#
# df.to_csv('newcsv3.csv')
# df.to_csv('newcsv4.csv', header=False)
#
# df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'], index_col=0)
# print(df.head())
#
# df.to_html('example.html')

df = pd.read_csv('newcsv4.csv', names=['Date', 'Austin_HPI'], index_col=0)
print(df.head())

df.rename(columns={'Austin_HPI': 'AAAA_HPI'}, inplace=True)

print(df.head())