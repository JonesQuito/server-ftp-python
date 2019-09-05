import pickle
lista = [1, 2, 3, 'quatro', 5]
ls = pickle.dumps(lista)
print('Lista serializada:', ls)
print(type(ls))

lr = pickle.loads(ls)
print('Lista restaurada: ', lr)