from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power

    def run(self):
        warriors = 100
        days = 0
        print(f'{self.name}, на нас напали!' + '\n')
        for i in range(warriors):
            if warriors > 0:
                warriors -= self.power
                days += 1
                sleep(1)
                print(f'{self.name} сражается {days} день(дня)..., осталось {warriors} воинов.' + '\n')
                if warriors == 0:
                    print(f'{self.name} одержал победу спустя {days} дней(дня)' + '\n')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
