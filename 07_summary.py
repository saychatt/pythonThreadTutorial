"""
PYTHON THREADING SUMMARY & BEST PRACTICES
==========================================

1. WHEN TO USE THREADING:
   ✓ I/O-bound tasks (network requests, file operations, database queries)
   ✗ CPU-bound tasks (use multiprocessing instead due to GIL)

2. KEY CONCEPTS:
   - Thread: Separate flow of execution
   - Lock: Prevents race conditions on shared data
   - Queue: Thread-safe data passing between threads
   - ThreadPoolExecutor: Modern, easier thread management

3. COMMON PATTERNS:

   a) Basic Thread:
      thread = threading.Thread(target=function, args=(arg1, arg2))
      thread.start()
      thread.join()  # Wait for completion

   b) With Lock:
      lock = threading.Lock()
      with lock:
          # Critical section - only one thread at a time
          shared_data += 1

   c) Producer-Consumer:
      q = queue.Queue()
      q.put(item)      # Producer
      item = q.get()   # Consumer
      q.task_done()    # Mark as processed

   d) ThreadPoolExecutor (RECOMMENDED):
      with ThreadPoolExecutor(max_workers=5) as executor:
          results = executor.map(function, items)

4. COMMON PITFALLS:
   ✗ Forgetting to use locks with shared data
   ✗ Using threading for CPU-intensive tasks
   ✗ Not calling join() and wondering why program exits early
   ✗ Deadlocks (two threads waiting for each other's locks)

5. DEBUGGING TIPS:
   - Use threading.current_thread().name to identify threads
   - Add logging to track thread execution
   - Start with small number of threads
   - Test with and without threading to verify correctness

6. PERFORMANCE:
   - More threads ≠ faster (overhead exists)
   - Optimal thread count depends on task type
   - For I/O: typically 5-20 threads is good
   - Measure before and after to verify improvement
"""

# Example: Complete template for a threaded application
import threading
from concurrent.futures import ThreadPoolExecutor
import queue

def worker_function(item):
    """Process a single item"""
    # Your logic here
    return f"Processed: {item}"

def main():
    items = range(10)
    
    # Method 1: ThreadPoolExecutor (RECOMMENDED)
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(worker_function, items))
    
    print(results)

if __name__ == "__main__":
    main()
