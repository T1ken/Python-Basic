import random


random.seed()


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4
        self.score = 0
        self.bot_score = 0

    def print_card(self, current, score, bot):
        if not bot:
            print(f'Вам попалась карта {current}. У вас {score} очков.')
        else:
            print(f'Крупье попалась карта {current}. У крупье {score} очков')

    def random_card(self, score, bot):
        current = self.deck.pop()
        if type(current) is int:
            score += current
        elif current == 'Туз':
            if score <= 10:
                score += 11
            else:
                score += 1
        else:
            score += 10
        self.print_card(current, score, bot)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        bot_score = self.random_card(self.bot_score, True)
        while True:
            choice = input('Будете брать карту? да/нет ').lower()
            if choice == 'да':
                score = self.random_card(score, False)
                if bot_score < 19 and score <= 21:
                    bot_score = self.random_card(bot_score, True)
                if score == 21 or bot_score == 21:
                    print('Вы проиграли, вы должны нам почку')
                    break
                elif score == 21 and bot_score == 21:
                    print('ничья, оба лохи')
                elif score == 21 or bot_score >= 21:
                    print('Вы победили! Поздравляю, ваш приз АВТОМОБИЛЬ "звуки Якубовича"')
                    break
            elif choice == 'нет':
                if score > bot_score and bot_score < 19:
                    while bot_score < 19:
                        bot_score = self.random_card(bot_score, True)
                if score < bot_score <= 21:
                    print(f'Вы проиграли, у вас {score} очков, у крупье {bot_score} очков')
                else:
                    print(f'Вы победили, у вас {score} очков, у крупье {bot_score} очков')
                break

    def start(self):
        random.shuffle(self.deck)
        self.choice()


game = BlackJack()
game.start()
