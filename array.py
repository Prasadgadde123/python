n=[[1,2,3],
   [4,5,6],
   [7,8,9] 
  ]
m=[[9,8,7],
   [6,5,4],
   [3,2,1]
  ]
result=[[n[i][j]+m[i][j] for i in range(len(n))] for j in range(len(n[0]))]
for r in result:
    print (r)  
