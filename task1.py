# def season(x):
#     winter = [12, 1, 2]
#     spring = [3, 4, 5] 
#     summer = [6, 7, 8]
#     fall = [9, 10, 11]

#     if x in winter:
#         winter = "winter"
#         return winter
#     elif x in spring: 
#         spring = "spring"
#         return spring
#     elif x in summer:
#         summer = "summer"
#         return summer  
#     elif x in fall:
#         fall = "fall"
#         return fall

# n = season(5)
# print(n)

def season(x):
     winter = [12, 1, 2]
     spring = [3, 4, 5] 
     summer = [6, 7, 8]
     fall = [9, 10, 11]

     if x in winter:
         winter = "winter"
         print(winter)
     elif x in spring: 
         spring = "spring"
         print(spring)
     elif x in summer:
         summer = "summer"
         print(summer)
     elif x in fall:
         fall = "fall"
         print(fall)

season(int(input("Type the month rate: ")))

