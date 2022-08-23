def eligible(user):
    if user>=18:
        print("you are eligible for vote")
    else:
        print("you are not eligible for vote")
user=int(input("enter the number:"))
eligible(user)