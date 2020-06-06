import pandas as pd
import numpy as np
from random import shuffle

from 力扣_牛客刷题.Tencent广告算法大赛.label_map import LabelMap


def testData():
    print('read data ...........')
    data = pd.read_csv('dataP1.csv', index_col=0)
    print('samples is ', data.shape)
    data = data.drop(['user_id', 'creative_id'], axis=1)
    data = data.to_numpy()
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i][j] == '\\N':
                data[i][j] = 0
    data = data.astype(int)
    # data = pd.DataFrame(shuffle(list(data)))
    return data[:, :-2]


def getData(data=None):
    print('read data ...........')
    data = pd.read_csv('dataP1.csv', index_col=0)
    print('samples is ', data.shape)
    data = data.drop(['user_id', 'creative_id'], axis=1)
    data = data.to_numpy()
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if data[i][j] == '\\N':
                data[i][j] = 0
    data = data.astype(int)
    # data = pd.DataFrame(shuffle(list(data)))
    return data[:, :-2], data[:, -2:]


def generate_batch(batchsize, x_data, y_data):
    x_train, y_train = [], []
    label_map = LabelMap()
    for x in range(x_data.shape[0]):
        s = x_data[x]
        label = y_data[x]
        x_train.append(s)
        y_train.append(label_map.label_to_one_hot(label))
        if x != 0 and x % batchsize == 0:
            yield np.array(x_train), np.array(y_train)
            x_train.clear()
            y_train.clear()

# datax, datay = getData()
# print(datax.shape, datay.shape)
# print(datax[1], datay[1])
# for x, y in generate_batch(1000, datax, datay):
#     print(x.shape, y.shape)
#     print(x[1], y[1])
#     break
