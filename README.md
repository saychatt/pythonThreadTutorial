# Python Threading Tutorial

A hands-on, step-by-step guide to Python threading with working examples.

## 📚 Tutorial Structure

Run the examples in order:

1. **[01_basic_thread.py](01_basic_thread.py)** - Creating and starting threads
2. **[02_thread_args.py](02_thread_args.py)** - Passing arguments to threads
3. **[03_locks.py](03_locks.py)** - Thread synchronization and race conditions
4. **[04_producer_consumer.py](04_producer_consumer.py)** - Producer-consumer pattern with Queue
5. **[05_threadpool.py](05_threadpool.py)** - ThreadPoolExecutor (modern approach)
6. **[06_real_world.py](06_real_world.py)** - Real-world web scraping example
7. **[07_summary.py](07_summary.py)** - Best practices and summary

## 🚀 Quick Start

```bash
cd ~/threading-tutorial
python3 01_basic_thread.py
python3 02_thread_args.py
# ... continue with each file
```

## 💡 Key Takeaways

- Use threading for **I/O-bound** tasks (network, files, databases)
- Use **ThreadPoolExecutor** for easier thread management
- Use **Locks** to protect shared data
- Use **Queue** for thread-safe communication
- Don't use threading for CPU-intensive tasks (use multiprocessing)

## 📖 Learning Path

1. Start with basic examples (01-02)
2. Understand synchronization (03)
3. Learn common patterns (04)
4. Master modern approach (05)
5. See real-world application (06)
6. Review best practices (07)

Happy threading! 🧵
