# Primary file for Basic Initiative Tracker.

# Defines the various combatants for use
class Participant:
    def __init__(self, name, initiative):
        self.name = name
        self.initiative = initiative
class InitiativeTracker:
    # Initializes an empty list of participants, sets the current participant index to 0, and starts at round 1.
    def __init__(self):
        self.participants = []
        self.current_participant_index = 0
        self.round_number = 1
    # Adds a new participant to the list, then sorts them by initiative.
    def add_participant(self, name, initiative):
        participant = Participant(name, initiative)
        self.participants.append(participant)
        self.sort_participants()
    # Sorts participants by initiative in descending order.
    def sort_participants(self):
        self.participants.sort(key=lambda x: x.initiative, reverse=True)
    # Advances to the next participant. If it reaches the end of the list, it increments the round number.
    def next_turn(self):
        self.current_participant_index = (self.current_participant_index + 1) % len(self.participants)
        if self.current_participant_index == 0:
            self.round_number += 1
    # Returns the current participant object.
    def get_current_participant(self):
        if self.participants:
            return self.participants[self.current_participant_index]
        return None
    # Prints the current round and participants in initiative order, highlighting the current participant.
    def display_tracker(self):
        print(f"--- Round {self.round_number} ---")
        for i, participant in enumerate(self.participants):
            prefix = "--> " if i == self.current_participant_index else "    "
            print(f"{prefix}{participant.name}: {participant.initiative}")

# Primary function
def main():
    tracker = InitiativeTracker()
    tracker.add_participant("Goblin King", 16)
    tracker.add_participant("Goblin 1", 3)
    tracker.add_participant("Goblin 2", 7)
    tracker.add_participant("Goblin 3", 9)
    tracker.add_participant("Goblin 4", 1)
    tracker.add_participant("Conan, the Librarian!", 42)
    tracker.add_participant("Gabriella of Edgemoor", 17)
    tracker.add_participant("Griswold the Evoker", 12)
    tracker.add_participant("Bob", 4)
    while True:
        tracker.display_tracker()
        input("Press Enter for next turn...")
        tracker.next_turn()
if __name__ == "__main__":
    main()