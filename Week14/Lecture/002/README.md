# Railway Reservation System with Semaphore

This Python application demonstrates a railway reservation system using threading and semaphore synchronization to handle concurrent berth reservation requests safely.

## Application Logic

The application simulates a railway reservation process where multiple users (threads) attempt to reserve limited berths simultaneously. The key components are:

1. **Railway Class**:
   - The `Railway` class manages berth availability and uses a semaphore to ensure thread-safe operations.
   - Attributes:
     - `available`: Tracks the number of available berths.
     - `l`: A semaphore object to control access to shared resources.

2. **Reserve Method**:
   - The `reserve` method handles the reservation process.
   - A semaphore lock is acquired before checking or updating the number of berths.
   - If the requested number of berths is available, the reservation is processed; otherwise, the user is informed that no berths are available.
   - After completing the reservation, the semaphore lock is released to allow other threads access.

3. **Main Logic**:
   - An instance of `Railway` is initialized with a specific number of available berths (in this example, 1).
   - Two threads are created, each requesting 1 berth.
   - The program ensures the threads execute sequentially without race conditions using semaphore synchronization.

## Avoiding Race Conditions

A **race condition** occurs when multiple threads simultaneously access shared resources, leading to inconsistent or incorrect results. This application prevents race conditions by using a **Semaphore**:

- The `acquire` method ensures that only one thread can access the critical section (checking and updating berth availability) at a time.
- The `release` method allows the next thread to enter the critical section after the current thread completes its task.

### Example Scenario

1. Initially, 1 berth is available.
2. Thread `t1` acquires the semaphore lock, reserves the berth, and updates the availability.
3. Thread `t2` attempts to reserve but finds no berths available due to the semaphore synchronization.

## Usage

### Prerequisites

- Python 3.6 or later

### Running the Program

1. Save the script as `002.py`.
2. Execute the script using Python:

   ```bash
   python 002.py
   ```

### Output

The program produces output similar to:

```plaintext
Available no. of berths =  1
1 berth(s) are allotted for First Person
Available no. of berths =  0
Sorry, no berths to allot
```

## Key Concepts Demonstrated

- **Threading**: Managing concurrent execution using threads.
- **Semaphore**: Synchronization mechanism to ensure safe access to shared resources.
- **Concurrency**: Efficiently handling shared resource management in multi-threaded environments.



