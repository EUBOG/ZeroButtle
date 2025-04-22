class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"Герой по имени {self.name} атакует героя по имени {other.name} и наносит урон уровня {self.attack_power}!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра начинается!")
        current_turn = 0  # 0 - игрок, 1 - компьютер

        while self.player.is_alive() and self.computer.is_alive():
            if current_turn == 0:
                self.player.attack(self.computer)
                print(f"У героя по имени {self.computer.name} осталось здоровья на уровне {self.computer.health}.")
            else:
                self.computer.attack(self.player)
                print(f"У героя по имени {self.player.name} осталось здоровья на уровне {self.player.health}.")
            current_turn = 1 - current_turn  # Меняем ход

        winner = self.player if self.player.is_alive() else self.computer
        print(f"Герой по имени {winner.name} побеждает!")


if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    game = Game(player_name)
    game.start()