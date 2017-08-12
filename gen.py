import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('data/mnist', one_hot=True)

def xavier_init(size):
    in_dim = size[0]
    xavier_Stddv = 1.0 / tf.sqrt(in_dim/2.0)
    return tf.random_normal(shape=size, stddev=xavier_stddev)


X = tf.placeholder(tf.float32, shape=[None, 784], name='X')

W1_dis = tf.Variable(xavier_init([784, 128]), name='W1_dis')
b1_dis = tf.Variable(tf.zeros(shape=[128]), name ='b1_dis')

W2_dis = tf.Variable(xavier_init([128, 1]), name='W1_dis')
b2_dis = tf.Variable(tf.zeros(shape=[1]), name ='b1_dis')

theta_dis = [W1_dis, W2_dis, b1_dis, b2_dis]

z = tf.placeholder(tf.float32, shape = [None, 100], name='Z')

W1_gen = tf.Variable(xavier_init([100, 128]), name='W1_gen')
b1_gen = tf.Variable(tf.zeros(shape=[128]), name='b1_gen')

W2_gen = tf.Variable(xavier_init([128, 784]), name='W2_gen')
b2_gen = tf.Variable(tf.zeros(shape=[784]), name='b2_gen')

theta_gen = [W1_gen, W2_gen, b1_gen, b2_gen]

def random_Z(z1, z2):
    return np.random.uniform(-1.0, 1.0, size=[z1, z2])

def gen(z):
    h1_gen = tf.nn.relu(tf.matmul(z, W1_gen) + b1_gen)
    log_prob_gen = tf.matmul(h1_gen, W2_gen) + b2_gen
    prob_gen = tf.nn.sigmoid(log_prob_gen)

    return prob_gen

def dis(x):
    h1_dis = tf.nn.relu(tf.matmul(x, W1_dis) + b1_dis)
    logit_dis = tf.matmul(h1_dis, W2_dis) + b2_dis
    prob_dis = tf.nn.sigmoid(logit_dis)

    return prob_dis, logit_dis

def plot(samples):
    fig = plt.figure(figsize =(4,4))
    grid = gridspec.GridSpec(4,4)
    grid.update(wspace=0.1, hspace=0.1)

    for i, sample in enumerate(samples):
        ax = plt.subplot(grid[i])
        plt.axis('off')
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('equal')
        plt.imshow(sample.reshape(28, 28), cmap='gray')

    return fig

sample_gen = gen(Z)
real_dis, logit_real_dis = dis(X)
fake_dis, logit_fake_dis  = dis(sample_gen)

loss_real_dis = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit_real_dis, labels=tf.ones_like(logit_real_dis)))
loss_fake_dis = tf.reduce_mean(tf.nn.sigmoid_cross_Entropy_with_logits(logits=logit_fake_dis, labels=tf.zeros_like(logit_fake_dis)))
loss_dis = loss_real_dis + loss_fake_dis
loss_gen = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logit_fake_dis, labels=tf.ones_like(logit_fake_dis)))

solver_dis = tf.train.AdamOptimizer().minimize(loss_dis, var_list=theta_dis)
solver_gen = tf.train.AdamOptimizer().minimize(loss_gen, var_list=theta_gen)


batch_size = 120
dim_Z = 100

sess = tf.Session()
sess.run(tf.global_variables_initializer())

i = 0

for j in range(100000):
    if j%2000 == 0 :
        samples = sess.run(sample_gen, feed_Dict = {Z: random_z(16, dim_z)})
        fig = plot(samples)
        plt.show()
        i += 1
        plot.close(fig)

    X_batch, _ = mnist.train.next_batch(batch_size)

    _, loss_curr_dis = sess.run([solver_dis, loss_dis], feed_dict={X:X_batch, Z:random_Z(batch_size, dim_Z)})

    _, loss_curr_gen = sess.run([solver_gen, loss_gen], feed_dict={Z:random_Z(batch_size, dim_Z)})

    if j%2000 == 0:
        print('Iteration: {}'.format(j))
        print('Discriminator loss: {:.3}'.format(loss_curr_dis))
        print('Generator loss: {:.3}'.format(loss_curr_gen))
        print()

