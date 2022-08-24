#words = ["anggur","apel","jeruk"]
#for i in words:
    #print(i)

users = {'qila': 'active', 'fuji': 'inactive', 'ala': 'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user]= status

print(users)
print(active_users)