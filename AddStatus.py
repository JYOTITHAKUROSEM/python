current_status_message = []
add_status=[]
default = str.lower(raw_input("Do you want to select from the older status (Y/N)?"))
if default == "y":
   my_list =["hey!'there i am using spy chat","Second Message"]
   for temp in my_list:
        print temp
else:
     new_status_message = raw_input("what status message do you want to set")
     if len(new_status_message) >0:
        current_status_meassge =new_status_message
        current_status_message.append(new_status_message)
        for message in current_status_message:
            print message

            choice=raw_input("y is old and n is new")
            if choice == "y":
                my_list = ["hey!'there i am using spy chat", "Second Message"]
                counter = 1
                for temp in my_list:
                    print ("%s%s") % (counter,temp)
                user_choice = raw_input("Select an Option")
                if choice == 1:
                 print my_list[0]
            else:
              print my_list[1]





