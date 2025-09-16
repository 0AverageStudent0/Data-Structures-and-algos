# def func_to_find(word):
#     with open ("practice.text","r") as file:
#         data = file.read()
#         if(data.find(word) != -1):
#             print("found")
#         else:
#             print("not found")

# func_to_find("java")

# def func_to_line(word):
#     data = True
#     line_value =1
#     with open ("practice.text","r") as file:
#         while data:
#             data = file.readline()
#             if (word in data):
#                 print("found in line : ",line_value)
#                 return
#             line_value += 1
#     return print(-1)
   
# func_to_line("xlearning")
count  = 0
with open("practice.text","r") as f:
    data = f.read()
    list = data.split(",")
    for i in list:
        if ( int(i) % 2 == 0):
            count+=1

print(count)