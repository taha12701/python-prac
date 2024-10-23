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

def currency_cnv(usd):
  pkr=0.0036
  amount=(usd/pkr)
  return amount

output=currency_cnv(278.15)
print(f"The amount in usd is : {output:.2f}","Rs")

#Question # 4

# def currency_cnv(pkr):
#   usd=278.15
#   amount=(pkr/usd)
#   return amount

# amt=int(input("Enter amount in Pkr : "))
# output=currency_cnv(amt)
# print(f"The amount in usd is :  {output:.2f}$")
