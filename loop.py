#!/usr/bin/env python
# coding: utf-8

# For Loop & While Loop ( Questions)
# 
# 1. Write a program to print all natural numbers from 1 to n. – using while
# loop
# 
# 2. Write a program to print all natural numbers in reverse (from n to 1). –
# using while loop
# 
# 3. Write a program to print all alphabets from a to z. – using while loop
# 
# 4. Write a program to print all even numbers between 1 to 100. – using
# while loop
# 
# 5. Write a program to find the sum of all odd numbers between 1 to n.
# 
# 6. Write a program to count the number of digits in a number.
# 
# 7. Write a program to calculate the sum of digits of a number.
# 
# 8. Write a program to find the first and last digit of a number.
# 
# 9. Write a program to find the sum of first and last digit of a number.
# 
# 10.Write a program to enter a number and print its reverse.
# 
# 11.Write a program to find the power of a number using for loop.
# 
# 12.Write a program to find all factors of a number.
# 
# 13.Write a program to calculate the factorial of a number.
# 
# 14.Write a program to find LCM of two numbers.
# 
# 15.Write a program to check whether a number is Prime number or not.
# 
# 16.Write a program to print all Prime numbers between 1 to n.
# 
# 17.Write a program to find all prime factors of a number.
# 
# 18.Write a program to check whether a number is an Armstrong number or
# not.
# a. An Armstrong number is a n-digit number that is equal to the sum
# of the nth power of its digits. For example –
# 6 = 61 = 6
# 371 = 33 + 73 + 13 = 371
# 
# 19.Write a program to check whether a number is Strong number or not
# a. Strong number is a special number whose sum of factorial digits is
# equal to the original number.
# For example: 145 is a strong number. Since, 1! + 4! + 5! = 145
# 
#     20.Write a program to check whether a number is perfect number or not
# 
# a. Perfect number is a positive integer which is equal to the sum of
# its proper positive divisors.
# For example: 6 is the first perfect number
# Proper divisors of 6 are 1, 2, 3
# Sum of its proper divisors = 1 + 2 + 3 = 6.
# Hence 6 is a perfect number.
# 
# 21.Write a program to print fibonacci series upto n terms
# a. Fibonacci series is a series of numbers where the current number
# is the sum of the previous two terms. For Example: 0, 1, 1, 2, 3, 5,
# 8, 13, 21, ... , (n-1th + n-2th)
# 
# 22.Write a program to find ones complement of a binary number
# a. One's complement of a binary number is defined as value
# obtained by inverting all binary bits. It is the result of swapping all
# 1s to 0s and all 0s to 1s.
# 

# In[7]:


#1
n=100
i=1
sum=0
while(i<n):
    sum=sum+i
    i+=1
print(sum)
    


# In[9]:


#2
n=100
i=1
sum=0
while(i<=n):
    sum=sum+n
    n-=1
print(sum)


# In[17]:


#3
a='a'
while a<="z":
    print(a)
    a=chr(ord(a)+1)


# In[18]:


#4
num=2
while num<=10):
    print(num, end=' ')
    num+=2


# In[20]:


#5
num=1
sum=0
while num<=100:
    sum=sum+num
    num+=2
print(sum)    


# In[22]:


#6
number=int(input("Enter a number: "))
count=0
while number!=0:
    number//=10
    count+= 1
print("Number of digits:",count)


# In[23]:


#7
number=int(input("Enter a number: "))
sum=0
while number!=0:
    rev=number%10
    sum=sum+rev
    number//=10
print("sum of digits:",sum)


# In[26]:


#8
number=int(input("Enter a number: "))
temp=number
while number!=0:
    rev=number%10
    number//=10
first_digit=temp%10
last_digit=rev%10
print(first_digit,last_digit)


# In[27]:


#9
number=int(input("Enter a number: "))
temp=number
while number!=0:
    rem=number%10
    number//=10
first_digit=temp%10
last_digit=rev%10
print(first_digit+last_digit)


# In[31]:


#10
number=int(input("Enter a number: "))
rev=0
while number!=0:
    rem=numbe%10
    rev=rev*10+rem
    number//=10
print(rev)


# In[37]:


#11
number=int(input("Enter a number: "))
pow=int(input("Enter the power: "))
i=1
res=1
while i<=pow:
    res=res*number
    i+=1
print(res)


# In[39]:


#12
number=int(input("Enter a number: "))
factor=1
while factor<=number:
    if number%factor==0:
        print("factor is ",factor)
    factor+=1


# In[41]:


#13
number=int(input("Enter a number: "))
fact=1
while number>0:
    fact=fact*number
    number-=1
print(fact)


# In[ ]:


#14
number1=int(input("Enter a number1: "))
number2=int(input("Enter a number2: "))

i=max(number1,number2)
while True:
    if number1%i==0 and number2%i==0:
        print("LCM is ",i)
        break
    else:
        i+=1


# In[95]:


#15
number1=int(input("Enter a number1: "))
is_prime=True
if number1<=1:
    is_prime=False
else:
    i = 2
    while i<number1:
        if number1%i==0:
            is_prime = False
            break
        i+=1

print(is_prime)


# In[100]:


#16  
number=int(input("Enter a number: "))
i=1
while i<=number:
    div=2
    while div<i:
        if i%div==0:
            break
        div+=1
    else:
        print(i)
    i+=1


# In[103]:


#17
number=int(input("Enter a number: "))
i=1
sum=0
while i<=number:
    div=2
    while div<i:
        if i%div==0:
            break
        div+=1
    else:
        sum=sum+i
    i+=1
print(sum)


# In[96]:


#18
num=int(input("Enter a number: "))
sum=0
temp=num

while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10

if num==sum:
    print(f"{num} is a Armstrong number")
else:
    print(f"{num} is not a Armstrong number")


# In[98]:


#19
num=int(input("Enter a number: "))
temp=num
sum_of_powers = 0
sum_fact=0

while temp > 0:
    digit = temp % 10
    fact=1
    while digit>0:
        fact=fact*digit
        digit-=1
    sum_fact=sum_fact+fact
    temp //= 10
if num==sum_fact:
    print("strong number")



# In[69]:


#20
num = int(input("Enter a number: "))
temp=num
i=1
sum=0
while i<num:
    if num%i==0:
        sum=sum+i
    i+=1
if temp==sum:
    print("perect number")
else:
    print("not a perfect number")
    


# In[73]:


#21
num = int(input("Enter a number: "))
first=0
second=1
print(first)
print(second)
sum=1
while sum<=num:
    sum=first+second
    print(sum)
    first=second
    second=sum


# In[ ]:


#22


# In[104]:


a=input("Enter a binary number: ")
i=0
print("One complement:",end=" ")
while i<len(a):
    if a[i]=='1':
        print('0',end="")
    else:
        print('1',end="")
    i+=1


# In[85]:





# In[84]:





# In[97]:




