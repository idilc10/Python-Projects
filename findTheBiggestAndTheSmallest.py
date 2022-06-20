# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 11:47:03 2022

@author: IFK
"""

a=input("The first number:\n")
b=input("The second number:\n")
c=input("The third number:\n")

#for a is the biggest
if a>b and a>c and b>c:
  print("The biggest one is:",a)
  print("The smallest one is:",b)
elif a>b and a>c and c>b:
  print("The biggest one is:",a)
  print("The smallest one is:",c)
elif a>b and a>c and c==b:
  print("The biggest one is:",a,"b and c are equal to each other")

#for b is the biggest
elif b>a and b>c and a>c:
  print("The biggest one is:",b)
  print("The smallest one is:",a)
elif b>a and b>c and c>a:
  print("The biggest one is:",b)
  print("The smallest one is:",c)
elif b>a and b>c and c==a:
  print("The biggest one is:",b,"a and c are equal to each other")

#for c is the biggest
elif c>a and c>b and b>a:
  print("The biggest one is:",c)
  print("The smallest one is:",a)
elif c>a and c>b and a>b:
  print("The biggest one is:",c)
  print("The smallest one is:",b)
elif c>a and c>b and a==b:
  print("The biggest one is:",c,"a and b are equal to each other")

if a==b>c:
  print("a and b are equal to each other and bigger than c")
elif a==b<c:
  print("a and b are equal to each other and smaller than c")
elif b==c>a:
  print("b and c are equal to each other and bigger than a")
elif b==c<a:
  print("b and c are equal to each other and smaller than a")
elif a==c>b:
  print("a and c are equal to each other and bigger than b")
elif a==c<b:
  print("a and c are equal to each other and bigger than b")