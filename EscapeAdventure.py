import random
"finale"

class pocket(object):
    def __init__(self):
        self.invlist = []
    def __iter__(self):
        return iter(self.invlist)
    def __del__(self):
        pass
    def addtoinvt(self, item):
        for each in item:
            self.invlist.extend([each])
    def __str__(self):
        return "{0}".format(self.invlist)
    def empty(self):
        self.invlist = []

class Hero(object):

    def __init__(self):
        self.pocket = pocket()

    def get(self, thing):
        itmlist = thing.invlist
        self.pocket.addtoinvt(itmlist)
        print("You got {0} try using it on the ceiling window".format(itmlist))
        thing.empty()

class Box(object):
    possible_contents = ['Screwdriver', 'Dirty Sock', 'Dopefish', 'basketball']
    def __init__(self):
        self.box_pocket = pocket()
    def __str__(self):
        return "{0}".format(self.box_pocket)
    def __del__(self):
        pass
    def add_contents(self):
        random_item = [random.choice(Box.possible_contents)]
        self.box_pocket.addtoinvt(random_item)

class decisionmaker(object):

    def __init__(self, stageinfo):
        self.info = stageinfo
    def receive_input(self):
        options = self.info.options
        choice = None
        bad_input_message = 0
        while choice not in range(1, (len(self.info.options) + 1)):
            if bad_input_message == 1:
                print("Thats not an option traveler try again.")
            for each in options:
                list_index = options.index(each) + 1
                print("{0}. {1}".format(list_index, each))
            choice = input("Make a decision: ")
            bad_input_message = 1
            if choice.isdigit():
                choice = int(choice)
            else:
                pass
            
        return choice

class Area(object):
    def __init__(self):
        self.optionchoice = decisionmaker(self)
        self.gme = 0
    def print_scene(self):
        if self.gme == 0:
            print(self.__str__())

class Shack(Area):

  def __init__(self):
        super(Shack, self).__init__()      
        self.shack_box = Box()
        self.options = [
            "Go up the stepladder",  
            "Go into the hole",
            "Look in the box",
            ]

  def __str__(self):
    self.gme = 1
    return (
        """
    On a dark and dreary night in the realm of testudoland you, young and weary traveler, have found yourself running to what looks like an abandoned shack.                                                                                                                                                                                  
       
    First you scout the area to check for critters and after you deem it safe you choose to hide there for the night.                                                                                                                                                                                                                         
    
    Entering the shack you hear the door slam behind you.                                                                                                                                                                                                                                                                                                                                                                                                                     
        
    You run back to the door to try and pry it open but alas, you are trapped. 
    
    A voice plays over what seems to be hidden speakers                                                                                                                                                                                                           
        
    "AHEM!!...IS THIS THING ON? agh I hope this is on because I know im not getting a refund on these speakers...any way it seems you are trapped young traveler AND WILL BE FORCED TO...um...DO MY INST326  HOMEWORK AHAHAHAHAHAHHAHAHAHAHHAAAAAAAAAA"                                                                                                                                                                                                                                                                                                                                                                                                                                 
        
    OH NO WHAT A TERRIBLE FATE HAS BEFALLEN YOU. It seems you have but one choice and that is to escape so you look around and see a hole in the ground, a stepladder that can   help you get to the roof window, and a wooden box.                                                                                                                                                                                                                                                                     
        
    You need to choose quick before he sends you the first html file!!!:""") 

  def run(self):
    self.shack_box.add_contents()
    box_inven = self.shack_box.box_pocket
    while True:
        pick = self.optionchoice.receive_input()
        if pick == 1:
            box_inven.empty()
            return 'stepladder'
        elif pick == 2:
            box_inven.empty()
            print("You fall in and hit your head...a bit later you wake up in the first room again...huh.")
            return 'shack'
        elif pick == 3:
            if box_inven.invlist != []:
                Character.get(box_inven)
            else:
                print("There's nothing in")


class Celingwindow(Area):

    def __init__(self):
        super(Celingwindow, self).__init__()
        self.options = [
            "Try to open up the ceiling window",
            "Go back down stepladder",
            ]
    def __str__(self):
        self.gme = 1
        return (
            "You get the stepladder to climb up to the celing window, there is a rusty latch holding the window locked"
            )
    def run(self):
        victory = (
            "You use the screwdriver you found to pop open the latch and climb to the roof. "
            "once youre up there you hop off the shack roof and run into the forrest...you survive another day doing no mans homework"
            )
        while True:
            pick = self.optionchoice.receive_input()
            if pick == 1:
                if 'Screwdriver' in Character.pocket:
                    print(victory)
                    return 'end'
                else:
                    print("The latch wont budge you need something to wedge it out.")
            elif pick == 2:
                print("well you're back where you started time to look around some more.")
                return 'shack'


class Game(object):
    def __init__(self):
        self.status = 'shack'
        self.start = Shack()
        self.escape = Celingwindow()
    def play(self):
        while self.status != 'end':
            if self.status == 'shack':
                self.start.print_scene()
                self.status = self.start.run()
            elif self.status == 'stepladder':
                self.escape.print_scene()
                self.status = self.escape.run()
        raise SystemExit

Character = Hero()
gamestart = Game()
gamestart.play()