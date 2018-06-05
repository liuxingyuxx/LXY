import tensorflow as tf 
import numpy as np 

#creat data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3 


###creat tensorflow structure start 

#Weight 可能是矩阵的形式 第一个是维度 第二个第三个数是范围
Weight = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
#初始值是零
biases = tf.Variable(tf.zeros([1]))

y = Weight*x_data + biases 

#误差
loss = tf.reduce_mean(tf.square(y-y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

#初始化
init = tf.initialize_all_variables()

###creat tensorflow structure end 

#SESSION就像一个指针
sess = tf.Session()
sess.run(init)   #very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weight), sess.run(biases))
