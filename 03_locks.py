"""
Step 3: Thread Synchronization - The Race Condition Problem
Without locks, multiple threads accessing shared data can cause issues.
"""
import threading

# Shared counter (dangerous without lock!)
counter = 0

def increment_without_lock():
    global counter
    for _ in range(100000):
        counter += 1

def increment_with_lock(lock):
    global counter
    for _ in range(100000):
        with lock:  # Only one thread can execute this block at a time
            counter += 1

if __name__ == "__main__":
    # Test WITHOUT lock (race condition)
    print("=== WITHOUT LOCK ===")
    counter = 0
    threads = [threading.Thread(target=increment_without_lock) for _ in range(5)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"Expected: 500000, Got: {counter}")
    print(f"Data corruption: {counter != 500000}")
    
    # Test WITH lock (safe)
    print("\n=== WITH LOCK ===")
    counter = 0
    lock = threading.Lock()
    threads = [threading.Thread(target=increment_with_lock, args=(lock,)) for _ in range(5)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    
    print(f"Expected: 500000, Got: {counter}")
    print(f"Data corruption: {counter != 500000}")
