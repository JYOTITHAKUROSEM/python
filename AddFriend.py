friend_name=[]
friend_age=[]
friend_rating=[]
friend_is_online=[]
def add1_friend():
    new_name=raw_input("please add your friend name:")
    new_saluatation=raw_input("are they mr.or ms.? ")
    new_name=new_name+" "+new_saluatation
    new_age=raw_input("age")
    new_rating=raw_input("spy_rating")
    new_age=int(new_age)
    new_rating=float(new_rating)
    if len(new_name)>0 and  new_age>12:
        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_rating.append(new_rating)
        print("Your friend is added successfully......")
    else:
        print "sorry!Invalid entry.we can/'t add spy with the details you provided"
    return len(friend_name)

