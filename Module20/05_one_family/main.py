family_dict = {
    ('Сидоров', 'Никита'): 35,
    ('Сидорова', 'Алина'): 34,
    ('Сидоров', 'Павел'): 10,
    ('Иванов', 'Максим'): 45,
    ('Иванова', 'Мария'): 41
}
surname = input("Введите фамилию: ").lower()
surname_man = ''
if surname[-1] == 'а':
    surname_man = surname[:-1]
surname_woman = surname + 'а'
for i_name, i_age in family_dict.items():
    if i_name[0].lower() == surname.lower() or i_name[0].lower() == surname_man.lower() or i_name[0].lower() == surname_woman:
        print(i_name[0], i_name[1], i_age)
# ты мне пытался объяснить, я не понял как это делать
# Я щас чекнул как я делал задание, и тут в бд имена храняться не в формате строки, а кортежа с разделёнными именем и
# фамилией. Это должно облегчить работу.
# Я неправильно понял твое объяснение, я думал, что имя запрашивается, если так, то задание изи
# зачтено
# слава богу, я думал, что неправильно сделал
