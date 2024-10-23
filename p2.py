#function questions

#Question # 1
# def len_list(list1):
#   len_lst=len(list1)
#   return len_lst

# lis=len_list(["Taha","Ahmed","Kohli","Bumrah"])
# print(lis)


#Question # 2

def cal_fact(a):
  sum = 1 
  for i in range(1,a+1,1):
    sum = sum * i

  return sum

fact=cal_fact(5)
print("The factorial is : ",fact)