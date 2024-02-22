from .fertilizer_data import fertilizer_dic

import pandas as pd


def get_fertilizer_reco(crop_name, N, P, K):
    df = pd.read_csv('fertidataset.csv')

    nr = df[df['Crop'] == crop_name]['N'].iloc[0]
    pr = df[df['Crop'] == crop_name]['P'].iloc[0]
    kr = df[df['Crop'] == crop_name]['K'].iloc[0]

    n = nr-N
    p = pr-P
    k = kr-K
    temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
    max_value = temp[max(temp.keys())]
    if max_value == "N":
        if n < 0:
            key = 'NHigh'
        else:
            key = 'Nlow'
    elif max_value == "P":
        if p < 0:
            key = 'PHigh'
        else:
            key = 'Plow'
    else:
        if k < 0:
            key = 'KHigh'
        else:
            key = 'Klow'

    return fertilizer_dic.get(key, "No Advice Available")


# crop_name = "apple"
# N = 10
# P = 110
# K = 200

# recomendation = get_fertilizer_reco(crop_name, N, P, K)
# print(recomendation)
