import matplotlib.pyplot as plt

def plot(xlabel, ylabel, ylim, title, bars: dict[str, float]):
    """Plot a bar graph with the given parameters."""
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0, ylim)
    plt.title(title)
    plt.bar(list(bars.keys()), list(bars.values()), align='center')
    plt.show()


def plot_multi(xlabel, ylabel, ylim, title, hoge: dict[str, tuple[float, float]]):
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.ylim(0, ylim)
    plt.title(title)

    for key, value in hoge.items():
        plt.bar(key, value[0], width=0.3, align='center', color='blue') # male
        plt.bar(key, value[1], width=0.3, align='edge', color='red') # female

    plt.show()