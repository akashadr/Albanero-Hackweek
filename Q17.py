if __name__=="__main__":
  
  N =  [

  Sum=0
  
  for i in range(len(N)):
    for j in range(len(N[0])):
      
      if(N[i][j]&1==0):
        Sum+=N[i][j]
  
  print(Sum)