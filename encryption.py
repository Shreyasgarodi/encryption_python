import pickle
file=open('PICKLE.txt','wb')
k=[1,2,3,4,5]
encode=pickle.dumps(k)
file.write(encode)
file.close()
