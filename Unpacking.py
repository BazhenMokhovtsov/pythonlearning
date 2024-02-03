#создать список словарей с 3мя словорями
#с помощью оператора распаковки списков создать 3 переменных каждая из которых будет содержать один из словарей.
#создать функцию которая будет принимать 2 аргумента
#в вызове функции должен распоковываться словарь
#вызвать функцию три раза
#

dict_list = [{
    'Brand': 'BMW',
    'Price': '25_999'
},
    {
    'Fruit': 'apple',
    'Another_fruit': 'banana'
},
    {
        'Name': 'Bazhen',
        'residences': 'Germany'
    }]

Auto_brand, Fruits, Person = dict_list

#def my_fn(key, value):
#    return f"argument one is {key}, argument two is {value}"

print(Auto_brand)

