#激励函数解决不能用线性方程y = Wx解决的问题
# y = AF(Wx)  掰弯利器    激励函数必须是可微分的
import tensorflow as tf
import numpy as np

#in_size表示输入多少个单位代表行  out_size代表列
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]) )
    biases = tf.Variable(tf.zores[1, out_size] + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases 

    if activation_function is None:
        outputs = Wx_plus_b 
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs

x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random_normal(0, 0.05, x_data.shape) 
y_data = np.square(x_data) - 0.5 + noise 

xs = tf.placeholder([None, 1])
ys = 
