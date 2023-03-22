def hello():
    print(f"Welcome to the world of Python!")

def pack(a, b, c):
   return [ a, b, c ]

#read instruction incorrect. Assume when everthing is eaten from the lunchbox a declaration of " My lunch box is empty"
def eat_lunch(any_list):
    print(f"First I eat {any_list[0]}")
    for i in range (1, len(any_list)+1):
        if i == len(any_list):
            print(f"My lunchbox is empty")
        else:
            print(f"Next I eat {any_list[i]}")

# corrected code to eat_lunch
def l_lunch(lunch):
   if len(lunch)==0:
        print("My lunchbox is empty!")
   else:
    for i in range (len(lunch)):
        if i== 0:
            print(f"First I eat {lunch[i]}") 
        else:  
            print(f"Next I eat {lunch[i]}")
            

# solution
def my_lunch(my_lst):
  if len(my_lst) == 0:
    print("My lunchbox is empty!")
  else:
    for i in range(len(my_lst)):
      if i == 0:
        print(f"First I eat {my_lst[0]}")
      else:
        print(f"Next I eat {my_lst[i]}")

    

      





hello()

# print(pack('amy','bob','sue'))

# lunch_list1 = ['salad', 'soup', 'pizza', 'pudding']
lunch_list2 = [ 'sushi', 'eggroll', 'tofu', 'peking duck', 'fried rice']

# eat_lunch(lunch_list1)

# my_lunch(lunch_list2)



l_lunch(['bread', 'croissant', 'baguette', 'brioche'])




