import random
import matplotlib.pyplot as plt
import seaborn as sns


def gain(n):
    res = []
    total = 0
    for i in range (1, n + 1):
        j = 0
        win = False
        while j < i and not win and pow(2, j) <= 10000000:
            j = j + 1
            win = random.randint(0, 1) == 1
        total += pow(2, j) * win
        res.append(total / i)
    return res


def plot(simulations):
    x = range(len(simulations))
    plt.plot(x, simulations)


if __name__ == '__main__':
    sns.set(style="white", palette="muted", color_codes=True)
    for i in range(20):
        plot(gain(100000))

    plt.title("St. Petersburg Paradox")
    plt.xlabel("Runs")
    plt.ylabel("Average gain")
    plt.show()
