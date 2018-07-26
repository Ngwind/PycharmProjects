t_id = "wwd"  #帐号
t_pwd = "123456" #密码
login_error = 0 # 密码错误次数

print("Hello login".center(50, "="))
while True:
        u_id = input("Enter your id:")
        u_pwd = input("Enter your password:")

        if u_id == t_id:
            if login_error < 3:
                if u_pwd == t_pwd:
                    print("Welcome {}".format(t_id).center(50, "="))
                    break
                else:
                    login_error += 1
                    print("password error :", login_error, "times\n")
            else:
                print("you have enter error password over", login_error, "times,so you id is locked\n")
        else:
            print("the id not real!\n")
