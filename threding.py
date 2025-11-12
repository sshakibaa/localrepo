#thredeing in python
from threading import Thread
import time
class MyThread(Thread):
    def __init__(self, thread_id, name, delay):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Starting thread: {self.name}")
        
        self.print_numbers()
        
        print(f"Exiting thread: {self.name}")

    def print_numbers(self):
        count = 0
        while count < 5:
            time.sleep(self.delay)
            count += 1
            print(f"{self.name}: {count}")

# Create threads
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)
# Start threads
thread1.start()
time.sleep(0.5)  # Slight delay to stagger thread starts
thread2.start()
time.sleep(0.5)
# Wait for both threads to complete
thread1.join()
thread2.join()
print("Exiting main thread")