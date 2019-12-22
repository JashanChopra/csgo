from helperFuncs import importData


if __name__ == "__main__":

    data = importData()
    print('Data Imported & Cleaned')

    data = removeTies(data)
    print('Tie Matches Removed')