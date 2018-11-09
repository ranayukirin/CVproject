import tensorflow as tf

initial = tf.truncated_normal([10, 128, 128, 1], stddev=0.1)
test = tf.Variable(initial, name='test')