## Задача 9. Протокол соревнований
Вы продолжаете развиваться в геймдеве и в этот раз вам пришло действительно внушительное техническое задание, с описанием правил игр, входными и выходными данными. Вот как оно выглядит:

Здравствуйте! Мы собираемся устраивать соревнования по [данные засекречены] и хотим, чтобы вы написали эффективную программу, которая составляла бы нам протокол и определяла победителя и призёров. О логике работы программы ниже.

**_Правила соревнований:_**
1. Участники имеют право играть несколько раз. Количество попыток одного участника не ограничивается. 
2. Окончательный результат участника определяется по одной игре, лучшей для данного участника.
3. Более высокое место в соревнованиях занимает участник, показавший лучший результат.
4. При равенстве результатов более высокое место занимает участник, раньше показавший лучший результат.

**_Как проходят соревнования:_**

В ходе соревнований заполняется протокол, каждая строка которого описывает одну игру и содержит результат участника и его игровое имя. Протокол формируется в реальном времени по ходу проведения чемпионата, поэтому строки в нём расположены в порядке проведения игр: чем раньше встречается строка в протоколе, тем раньше закончилась соответствующая этой строке игра.

Напишите программу, которая по данным протокола определяет победителя и призёров. Гарантируется, что в чемпионате участвует не менее трёх игроков.

**_Описание входных данных_**

Первая строка содержит число N - это общее количество строк протокола. Каждая из следующих N строк содержит записанные через пробел результат участника (целое неотрицательное число) и игровое имя (имя не может содержать пробелов). Строки исходных данных соответствуют строкам протокола и расположены в том же порядке, что и в протоколе.
Гарантируется, что количество участников соревнований не менее 3.

**_Описание выходных данных_**

Программа должна вывести имена и результаты трёх лучших игроков по форме, приведённой ниже в примере.


#### Пример входных и выходных данных:
```
Сколько записей вносится в протокол? 9
Записи (результат и имя):
1 запись: 69485 Jack 
2 запись: 95715 qwerty 
3 запись: 95715 Alex 
4 запись: 83647 M
5 запись: 197128 qwerty 
6 запись: 95715 Jack 
7 запись: 93289 Alex 
8 запись: 95715 Alex 
9 запись: 95715 M

Итоги соревнований:
1 место. qwerty (197128)
2 место. Alex (95715)
3 место. Jack (95715)
```
