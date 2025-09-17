# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self): #initializes class
        self.front = None
        self.rear = None
    
    def enqueue(self,value):
        newnode = Node(value) 
        if not self.front: #if self.front has no value, then the newnode is made front value and the rear value
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode #the rear is made the new node
            self.rear = newnode #the new node is made the rear

    def dequeue(self):
        if not self.front: #makes sure that there is anything present in the queue,
            return None
        removednode = self.front
        self.front = self.front.next #removes the front node by replacing it with the next one

        if not self.front: #updates the rear to None if the node removed was the last one
            self.rear = None
        return removednode.value
    
    def peek(self):
        if self.front:
            return self.front.value #returns front value that can have something done with it
        else:
            return None
        
    def print_queue(self):
        firstnode = self.front #creates variable for first value in the queue
        if not firstnode: #makes sure the queue isn't empty
          print("Queue is empty")
          return
        while firstnode:
            print(f"-{firstnode.value}")
            firstnode = firstnode.next #sets the firstnode variable to the next value in queue
    


def run_help_desk():
    # Create an instance of the Queue class
    helpdesk = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            helpdesk.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            if helpdesk.front: #makes sure there are customers in the queue
                firstcustomer = helpdesk.front.value
                helpdesk.dequeue()
                print(f"Helped {firstcustomer} and removed from queue")
            else:
                print("There are no customers left to help")



        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            if helpdesk.front == None: #makes sure there are customers in the queue
                print("There are no more customers in the queue")
            else:
                print(f"The next customer in the queue is {helpdesk.peek()}")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            helpdesk.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
