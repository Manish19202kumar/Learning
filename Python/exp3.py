user_details={}
user_id=input("Enter user ID:")
user_name=input("Enter user name:")
user_age=input("Enter user age:")

user_details[user_id]={"Name":user_name,"Age":user_age}
search_id=input("Enter ID to retrieve details:")
if search_id in user_details:
    details=user_details[search_id]
    print (F"user ID:{search_id}")
    print(F"name: {details['name']}")
    print(F"Age: {details['age']}")
else:
    print("user ID not found")