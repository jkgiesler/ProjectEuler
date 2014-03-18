#given a 20x20 grid find the largest product of numbers

text <- read.table("~/Dropbox/Life/code/Python/Python for git/Project Euler/textanaly.txt", quote="\"")

biggest=0
#check all vertical
for(i in 1:17){
    for(j in 1:20){
      z=i+3
      sum=1
      ans=text[i:z,j]
      for(x in 1:length(ans)){
        sum = sum*ans[x]
      }
      if(sum>biggest){
        biggest=sum
      }
    }
}
#check all horizontal
for(i in 1:20){
  for(j in 1:17){
    z=j+3
    sum=1
    ans=text[i,j:z]
    for(x in 1:length(ans)){
      sum = sum*ans[x]
    }
    if(sum>biggest){
      biggest=sum
    }
  }
}
#check all right diagonal
for(i in 1:17){
  for(j in 1:17){
    z=j+3
    y=i+3
    sum=1
    ans=text[i:y,j:z]
    for(x in 1:length(ans)){
      sum=sum*ans[x,x]
    }
    if(sum>biggest){
      biggest=sum
    }
  }
}
#check all left diagonal
for(i in 1:17){
  for(j in 17:1){
    z=j+3
    y=i+3
    sum=1
    ans=text[i:y,j:z]
    for(x in 1:length(ans)){
      sum=sum*ans[x,5-x]
    }
    if(sum>biggest){
      biggest=sum
    }
  }
}
biggest