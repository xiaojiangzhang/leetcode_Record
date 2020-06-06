import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from 力扣_牛客刷题.Tencent广告算法大赛.precess import getData, generate_batch


class dnnModel:
    def init_op(self):
        # 构建输入数据占位符[样本数，特征数]
        with tf.variable_scope("data"):
            x = tf.placeholder(tf.float32, [None, 7])
            y_true = tf.placeholder(tf.int32, [None, 20])

        # 构建神经网络模型，初始化权重和偏置参数
        with tf.variable_scope("fc_model"):
            # 创建权重变量,将权重初始化为随机张量,大小为
            weight1 = tf.Variable(tf.random_normal([7, 64], mean=0.0, stddev=1.0), name='weight1')
            bias1 = tf.Variable(tf.constant(0.0, shape=[64]), name='bias1')
            y_pred1 = tf.matmul(x, weight1) + bias1
            # 1000,128
            weight2 = tf.Variable(tf.random_normal([64, 20], mean=0.0, stddev=1.0), name='weight2')
            bias2 = tf.Variable(tf.constant(0.0, shape=[20]), name='bias2')
            y_pred2 = tf.matmul(y_pred1, weight2) + bias2

        with tf.variable_scope("soft_cross"):
            loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true, logits=y_pred2))
        return x, y_true, loss, y_pred2


x, y_true, loss, y_pred2 = dnnModel().init_op()
train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
equal_list = tf.equal(tf.argmax(y_true, 1), tf.argmax(y_pred2, 1))
accuracy = tf.reduce_mean(tf.cast(equal_list, tf.float32))
init_op = tf.global_variables_initializer()
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init_op)
    x_data, y_data = getData()
    minMax = MinMaxScaler()
    x_data = minMax.fit_transform(x_data)
    # x_test = x_data[:10000]
    # y_test = y_data[:10000]
    step = 0
    for i in range(5):
        for x1, y1 in generate_batch(1000, x_data[10000:], y_data[10000:]):
            sess.run([train_op], feed_dict={x: x1, y_true: y1})
            step += 1
            if step % 300 == 0:
                print("训练第%d步，准确率为：%f" % (step, sess.run(accuracy, feed_dict={x: x1, y_true: y1})))
                saver.save(sess, './model/model')
    # test_accuracy = []
    # for x1, y1 in generate_batch(1000, x_test, y_test):
    #     test_accuracy.append(sess.run(accuracy, feed_dict={x: x1, y_true: y1}))
    # print("测试准确率为：{}".format(sum(test_accuracy) / len(test_accuracy)))

