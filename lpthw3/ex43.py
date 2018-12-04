from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() # 将第一个场景对象赋值给current_scene
        last_scene = self.scene_map.next_scene('finished') # 定义结束场景

        while current_scene != last_scene: # 通过结束场景后循环结束
            next_scene_name = current_scene.enter() # 进入场景，并将通过流程后返回的场景名称字符串赋值给next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name) #通过传入参数将对应的场景对象赋值给current_scene

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better au this."
        "You're worse that your Dad's jokes."
    ]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
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
            """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon. His clown costume is flowing and
                moving around his body, which throws off your aim.
                Then he eats you.
                """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                The Goyhon eats you.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                While he is laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            If you get the code wrong 10 times then
            the lock closes forever and you can't get the bomb. The
            code is 3 digits.
            """))


        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code or guess == 'kaka':
            print(dedent("""
                You get the neutron bomb, and you must put it
                in right place.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                You die.
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst into bridge and surprise 5 Gothons who are
            trying to take control of the ship.
            """))

        action = input("> ")

        if action == "throw the bomb":
            print("A Gothon shoot you. You die.")
            return 'death'

        elif action == "slowly place the bomb":
            print("The bomb is placed. You should begin to run.")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'bridge'


class EscapePod(Scene):

    def enter(self):
        print("There's 5 pod, which one do you take?")

        good_pod = randint(1,5)
        print(good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod {guess}.the pod explodes.")
            return 'death'
        else:
            print("You won!")
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name) # 创景该场景对应的1个实例val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
