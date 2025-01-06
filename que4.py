# str1="James Anderson"
# a=str1[0:3:2]
# b=str1[-3:]
# print(a+ "_" +b)

# var = "haldia"
# a=var[-1:-4:-1]
# b=var[2::-1]
# result= a+ " " +b
# c=result.capitalize()
# print(c)

# s1="Ynf"
# s2="PYnative"
# print(s1==s2)

# str1 = "Emma-is-a-data-scientist"
# x=str1.split("-")
# print(x)

# totalMoney=1000
# quantity=3
# price=450
# main_price = float(price)/quantity
# print("I have",totalMoney,"dollars so I can buy",quantity,"football for each of",main_price,"dollars")

# str1 = "/*Jon is @developer & musician"
# str2 = str1.replace("/*","").replace("@","").replace("&","")
# print(str2)

import re
str1 = "/*Jon is @developer & musician"
str2 = re.sub(r'[/*@&]', '', str1)
print(str2)

