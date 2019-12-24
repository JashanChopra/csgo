from helperFuncs import importData, removeTies, createFeatures, removeRandoms
from basicPlotting import multivariateTest


if __name__ == "__main__":

    data = importData()
    print('Data Imported')

    data = removeTies(data)
    data = removeRandoms(data)
    print('Data Cleaned & Trimmed')

    data = createFeatures(data)
    print('Additional Features Created')



