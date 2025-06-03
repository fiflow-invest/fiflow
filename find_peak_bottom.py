import pandas as pd

def find_peak(data, var='Close', local_top_number=1):
    extreme = pd.DataFrame()
    data_len = len(data)
    rolling_number = local_top_number * 2 + 1
    temp_df = data[['Date', var]]

    for i in range(data_len + 1 - rolling_number):
        j = i + rolling_number
        temp_data = temp_df[i:j]
        if temp_data[var].max() == temp_data[var].iloc[local_top_number]:  #
            temp_extreme = temp_data.iloc[[local_top_number]].copy()
            extreme = pd.concat([extreme, temp_extreme], axis=0)

    return extreme


def find_bottom(data, var='Close', local_top_number=1):
    extreme = pd.DataFrame()
    data_len = len(data)
    rolling_number = local_top_number * 2 + 1
    temp_df = data[['Date', var]]

    for i in range(data_len + 1 - rolling_number):
        j = i + rolling_number
        temp_data = temp_df[i:j]
        if temp_data[var].min() == temp_data[var].iloc[local_top_number]:
            temp_extreme = temp_data.iloc[[local_top_number]].copy()
            extreme = pd.concat([extreme, temp_extreme], axis=0)

    return extreme
