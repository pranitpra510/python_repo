mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[10,11,12],[13,14,15],[16,17,18]]
res=[]

for i in range(0,len(mat1)):
    for j in range(0,len(mat2)):
          res.append(mat1[i][j] + mat2[i][j])


print(res)

