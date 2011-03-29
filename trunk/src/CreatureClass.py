# External imports
import libtcodpy as libtcod


class Creature:
    #combat-related properties and methods (monster, player, NPC).
    def __init__(self, hp, stats = (10, 10, 10), alignment =
    Alignment("N"), energy = 100, move_cost = 100, attack_cost = 100, ai =
    NormalMonster(), inventory = None, death_function=None):
        self.death_function = death_function
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def heal(self, amount):
        #heal by the given amount, without going over the maximum
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def take_damage(self, damage):
        #apply damage if possible
        if damage > 0:
            self.hp -= damage
            #check for death. if there's a death function, call it
            if self.hp <= 0:
                function = self.death_function
                if function is not None:
                    function(self.owner)


    def attack(self, target):
        #a simple formula for attack damage
        damage = self.power - target.fighter.defense
 
        if damage > 0:
            #make the target take some damage
            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' for ' + str(damage) + ' hit points.')
            target.fighter.take_damage(damage)
        else:
            message(self.owner.name.capitalize() + ' attacks ' + target.name + ' but it has no effect!')


class ConfusedMonster:
    #AI for a temporarily confused monster (reverts to previous AI
    #after a while).
    def __init__(self, old_ai, num_turns=CONFUSE_NUM_TURNS):
        self.old_ai = old_ai
        self.num_turns = num_turns
 
    def take_turn(self):
        if self.num_turns > 0:  #still confused...
            
            #move in a random direction, and decrease the number of
            #turns confused
            self.owner.move(libtcod.random_get_int(0, -1, 1), 
                            libtcod.random_get_int(0, -1, 1))
            self.num_turns -= 1
 
        else:  

            #restore the previous AI (this one will be deleted because
            #it's not referenced anymore)
            self.owner.ai = self.old_ai
            message('The ' + self.owner.name + ' is no longer confused!', 
                    libtcod.red)


# Normal Monster class
class NormalMonster:
    #AI for a basic monster.
    def take_turn(self):
        #a basic monster takes its turn. If you can see it, it can see you
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
 
            #move towards player if far away
            if monster.distance_to(player) >= 2:
                monster.move_towards(player.x, player.y)
 
            #close enough, attack! (if the player is still alive.)
            elif player.fighter.hp > 0:
                monster.fighter.attack(player)
