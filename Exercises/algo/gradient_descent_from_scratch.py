import numpy as np

def gradient_descent(x, y, lr = 0.01, epoch = 3000):
    m, b = 0.0, 0.0

    for epochs in range(epoch):
        y_hat = m*x + b
        error = y - y_hat
        cost = np.mean(error**2)

        d_m = -2 * np.mean(x * error)
        d_b = -2 * np.mean(error)

        b -= d_b * lr
        m -= d_m * lr

        print(f"m = {m}, b = {b}, Epoch {epoch}  : cost {cost}, ")


if __name__ == "__main__":
    x= np.array([1, 2 , 3, 4, 5])
    y = np.array([5, 7, 9, 11, 13])
    gradient_descent(x, y)