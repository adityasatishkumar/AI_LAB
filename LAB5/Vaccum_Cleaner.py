def check(stack):
    if stack[-1]=="right" or stack[-1]=="left":
        if stack[-2]=="left" or stack[-2]=="right" :
            return False
stack=[]
flag=True
count=1
while flag:
    perc=input("Enter the percept: ")
    loc =input("Enter the location: ")
    if loc=="A":
        if perc=="dirty":
            print("Action: suck...turn right\n")
            stack.append("suck")
            stack.append("right")  
        else:
            print("Action: turn right\n")
            stack.append("right")
    else:
        if perc=="dirty":
            print("Action: suck.....turn left\n")
            stack.append("suck")
            stack.append("left")
        else:
            print("Action: turn left\n")
            stack.append("left")
    count=count+1
    if count>2:
        flag=check(stack)
print("Both A and B are Clean!!")