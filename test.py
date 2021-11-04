import pickle
age=[]
y=input('do you want to open a new file: ')
if y=='y':
    x=int(input('ender your age: '))
    age.append(x)
    with open ('pickle_list.pickle','wb') as f:
        pickle.dump(age,f)
else:
    with open('pickled_list.pickle', 'rb') as f:    
        age = pickle.load(open('pickle_list.pickle','rb'))
        print(age[0])
