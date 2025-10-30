import pickle

arq = open('arq.bin', 'rb')
a = pickle.load(arq)
print(a)

arq.close()
