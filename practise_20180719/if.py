print("hello world!".center(50, "="))
user_id = input("inter the id,please!\n")
user_pwd = input("inter the password,please!\n")
if user_id == "xiaoming" and user_pwd == "123456":
    print("welcome!  {}\n".format(user_id))
else:
    print("error!\n")


