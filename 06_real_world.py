"""
Step 6: Real-World Example - Parallel URL Fetching
Demonstrates significant speedup with threading for I/O-bound tasks.
"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor
import urllib.request

def fetch_url(url):
    """Fetch a URL and return its size"""
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = response.read()
            return url, len(data)
    except Exception as e:
        return url, f"Error: {e}"

def sequential_fetch(urls):
    """Fetch URLs one by one"""
    results = []
    for url in urls:
        results.append(fetch_url(url))
    return results

def parallel_fetch(urls, max_workers=5):
    """Fetch URLs in parallel"""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(fetch_url, urls))
    return results

if __name__ == "__main__":
    urls = [
        "https://www.python.org",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org",
        "https://www.reddit.com"
    ]
    
    print("=== Sequential Fetching ===")
    start = time.time()
    results = sequential_fetch(urls)
    sequential_time = time.time() - start
    
    for url, size in results:
        print(f"{url}: {size} bytes" if isinstance(size, int) else f"{url}: {size}")
    print(f"Time: {sequential_time:.2f} seconds\n")
    
    print("=== Parallel Fetching ===")
    start = time.time()
    results = parallel_fetch(urls)
    parallel_time = time.time() - start
    
    for url, size in results:
        print(f"{url}: {size} bytes" if isinstance(size, int) else f"{url}: {size}")
    print(f"Time: {parallel_time:.2f} seconds")
    
    print(f"\nSpeedup: {sequential_time/parallel_time:.2f}x faster!")
