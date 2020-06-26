n = [2,14,62,126,510]
m = []

def func(x):
    for i in x:
        i = i*2 + 2
        
        if i not in n:
            m.append(i)

    m.pop()
    
    print(min(m))
    print(m)
func(n)

# n = [4,9,3,15,17]
# m = list(range(min(n),max(n)+1))
# k =[]

# for i in m:
#     if i in n:
#         continue
#     else:
#         k.append(i)

# print(k)
# print(min(k))

# def func(x):
#     if x:
#         m = min(x)
#         x = max(x)
#         while m < x:
#             m+=1

#             if m not in n:
#                 k.append(m)
    
#         print(k[0])
#         print(k)

# func(n)


