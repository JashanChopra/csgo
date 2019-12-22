from helperFuncs import importData, removeTies, createFeatures


if __name__ == "__main__":

    data = importData()
    print('Data Imported & Cleaned')

    data = removeTies(data)
    print('Tie Matches Removed')

    data = createFeatures(data)
    print('Additional Features Created')