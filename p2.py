#function questions

#Question # 1
# def len_list(list1):
#   len_lst=len(list1)
#   return len_lst

# lis=len_list(["Taha","Ahmed","Kohli","Bumrah"])
# print(lis)


#Question # 2

# def cal_fact(a):
#   sum = 1 
#   for i in range(1,a+1,1):
#     sum = sum * i
#   return sum
# fact=cal_fact(5)
# print("The factorial is : ",fact)

#Question # 3

# def currency_cnv(usd):
#   pkr=0.0036
#   amount=(usd/pkr)
#   return amount

# output=currency_cnv(278.15)
# print(f"The amount in usd is : {output:.2f}","Rs")

#Question # 4

# def currency_cnv(pkr):
#   usd=278.15
#   amount=(pkr/usd)
#   return amount

# amt=int(input("Enter amount in Pkr : "))
# output=currency_cnv(amt)
# print(f"The amount in usd is :  {output:.2f}$")


#Question # 5

# def print_list(list1):
#   for item in list1:
#     print(item,end='')
  
# print_list(["Babar","Azam","Shaheen","Afridi"])


#Question # 6

# def max_num(a,b,c):
#   if(a>b and a>c):
#     print("A is greater")
#   elif(b>a and b>c):
#     print("B is greater")
#   else:
#     print("C is greater")

# max_num(5,27,2)

#Question # 7

# def rev_str(str):
#   reverse=''
#   st=len(str)
#   while st>0:
#     reverse +=str[st-1]
#     st = st-1

#   return reverse
  
# output=rev_str('Taha')
# print(output)
    

#Question # 8

def cal_avg(n):
  n=int(input("Enter no of items : "))
  sum=0
  for i in range(0,n,1):
    k=int(input("Enter a number : "))
    sum=sum+k
  print("The sum is equal to : ", sum)
  avg=(sum)/n
  print(f"The average is equal to {avg:.2f} ")  
cal_avg(4)

