def hello():
    print(f"Welcome to the world of Python!")

def pack(a, b, c):
   return [ a, b, c ]

def eat_lunch(any_list):

    print(f"First I eat {any_list[0]}")

    for i in range (1, len(any_list)+1):
      
        if i == len(any_list):
            print(f"My lunchbox is empty")
        else:
            print(f"Next I eat {any_list[i]}")



hello()

print(pack('amy','bob','sue'))

lunch_list1 = ['salad', 'soup', 'pizza', 'pudding']
lunch_list2 = [ 'sushi', 'eggroll', 'tofu', 'peking duck', 'fried rice']

eat_lunch(lunch_list1)

eat_lunch(lunch_list2)

eat_lunch(['bread', 'croissant', 'baguette', 'brioche'])
