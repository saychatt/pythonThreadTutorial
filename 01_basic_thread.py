"""
Step 1: Creating and Starting a Basic Thread
A thread is a separate flow of execution within a program.
"""
import threading
import time

def print_numbers():
    """Function that will run in a separate thread"""
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)

def print_letters():
    """Another function for a separate thread"""
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letter: {letter}")
        time.sleep(1)

if __name__ == "__main__":
    print("Starting threads...")
    
    # Create thread objects
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    
    # Start the threads
    thread1.start()
    thread2.start()
    
    # Wait for both threads to complete
    thread1.join()
    thread2.join()
    
    print("Both threads finished!")
