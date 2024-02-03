#создается функция аргументом 'images' / The function is created with the argument 'images'
def image_info(images):
    #пишется условие при котором будет выводится ошибка./
    #writes the condition under which the error will be displayed.
    if 'image_id' not in images or 'image_title' not in images:

        # используется конструткор raise для создания
        #ошибки типа TypeError./ uses the raise constructor to create an error of the TypeError type.
        raise TypeError(f"image_title or image_id must be present.")
    #возвращает строку ссылаясь на аргумент images
    #поскольку аргумент images пуст в него необходимо поместить ключь и значение./
    #returns a string referring to the images argument since the images argument is empty,
    #a key and a value must be placed in it.
    return f"Image '{images['image_title']}' has ID-{images['image_id']}."


#происходит обработка ошибки в случии несоответсвия с условием заданном в функции.
#an error is processed in case of inconsistency with the condition specified in the function.

#обработка происходит с помощью конструкции try/except
#processing is performed using the try/except construct

#вывод ошибки помещается в переменную 'e'
#the error output is placed in the 'e' variable

#перменная с выводом ошиьки выводится в терминал в случаи возникновения ошибки.
#variable with error output is output to the terminal in case of an error.
try:
    print(image_info({'image_title':'my cat', 'image_id': 123})) # в терминал выводится значение функции с аргументами.
except TypeError as e:
    print(e)