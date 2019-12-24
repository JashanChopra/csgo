"""
Set of helper functions for basic file I/O, data cleaning, and other misc tasks
"""
import pandas as pd


def importData():
    """
    Imports csgo data from original .csv sheet
    :return: data: pandas dataframe of game information, NaN's removed, some columns removed.
    """
    import pathlib

    # path directories
    homepath = pathlib.Path.cwd()
    datadir = pathlib.PurePath.joinpath(homepath, r'original.csv')

    # import, drop some columns, remove extra rows
    data = pd.read_csv(datadir)
    data.drop(columns=['W', 'Unnamed: 16', 'ELO'], inplace=True)
    data.dropna(how='any', inplace=True)

    # return data
    return data


def removeTies(data):
    """
    Remove matches with a win indicator of 2, these are ties and add another detection that is not needed,
    another option in the future would be to count ties as losses
    :param data: main dataset of csgo matches returned from importData
    :return: data: same dataset but with removed matches
    """

    data = data[data['Win = 1'] < 2]

    return data


def removeRandoms(data):
    """
    Remove matches where randoms are on the team, these matches will bias the results that should only apply to a
    full five man stack
    """

    return data


def createFeatures(data):
    """
    Creates additional features on the dataset from the original set of variables
    :param data: main dataset of csgo matches returned from importData
    :return: data: dataset of csgo matches with additional features
    """

    data['kd_ratio'] = data['Kills'] / data['Deaths']   # add kill/death ratio column

    # total number of rounds in match
    strings = [x.split('-') for x in data['Scoreline']]
    data['total_rounds'] = [(int(x[0]) + int(x[1])) for x in strings]

    # map starting side to numeric values
    start_side = {'CT': 0, 'T': 1}
    data['num_start'] = data['Starting Side'].map(start_side)

    return data


