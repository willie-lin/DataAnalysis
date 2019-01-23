import pandas as pd
import quandl

api_key = 'tA69P8uAeoLBkoate1xB'
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(fiddy_states)
# print(fiddy_states[0])
# print(fiddy_states[0][0])
main_df = pd.DataFrame()
for abbv in fiddy_states[0][1][2:]:
    # print(abbv)
    # print("FMAC/HPI_" + str(abbv))

    # print("FMAC/HPI_{}".format(abbv))

    # for abbv in fiddy_states[0][1][2:]:
    # query = "FMAC/HPI_{}".format(abbv)
    query = "FMAC/HPI_" + str(abbv)
    # print(abbv)
    # print("FMAC/HPI_" + str(abbv))
    #
    # print("FMAC/HPI_{}".format(abbv))
    df = quandl.get(query, authtoken=api_key)

    if main_df.empty:
        main_df = df
    else:
        main_df = main_df.join(df, how='left', lsuffix='_left', rsuffix='_right')

print(main_df.head())