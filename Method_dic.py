#Use the method values(): name of dictionary.values() : sẽ in ra các giá trị trong các items of dictionary.
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

#Use the method keys(): giống với methods values()
for s in spam.keys():
    print(s)

#Use the method items(): cả 2 cái trên cộng vô (nhưng kết quả return of items() là kiểu Tuple of keys() and values())
for k in spam.items():
    print(k)
#Use 2 variable to separate the keys and values:
for m,o in spam.items():
    print('Key: ' + m + ' Value: ' + str(o))

#Use list(dictionary) để convert the dictionary to true list:
print(list(spam))

#get() method: dùng để check xem có dữ liệu trong đó không. Nếu không có thì sẽ trả lại một giá trị dự phòng (fallback value)
#syntax: get('the keys to retrieve',fallback value)
picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs') #eggs không tồn tại trong picnicitems dictionary
#do đó giá trị dự phòng là 0 sẽ được in ra.
#Without using get() method can make KeyError.

#setdefault() method: 
#Syntax: setdefault('the keys to check exist or not',the value will to assign if this key do not exist in dictionary)
spam1 = {'name': 'Pooka', 'age': 5}
spam1.setdefault('color', 'black') #check keys: 'color" nếu không có thì tự động gán giá trị black cho 'color'
                                   #Đồng thời tự động insert to the spam1 dictionary
print (spam1.setdefault('color', 'black')) # nếu in cả cái câu lệnh này ra thì sẽ trả về là  black
print (spam1)

spam1.setdefault('color','White') # nếu cố dùng lại setdefault một lần nữa thì sẽ không có gì thay đổi
                                  # Bởi vì the key color đã tồn tại
