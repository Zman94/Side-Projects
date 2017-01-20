import pickle

data1 = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
with open('data.pickle', 'wb') as f:
    pickle.dump(data1, f)
