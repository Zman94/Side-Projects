"""
Introduction to TensorFlow from website
"""
import tensorflow as tf
import numpy as np

# # Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
# x_data = np.random.rand(100).astype(np.float32)
# y_data = x_data * 0.1 + 0.3

# # Try to find values for W and b that compute y_data = W * x_data + b
# # (We know that W should be 0.1 and b 0.3, but TensorFlow will
# # figure that out for us.)
# W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
# b = tf.Variable(tf.zeros([1]))
# y  W * x_data + b

# # Minimize the mean squared errors.
# loss = tf.reduce_mean(tf.square(y - y_data))
# optimizer = tf.train.GradientDescentOptimizer(0.5)
# train = optimizer.minimize(loss)

# # Before starting, initialize the variables.  We will 'run' this first.
# init = tf.global_variables_initializer()

# # Launch the graph.
# sess = tf.Session()
# sess.run(init)

# # Fit the line.
# for step in range(201):
    # sess.run(train)
    # if step % 20 == 0:
        # print(step, sess.run(W), sess.run(b))

# # Learns best fit is W: [0.1], b: [0.3]
# node1 = tf.constant(3.0)
# node2 = tf.constant(4.0)

# node3 = tf.add(node1, node2)

# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# adder_node = a + b

# add_and_trple = adder_node*3

# print(sess.run(add_and_trple, {a: 3, b: 4.5}))
sess = tf.Session()


W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
init = tf.global_variables_initializer()

linear_model = W*x+b

squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)
for i in range(1000):
    sess.run(train, {x:[1,2,3,4], y:[0,-1,-2,-3]})

print(sess.run([W,b]))
