# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
comb=name1.lower() +name2.lower()
t=comb.count('t')
r=comb.count('r')
u=comb.count('u')
e=comb.count('e')
true=t+r+u+e
l=comb.count('l')
o=comb.count('o')
v=comb.count('v')
e=comb.count('e')
love=l+o+v+e
com_str=int(str(true)+str(love))
if com_str<10 or com_str>90:
    print(f"Your score is {com_str}, you go together like coke and mentos.")
elif 40<com_str<50:
    print(f"Your score is {com_str}, you are alright together.")
else:
    print(f"Your score is {com_str}.")


