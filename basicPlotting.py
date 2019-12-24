"""
Set of helper functions for initial data exploration, basic plots, etc
"""

import matplotlib.pyplot as plt
import seaborn as sns


def winRelation(data):
    pass


def multivariateTest(data):

    sns.violinplot(x='Starting Side', y='total_rounds', hue='Win = 1', data=data, split=True)
    plt.show()

    pass


def sideDist(data):
    """
    Creates distribution plots for CT and T side to compare the win and loss rate to the number of kills
    :param data: main dataset of the csgo data
    :return: None
    """

    f, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

    # separate dataframes by starting side
    ct = data[data['Starting Side'] == 'CT']
    t = data[data['Starting Side'] == 'T']

    # details of plots
    nbinsT = 10
    nbinsCT = 6

    # plot CT data
    ax = sns.distplot(ct[ct['Win = 1'] == 1].Kills, bins=nbinsCT, label='win', ax=axes[0], kde=False)
    ax = sns.distplot(ct[ct['Win = 1'] == 0].Kills, bins=nbinsCT, label='loss', ax=axes[0], kde=False)
    ax.legend()
    ax.set_title('CT Starting Side')

    # plot T data
    ax = sns.distplot(t[t['Win = 1'] == 1].Kills, bins=nbinsT, label='win', ax=axes[1], kde=False)
    ax = sns.distplot(t[t['Win = 1'] == 0].Kills, bins=nbinsT, label='loss', ax=axes[1], kde=False)

    ax.legend()
    _ = ax.set_title('T Starting Side')

    plt.show()





