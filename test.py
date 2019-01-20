import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')


def state_list():
    fiddy_states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
    return fiddy_states[0][1][2:]


def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_" + str(abbv)
        df = quandl.get(query, authtoken="zpFWg7jpwtBPmzA8sT2Z")
        df.columns = [str(abbv)]
        # df = df.pct_change() # percentage of every year
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0 # cumulative percentage change # compound

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    print(main_df.head())

    pickle_out = open('fiddy_states.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# grab_initial_state_data()

def HPI_Benchmark():
    df = quandl.get('FMAC/HPI_USA', authtoken="zpFWg7jpwtBPmzA8sT2Z")
    df.columns = ['United_States']
    # df.rename(columns={'Value':'United_States'}, inplace=True)
    df["United_States"] = (df["United_States"] - df["United_States"][0]) / df["United_States"][0] * 100.0
    return df

# Graph of HPI USA and all states
fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0)) # one 1 x 1 grid # 0,0 starting point

HPI_data = pd.read_pickle('fiddy_states.pickle')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how='mean')

print(HPI_data[['TX', 'TX1yr']].head())
# dropna
# any = default all missing data, all = Nan in both row

# fillna
# method='ffill' = take data fill forward, take previous value fill forward
# bfill = take data fill backward, take future value fill backward, too bias
# value = -999999, for machine learning outlier
HPI_data.fillna(inplace=True)
print(HPI_data[['TX', 'TX1yr']].head())

HPI_data[['TX', 'TX1yr']].plot(ax = ax1)

plt.legend(loc=4)
plt.show()