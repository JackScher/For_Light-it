import random
import time



class Character:
    def __init__(self, name, sleep):
        """Creating a character"""
        self.name = name
        self.sleep = sleep
        self.HP = 100
        self.random_step = 0
        self.random_skill = 0
        self.damage = 0
        self.hill_health = 0


    def step(self):
        """Who will go next function"""
        self.random_step = random.randint(0, 1)
        return self.random_step


    def skill(self):
        """What skill will you use function"""
        self.random_skill = random.randint(0, 2)
        if self.random_skill == 0:
            self.damage = random.randint(18, 25)
            print("Low range damage =", self.damage)
            return ("damage", self.damage)
        elif self.random_skill == 1:
            self.damage = random.randint(10, 35)
            print("High range damage =", self.damage)
            return ("damage", self.damage)
        else:
            self.hill_health = random.randint(18, 25)
            print("Hill =", self.hill_health)
            return ("hill", self.hill_health)


    def low_hp_computer(self):
        """Computer`s better hill with low HP function"""
        self.random_skill = random.randint(0, 3)
        if self.random_skill == 0:
            self.damage = random.randint(18, 25)
            print("Low range damage =", self.damage)
            return ("damage", self.damage)
        elif self.random_skill == 1:
            self.damage = random.randint(10, 35)
            print("High range damage =", self.damage)
            return ("damage", self.damage)
        else:
            self.hill_health = random.randint(18, 25)
            print("Hill =", self.hill_health)
            return ("hill", self.hill_health)


    def hilling(self):
        """Hill your health function"""
        if self.HP < 100:
            self.HP += self.hill_health
            if self.HP > 100:
                self.HP = 100
        print("health =", self.HP, "\n")
        time.sleep(self.sleep)


    def dmg(self, damag):
        """Taken damage function"""
        self.HP -= damag
        if self.HP < 0:
            self.HP = 0
        print("health =", self.HP, "\n")
        time.sleep(self.sleep)


    def check_HP(self):
        """Function for checking HP"""
        return self.HP