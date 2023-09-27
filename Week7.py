#Taner Fitchue
# Week 7
# 9/27/23

class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

class Scoreboard:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_score(self, name, score):
        new_node = Node(name, score)
        if not self.head or score >= self.head.score:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and score < current.next.score:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1
        if self.size > 10:
            self.delete_last()

    def delete_score(self, name):
        if not self.head:
            print("Scoreboard is empty.")
            return
        if self.head.name == name:
            self.head = self.head.next
            self.size -= 1
            print(f"{name}'s score has been deleted.")
            return
        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                self.size -= 1
                print(f"{name}'s score has been deleted.")
                return
            current = current.next
        print(f"No player with the name {name} found.")

    def delete_last(self):
        if not self.head:
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
        self.size -= 1

    def print_scores(self):
        if not self.head:
            print("Scoreboard is empty.")
        else:
            print("Top 10 Scores:")
            current = self.head
            position = 1
            while current and position <= 10:
                print(f"{position}. {current.name}: {current.score}")
                current = current.next
                position += 1

def main():
    scoreboard = Scoreboard()
    while True:
        print("\nMenu:")
        print("1. Add a new player score")
        print("2. Delete a player/score node")
        print("3. Print the list")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter player name: ")
            score = int(input("Enter player score: "))
            scoreboard.add_score(name, score)
        elif choice == "2":
            name = input("Enter the name of the player to delete: ")
            scoreboard.delete_score(name)
        elif choice == "3":
            scoreboard.print_scores()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None

class Scoreboard:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_score(self, name, score):
        new_node = Node(name, score)
        if not self.head or score >= self.head.score:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and score < current.next.score:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1
        if self.size > 10:
            self.delete_last()

    def delete_score(self, name):
        if not self.head:
            print("Scoreboard is empty.")
            return
        if self.head.name == name:
            self.head = self.head.next
            self.size -= 1
            print(f"{name}'s score has been deleted.")
            return
        current = self.head
        while current.next:
            if current.next.name == name:
                current.next = current.next.next
                self.size -= 1
                print(f"{name}'s score has been deleted.")
                return
            current = current.next
        print(f"No player with the name {name} found.")

    def delete_last(self):
        if not self.head:
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
        self.size -= 1

    def print_scores(self):
        if not self.head:
            print("Scoreboard is empty.")
        else:
            print("Top 10 Scores:")
            current = self.head
            position = 1
            while current and position <= 10:
                print(f"{position}. {current.name}: {current.score}")
                current = current.next
                position += 1

def main():
    scoreboard = Scoreboard()
    while True:
        print("\nMenu:")
        print("1. Add a new player score")
        print("2. Delete a player/score node")
        print("3. Print the list")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter player name: ")
            score = int(input("Enter player score: "))
            scoreboard.add_score(name, score)
        elif choice == "2":
            name = input("Enter the name of the player to delete: ")
            scoreboard.delete_score(name)
        elif choice == "3":
            scoreboard.print_scores()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
