
a,b,c,d,e,f=0,0,0,0,0,0
#bool variables to check the answer status of the each question.

print("\n\t\t\t\t\t\t\tAuthentication System\n\n")
print("Answer the following set of questions\n\n\n")
#using seven segment display for testing the user

print("  ---\t  ---\t  ---\t  ---\n")
print("     |\t     |\t |\t |   |\n")
print("     |\t     |\t |\t |   |\n")
print("  ---\t  ---\t  ---\t    \n")
print(" |  \t     |\t     |\t     |  \n")
print(" |  \t     |\t     |\t     |  \n")
print("  ---\t  ---\t  ---\t    \n")

first=input("1) Enter the next number in the above sequence\n")
if(first=='11'):
    a=1

#prime number sequence
second=input("\n2) Enter the value of the expression: 5*4 +2 -19\n")
if(second=='3'):
    b=1

print("\n3) Answer the following logical questinon\n")
print("If 1 + 4 = 5 \n"
     "2 + 5 = 12\n"
   "3 + 6 = 21 \n"
 "Then 8 + 12 = ?\n")
third=input()
if(third=='104'):
    c=1
# using the logic a+b=ab+a

fourth=input("\n4) Enter the number:'five hundred thirty six' in digits \n")
if(fourth=='536'):
    d=1

print("\n5) Answer the following logical question\n")
print("If 3,2,4 = 10\n"
        "4,3,5 =17\n"
       "5,4,6 = 26\n"
       "Then 7,6,8 = ?\n")

fifth=input()
if(fifth=='50'):
    e=1
# using the logic a,b,c = a*b+c

sixth=input("\n6) what is the most repeated letter in this sentence?\n")
if(sixth=='e'):
    f=1

#most repeated letter in the sentence is e(9 times)
#2nd most repeated letter in the sentence is t (8 times)

if(a and b and c and d and e and f):
    print("\n\n\t\tAuthentication Successful\n")
else:
    print("\n\n\t\tAuthentication Failed\n")
