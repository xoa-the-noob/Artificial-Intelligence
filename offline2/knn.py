movielist = [
                    ('Up',2009,8.2,96),
                    ('Rio',2011,6.9,96),
                    ('Toy Story',1995,8.3,81),
                    ('The Lion King',1994,8.5,88),
                    ('Ice Age',2002,7.5,81)
              ]

X=str(input("Movie name :"))

i,j=0,0
temp1,s=0,0
k=1

distancelist = {}
  

for i in range(5):
    if(movielist[i][0] == X):
        break

for j in range(5):
    if( j != i ):
        s = 0  
        for k in range(4):
           if(k != 0 ):
               s = s + pow((movielist[i][k] - movielist[j][k]),2)
        temp1 = pow(s,1/2)
        distancelist[movielist[j][0]] = [temp1]


templist = sorted(distancelist.items(), key=lambda x:x[1])
sortdict = dict(templist)

print('The nearest neighbors are:')

print(list(sortdict.keys())[:3])



  

