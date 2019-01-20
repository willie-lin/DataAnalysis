import quandl as Quandl

api_key = 'tA69P8uAeoLBkoate1xB'

df = Quandl.get("FMAC/HPI_TX", authtoken=api_key)

print(df.head())