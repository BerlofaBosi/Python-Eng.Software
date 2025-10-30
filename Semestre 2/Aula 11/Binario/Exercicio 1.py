import pickle

def create(name, obj):
    arq = open(f'{name}', 'wb')
    pickle.dump(obj, arq)

def read():
    