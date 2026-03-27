# logic 1st
def checkEquation(str):
    s=[]
    for i in str:
        if(i=='{' or i=='(' or i=='['):
            s.append(i)
        else :
            if(len(s)==0):
                return False
            elif(i=="}" and s[-1]!="{"):
                return False
            elif(i=="]" and s[-1]!="["):
                return False
            elif(i==")" and s[-1]!="("):
                return False
            else :
                s.pop()
    return len(s)==0                 
         



eq="{}{[(())]}"
print('result :',checkEquation(eq))        

#------------ logic 2nd-------------------------------

# def checkEquation(str):
#     s=[]
#     for i in str:
#         if(i=='{' or i=='(' or i=='['):
#             s.append(i)
#         else :
#             if(len(s)==0):
#                 return False
#             elif(i=="}" and s[-1]=="{"):
#                 s.pop()
#             elif(i=="]" and s[-1]=="["):
#                 s.pop()
#             elif(i==")" and s[-1]=="("):
#                 s.pop()
#             else :
#                 return False
#     return len(s)==0                 
         



# eq="{}{[(())]}"
# print('result :',checkEquation(eq))      