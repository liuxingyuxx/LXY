import tensorflow as tf 

#定义变量必须先定义  0是初始值
state = tf.Variable(0, name='counter')
print(state.name)

one = tf.constant(1)

new_value = tf.add(state, one)
# 把new_value这个变量加载到state上面
update = tf.assign(state, new_value)

init = tf.initialize_all_variables()   #must have if define variable 

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
