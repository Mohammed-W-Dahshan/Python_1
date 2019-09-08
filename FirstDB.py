from db_operations import Students
import sqlite3

s1 = Students()
res = s1.insert_std('alla','alla',22,'alla@gmail.com')
# rows = s1.get_all_std()
# for i in rows:
#     print(i)
# res = s1.update_attr(1,'age',21)
# print(res)
# s1.delete_std(6)


rows = s1.get_all_std()
for i in rows:
    print(i)
