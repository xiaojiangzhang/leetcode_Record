import numpy as np


class LabelMap:
    '''
    将数据label中的年龄和性别转换为one-hot向量
    '''

    def __init__(self):
        self.hot = []
        for i in range(1, 11):
            for j in range(1, 3):
                self.hot.append([i, j])
        # print(self.hot)
        # print(len(self.hot))

    def label_to_one_hot(self, label):
        la = [0 for _ in range(20)]
        index = self.hot.index(list(label))
        la[index] = 1
        return np.array(la)

    def one_hot_to_label(self, index):
        # one_hot = list(one_hot)
        return self.hot[index]

# labelmap = LabelMap()
# res = labelmap.label_to_one_hot([4, 1])
# print(res)
# la = labelmap.one_hot_to_label(res)
# print(la)
