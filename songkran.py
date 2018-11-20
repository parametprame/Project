import matplotlib.pyplot as plt
def demol():
    x = range(5)
    y = (2992, 3373, 3447, 3690, 3724)
    xtrik = ("2557", "2558", "2559", "2560", "2561")
    plt.bar(x, y)
    plt.xticks(x, xtrik)
    plt.title("Number of deaths during the Songkran festival over the past 5 years")
    plt.show()
if __name__ == '__main__':
    demol()
