"""
Step 2: Passing Arguments to Thread Functions
"""
import threading
import time

def download_file(file_name, size):
    """Simulate downloading a file"""
    print(f"Starting download: {file_name} ({size}MB)")
    time.sleep(2)  # Simulate download time
    print(f"Completed: {file_name}")

if __name__ == "__main__":
    files = [
        ("video.mp4", 100),
        ("document.pdf", 5),
        ("music.mp3", 10)
    ]
    
    threads = []
    
    # Create and start threads with arguments
    for file_name, size in files:
        thread = threading.Thread(target=download_file, args=(file_name, size))
        threads.append(thread)
        thread.start()
    
    # Wait for all downloads to complete
    for thread in threads:
        thread.join()
    
    print("All downloads complete!")
