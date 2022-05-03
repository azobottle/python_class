import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    X = np.array([[1, 1, 0]])  # 补零
    Y = np.array([[0.9, 0.1]])
    Theta1 = np.array([[-0.4, 0.2, 0.1], [-0.2, 0.4, 0.1]])
    Theta2 = np.array([[0.1, -0.2, 0.1], [0.4, -0.1, 0.1]])
    alpha = 0.3
    plotx = []
    ploty = []
    for i in range(200):
        # forward
        a1 = X.T
        z2 = np.dot(Theta1, a1)
        a2 = np.vstack((np.ones(1), sigmoid(z2)))
        z3 = np.dot(Theta2, a2)
        a3 = sigmoid(z3)
        # cost
        J = np.sum(-Y.T * np.log(a3) - (1 - Y.T) * np.log(1 - a3))
        plotx.append(i)
        ploty.append(J)
        # backward
        delta3 = a3 - Y.T
        delta2 = np.dot(Theta2.T, delta3) * a2 * (1 - a2)
        Delta1 = np.dot(delta2[1:, ], a1.T)
        Delta2 = np.dot(delta3, a2.T)
        Theta1 = Theta1 - alpha * Delta1
        Theta2 = Theta2 - alpha * Delta2
    plt.plot(plotx, ploty)
    plt.xlabel('Time')
    plt.ylabel('Cost')
    plt.show()