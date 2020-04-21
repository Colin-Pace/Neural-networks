import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

a = tf.Variable(1, name="a")
b = tf.Variable(2, name="b")
f = a + b

init = tf.compat.v1.global_variables_initializer()
with tf.Session() as s:
	init.run()
	print("f value: ")
	print( f.eval() )