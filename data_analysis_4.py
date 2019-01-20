import quandl as Quandl
import pandas as pd

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(fiddy_states)
print(fiddy_states[0])
print(fiddy_states[0][0])
for abbv in fiddy_states[0][1][2:]:
    # print(abbv)
    print("FMAC/HPI_" + str(abbv))

    print("FMAC/HPI_{}".format(abbv))