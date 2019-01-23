import pickle

import pandas as pd
import quandl

api_key = 'tA69P8uAeoLBkoate1xB'
# quandl.ApiConfig.api_key = 'tA69P8uAeoLBkoate1xB'
# quandl.ApiConfig.api_version = '2015-04-09'


def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][1][2:]
    # print(fiddy_states[0][1][2:])


# print(state_list())


def grab_initial_state_data():
    states = state_list()
    # print(states)
    main_df = pd.DataFrame()

    for abbv in states:
        # query = "FMAC/HPI_".format(abbv)
        query = "FMAC/HPI_" + str(abbv)
        # print(query)
        # query = "FMAC/HPI_" + str(abbv)

        df = quandl.get(query, authtoken=api_key)
        # print(df)

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, lsuffix='_a', rsuffix='_b')
            # print(main_df)
    print(main_df.head())

    pickle_out = open('fiddy_states.pickle', 'wb')

    pickle.dump(main_df, pickle_out)
    pickle_out.close()


grab_initial_state_data()
print(grab_initial_state_data())
#
# # print(fiddy_states)
# # print(fiddy_states[0])
# # print(fiddy_states[0][0])
#
# # main_df = pd.DataFrame()
#
# # for abbv in fiddy_states[0][1][2:]:
# #     # query = "FMAC/HPI_{}".format(abbv)
# #     query = "FMAC/HPI_" + str(abbv)
#     # print(abbv)
#     # print("FMAC/HPI_" + str(abbv))
#     #
#     # print("FMAC/HPI_{}".format(abbv))
#     df = Quandl.get(query, authtoken=api_key)
#
#     if main_df.empty:
#         main_df = df
#     else:
#         main_df = main_df.join(df,how='left', lsuffix='_left', rsuffix='_right')
#
# print(main_df.head())