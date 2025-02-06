

def countit(row,column,lst):
    count=0
    while row!=2 or column!=2:
        if row>2:
            lst[row-1],lst[row]=lst[row],lst[row-1]
            row-=1
            count+=1
          
        elif row<2:
            lst[row],lst[row+1]=lst[row+1],lst[row]
            row=row+1
            count+=1
           
        elif column>2:
            lst[2][column-1],lst[2][column]=lst[2][column],lst[2][column-1]
            column=column-1
            count+=1
            
        elif column<2:
            lst[2][column],lst[2][column+1]=lst[2][column+1],lst[2][column]
            count+=1
            column=column+1
           
    return count 
mega_lst=[]
for i in range(5):
    mini_list=list(map(int,input().split()))
    mega_lst.append(mini_list)
for i in mega_lst:
    for j in i:
        if j==1:
            row=mega_lst.index(i)
            column=i.index(j)
            break 
    


print(countit(row,column,mega_lst))


        

        
