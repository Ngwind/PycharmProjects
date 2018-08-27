sql = "insert into o_exchange_billing " \
    "(status,notice_status,client_id,suid,user_name,billing_created,exchange_money,billing_no) values "

suid = "13747668411"  # suid
user_name = suid + "666"  # user_name
billing_created = ''  # 订单创建时间
exchange_money = "6"  # 交易金额
times = 50  # 订单数目
for i in range(times):
    if i == times-1:
        billing_no = suid + str(i)
        sub_sql = "(1,1,1383532238264530," + suid + "," + user_name + ",'2018-08-15 09:33:33'," + exchange_money+"," + billing_no + ");"
        print(sub_sql)
        sql = sql + sub_sql
    else:
        billing_no = suid + str(i)
        sub_sql = "(1,1,'1383532238264530'," + suid + ",'" + user_name + "','2018-08-15 09:33:33'," + exchange_money+","+billing_no + "),"
        print(sub_sql)
        sql = sql+sub_sql

print(sql)
