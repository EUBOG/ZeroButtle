# ZeroButtle
ZeroButtle - учебный проект
Общее описание:
Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
Требования:
1.Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
2.Игра должна быть реализована как консольное приложение.
Классы:
Класс Hero:
•Атрибуты:
•Имя (name)
•Здоровье (health), начальное значение 100
•Сила удара (attack_power), начальное значение 20
•Методы:
•attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
•is_alive(): возвращает True, если здоровье героя больше 0, иначе False
Класс Game:
•Атрибуты:
•Игрок (player), экземпляр класса Hero
•Компьютер (computer), экземпляр класса Hero
•Методы:
•start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.
