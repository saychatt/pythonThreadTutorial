"""
Step 5: ThreadPoolExecutor - Modern, Easier Way to Manage Threads
Automatically manages a pool of threads for you.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def process_task(task_id):
    """Simulate processing a task"""
    print(f"Task {task_id} started")
    time.sleep(1)
    result = task_id * 2
    print(f"Task {task_id} completed")
    return result

if __name__ == "__main__":
    print("=== Using ThreadPoolExecutor ===\n")
    
    # Create a pool with 3 worker threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Submit tasks
        tasks = [executor.submit(process_task, i) for i in range(6)]
        
        # Get results as they complete
        for future in as_completed(tasks):
            result = future.result()
            print(f"  Result: {result}")
    
    print("\n=== Using map (simpler for same function) ===\n")
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Map function to inputs (returns results in order)
        results = executor.map(process_task, range(6))
        print(f"All results: {list(results)}")
