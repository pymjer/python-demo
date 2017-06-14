import input_data
import tensorflow as tf


if __name__ == '__main__':
    mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
    sess = tf.InteractiveSession()
    x = tf.placeholder("float", [None, 784])
    W = tf.Variable(tf.zeros([784, 10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)

    # y_ 是实际的概率分布
    y_ = tf.placeholder("float", [None, 10])

    # 计算交叉熵，使其最小化
    cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

    # 梯度下降算法
    train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

    # Train
    tf.initialize_all_variables().run()

    # 开始训练模型，每次100条数据，循环1000次
    for i in range(1000):
        batch_xs, batch_ys = mnist.train.next_batch(100)
        train_step.run({x: batch_xs, y_: batch_ys})

    correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print(accuracy.eval({x: mnist.test.images, y_: mnist.test.labels}))
