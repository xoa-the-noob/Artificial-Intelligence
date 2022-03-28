pointlist = [('Medicine A',1,1),('Medicine B',2,1),('Medicine C',4,3),('Medicine D',5,4)]

centroid1 = [1,1]
centroid2 = [2,1]
i,j,k,l,m,n=0,0,0,0,0,0
temp1,temp2=0,0
distance2 = []
distance1 = []
cluster = []
tempcluster = []

while(1):
    
    for i in range(4):
        temp1 = pow( (pow((pointlist[i][1] - centroid1[0]),2) + pow((pointlist[i][2] - centroid1[1]),2)) , 1/2 )
        temp2 = pow( (pow((pointlist[i][1] - centroid2[0]),2) + pow((pointlist[i][2] - centroid2[1]),2)) , 1/2 )
        distance1.append(temp1)
        distance2.append(temp2)
        
    cluster.clear()
    for j in range(4):
        if(distance1[j]<distance2[j]):
            cluster.append(1)
        if(distance2[j]<distance1[j]):
            cluster.append(2)
            
    if( tempcluster == cluster ):
        break
    if( tempcluster != cluster ):
        centroid1.clear()
        centroid2.clear()
        distance1.clear()
        distance2.clear()
        x1,y1,x2,y2 = 0,0,0,0
        cnt1,cnt2 = 0,0

        for k in range(4):
            if ( cluster[k] == 1 ):
                x1 += pointlist[k][1]
                y1 += pointlist[k][2]
                cnt1 = cnt1+1
            if ( cluster[k] == 2 ):
                x2 += pointlist[k][1]
                y2 += pointlist[k][2]
                cnt2 = cnt2 + 1
        centroid1.append(x1/cnt1)
        centroid1.append(y1/cnt1)
        centroid2.append(x2/cnt2)
        centroid2.append(y2/cnt2)
        tempcluster.clear()
        tempcluster = cluster.copy()
       
print('Group 1:')
for l in range(4):
    if(cluster[l] == 1):
        print(pointlist[l][0])
print('Group 2:')
for l in range(4):
    if(cluster[l] == 2):
        print(pointlist[l][0])
        
    






  

