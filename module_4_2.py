def test_function(): #функция по условию
    def inner_function(): #функция по условию
        print("Я в области видимости test_function") #вывод на экран по условию
    inner_function() #вызов фунеции
test_function() #вызов функции
inner_function() #будет ошибка, так как функция находится вне зоны видимости 