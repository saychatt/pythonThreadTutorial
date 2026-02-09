"""
Step 4: Producer-Consumer Pattern with Queue
Queue is thread-safe and perfect for passing data between threads.
"""
import threading
import queue
import time
import random

def producer(q, producer_id):
    """Produces items and puts them in the queue"""
    for i in range(5):
        item = f"Item-{producer_id}-{i}"
        q.put(item)
        print(f"Producer {producer_id} produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))
    print(f"Producer {producer_id} finished")

def consumer(q, consumer_id):
    """Consumes items from the queue"""
    while True:
        try:
            item = q.get(timeout=2)  # Wait max 2 seconds
            print(f"  Consumer {consumer_id} consumed: {item}")
            time.sleep(random.uniform(0.1, 0.3))
            q.task_done()
        except queue.Empty:
            print(f"  Consumer {consumer_id} timed out, exiting")
            break

if __name__ == "__main__":
    # Create a thread-safe queue
    work_queue = queue.Queue()
    
    # Create producer threads
    producers = [
        threading.Thread(target=producer, args=(work_queue, i))
        for i in range(2)
    ]
    
    # Create consumer threads
    consumers = [
        threading.Thread(target=consumer, args=(work_queue, i))
        for i in range(3)
    ]
    
    # Start all threads
    for p in producers:
        p.start()
    for c in consumers:
        c.start()
    
    # Wait for producers to finish
    for p in producers:
        p.join()
    
    # Wait for queue to be empty
    work_queue.join()
    
    # Wait for consumers to finish
    for c in consumers:
        c.join()
    
    print("\nAll work completed!")
