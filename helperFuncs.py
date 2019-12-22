
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

