print("please enter the quantity of each book")
b1 = int(input("Intro to python : "))
b2 = int(input("python lib cookbook : "))
b3 = int(input("DataScience In python : "))
b1_amt = 499.00*b1
b2_amt = 855.00*b2
b3_amt = 645.00*b3
t_price = b1_amt+b2_amt+b3_amt
final_amt = t_price+(t_price*0.12)+ 250
print("invoice---")s
print("GST = 12%" ,end = " ")
print("Delivery charges = 250")
print("Total amount for all the books is ",end = " ")
print("final_amt")
