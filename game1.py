from random import randrange
from random import choice
# Creating Mother's class to initialised the players
class Character:

    def __init__(self,name,life_points, damage):
        self.name = name
        self.life_points = life_points
        self.damage = damage

    def presentation(self):
        return self.name

    def init_life_points(self, life_points):
        self.life_points = life_points

    def make_damage(self):
        return self.damage
    # creating the attack
    def take_damage(self,damage):
        self.life_points -= damage
        if self.life_points <= 0:
            self.life_points = 0  # on met la valeur à zéro

    # Creating Warrior class: our hero for this game
class Warrior(Character):

    life_points = randrange(30, 50)
    damage = randrange(5, 10)

    def __init__(self,name,life_points, damage, weapon):
        super().__init__(name,life_points, damage)
        self.name = name
        self.weapon = weapon


    # Creating Archer's class. The bad guy is rude!
class Archer(Character):

    be_bad= ["You are just a little dropping!", "That's all you got!", "You punch like a girl!","You fight like my granny!", "Fight back, I am falling asleep"]
    def __init__(self, name, life_points , damage,be_bad):
        super().__init__(name, life_points, damage)
        self.life_points = life_points
        self.damage = damage
        self.be_bad = be_bad

# Initialised the Warrior
username = input(" Choose your Warrior name : ")
life_beginning = Warrior.life_points
sharp_weapon = Warrior.damage
the_weapon = "sword"
warrior1 = Warrior(username, life_beginning, sharp_weapon, the_weapon)
print("Hello", username," you have got", sharp_weapon , " damage values, and", life_beginning ,"points of life. Your", the_weapon, "will help you to kill Archers! Fight well!")

# Initialised the Archer one
archer1_name = "The Rock"
life_beginning1 = randrange(30,50)
archer1_damage = randrange(5,10)
archer1_rudness = choice(Archer.be_bad)
archer1 = Archer(archer1_name, life_beginning1,archer1_damage,archer1_rudness)
print("The Archer named :", archer1_name, ". He has got ", archer1_damage, "damage values and", life_beginning1,"points of life. He is aggressif and can insult you like this :",archer1_rudness,"! Be ready and don't enter his game!!")

# Initialised the Archer two
archer2_name = "The Cutman"
life_beginning2 = randrange(30,50)
archer2_damage = randrange(5,10)
archer2_rudness = choice(Archer.be_bad)
archer2 = Archer(archer2_name, life_beginning2,archer2_damage,archer2_rudness)
print("The Archer named :", archer2_name, ". He has got ", archer2_damage, "damage values and", life_beginning2,"points of life. He is aggressif and can insult you like this :",archer2_rudness,"! Be ready and don't enter his game!!")


dead = 0
# I start my game in a "while" loop:
while warrior1.life_points > dead and (archer1.life_points > dead and archer2.life_points > dead):
    # First if my hero attack
    if warrior1.life_points >= dead:
        warrior1.take_damage(archer1.make_damage())
        print("Good job {}! Your sword is sharp! {} received {} damage value. He has {} points of life left!".format(
            username, archer1_name, archer1.damage, archer1.life_points))
        warrior1.take_damage(archer2.make_damage())
        print("Good job {}! Your sword is sharp! {} received {} damage value. He has {} points of life left!".format(
            username, archer2.name, archer2.damage, archer2.life_points))

    # if my hero succees to kill one of the Archers
    elif archer1.life_points or archer2.life_points < dead:
        print("well done {} you killed one of them!!".format(username))

    # The Archers are fighting back
    if (archer1.life_points and archer2.life_points > dead):
        archer1.take_damage(warrior1.make_damage())
        archer2.take_damage(warrior1.make_damage())
        print(archer1.name, choice(Archer.be_bad))
        print(archer2.name, choice(Archer.be_bad))
        print("{}, You were under attack and you have got {} damage value. You have {} points of life left!!!".format(username, warrior1.damage, warrior1.life_points))

    # If my hero succeed to kill both from the Archer
    elif archer1.life_points < dead and archer2.life_points < dead:
        print("Congratulations {}, you won!! You are a super Warrior!. You finished the game!!".format(username))

# If my hero died
print("Aouch! You fight well {} but not well enough. You are dead! ---- GAME OVER !!!".format(username))
