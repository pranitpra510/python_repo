# import random

# input=random.randint(0,1)
# if input == 1 :

#     print("Heads",input)
# elif  input ==0:
#     print("Tails",input)
# else:
#     print("Enter valid number",input)        

# for i in range(10,-1,-1):
#     print(i)

data=[
    {
        "left":{
            "swim":"Gamover",
            "wait":{
                "red":"Gamover",
                "yellow":"You win",
                "blue":"Gamover"
            }
        },
        "right":"Game over"
    }]
user_input=input("Enter direction:")
if data[0][user_input] == 'right' :
    print(data[0][user_input])

elif data[0][user_input] == 'left':
        print()   