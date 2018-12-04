class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and
destroyed your entire crew. You are the last surviving
member and your last mission is to get the neutron destruct
bomb from the Weapons Armory, put it in the bridge, and
blow the ship up after getting into an escape pod.
You're running down the central corridor to the Weapons
Armory when a Gothon jumps out, red scaly skin, dark grimy
teeth, and evil clown costume flowing around his hate
filled body. He's blocking the door to the Armory and
about to pull a weapon to blast you.
""")


laser_weapon_armory = Room("Laser Weapon Armory",
"""
If you get the code wrong 10 times then
the lock closes forever and you can't get the bomb. The
code is 3 digits.
""")


the_bridge = Room("The Bridge",
"""
You burst into bridge and surprise 5 Gothons who are
trying to take control of the ship.
""")


escape_pod = Room("Escape pod", "There's 5 pod, which one do you take?")


the_end_winner = Room("The End", "You jump into pod 2.You Won!")


the_end_loser = Room("The End", "You jump into a random pod.the pod explodes.")

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

generic_death = Room("death", "You died.")

the_bridge.add_paths({
    'throw the bomb': generic_death,
    'slowly place the bomb':escape_pod
})

laser_weapon_armory.add_paths({
    '0132': the_bridge,
    '*': generic_death
})

central_corridor.add_paths({
    'shoot!': generic_death,
    'dodge!': generic_death,
    'tell a joke': laser_weapon_armory
})

START = 'central_corridor'

def load_room(name):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(name)

def name_room(room):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this global lookup?
    """
    for key, value in globals().items():
        if value == room:
            return key
