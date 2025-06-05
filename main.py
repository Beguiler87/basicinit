# Primary file for Basic Initiative Tracker.
# Warrior class defines combatants: name, initiative, which side of combat they belong to.
class Warrior:
    def __init__(self, name, initiative, side):
        self.name = name
        self.initiative = initiative
        self.side = side
# Tracker class creates empty list of combatants, allies/enemies, sets current combatant to 0.
class Tracker:
    def __init__(self):
        self.warriors = []
        self.allies = []
        self.enemies = []
        self.current_warrior_index = 0
    # Adds combatants to lists, then sorts by initiative in descending order.
    def add_warrior(self, name, initiative, side):
        warrior = Warrior(name, initiative, side)
        self.warriors.append(warrior)
        if warrior.side == "enemy":
            self.enemies.append(warrior.name)
        else:
            self.allies.append(warrior.name)
        self.sort_warriors()
    # Initiative sorting
    def sort_warriors(self):
        self.warriors.sort(key=lambda x: x.initiative, reverse=True)
    # Displays combatants
    def order_list(self):
        for i, warrior in enumerate(self.warriors):
            print(f"{warrior.name} is an {warrior.side} with an initiative of {warrior.initiative}")
    # Displays current combatant's turn
    def get_current_warrior(self):
        if self.warriors:
            current = self.warriors[self.current_warrior_index]
            print(f"It is {current.name}'s turn.")
        return None
    # Advances to next turn.
    def next_turn(self):
        self.current_warrior_index = (self.current_warrior_index + 1) % len(self.warriors)
        self.get_current_warrior()
        return None
# Primary function
def main():
    tracker = Tracker()
    # Combatants
    tracker.add_warrior("Goblin King", 16, "enemy")
    tracker.add_warrior("Goblin 1", 3, "enemy")
    tracker.add_warrior("Goblin 2", 7, "enemy")
    tracker.add_warrior("Goblin 3", 9, "enemy")
    tracker.add_warrior("Goblin 4", 1, "enemy")
    tracker.add_warrior("Goblin 5", 6, "enemy")
    tracker.add_warrior("Ogre", 2, "enemy")
    tracker.add_warrior("Conan, the Librarian!", 23, "ally")
    tracker.add_warrior("Gabriella of Edgemoore", 17, "ally")
    tracker.add_warrior("Griswold the Evoker", 12, "ally")
    tracker.add_warrior("Bob the cleric", 4, "ally")
    tracker.add_warrior("Possum the Trollslayer, a Kobold of Means", 18, "ally")
    # Prints the initiative order and the first combatant in the initiative.
    print("Welcome to combat. Initiative has been rolled.")
    tracker.order_list()
    tracker.get_current_warrior()
    # Handles initiative actions and conditions.
    while True:
        user_input = input("Press Enter to advance the turn, or type 'slain' to remove a combatant.")
        if not tracker.warriors:
            print("There are no combatants. Combat has ceased.")
            break
        if user_input == "slain":
            slain = tracker.warriors[tracker.current_warrior_index]
            print(f"{slain.name} has been slain!")
            del tracker.warriors[tracker.current_warrior_index]
            if tracker.warriors:
                tracker.current_warrior_index %= len(tracker.warriors)
                tracker.next_turn()
        else:
            tracker.next_turn()



if __name__ == "__main__":
    main()