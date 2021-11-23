d = {}
print(d)
d.setdefault('name',input('enter name to register :'))
d.setdefault('pasword',input('enter password to register :'))
print(d)
print('register successfully')
print('login')
user_name = input('enter username :')
password = input('eneter password :')
if d.get('name')==user_name and d.get('pasword')==password:
      print('get in')
else: print('get out')
'''
user_name = input('enter ur name :')
password = input('eneter ur pasword : ') 
if user_name == d.get(name):
    if password == d.get(password):
        print('successfully login')
else:
    print('login is not successfull')
'''
