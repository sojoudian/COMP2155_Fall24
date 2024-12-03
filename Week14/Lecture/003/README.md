
# Deadlock Simulation in Python

This Python application demonstrates a classic deadlock scenario using threads and locks. It serves as an educational example to understand how deadlocks occur and how to avoid them in multi-threaded programming.

## Application Logic

The program simulates a railway ticketing system where two operations, **ticket booking** and **ticket cancellation**, require access to two shared resources (locks). These operations result in a deadlock due to the improper order of acquiring locks.

### Key Components

1. **Locks (`l1` and `l2`)**:
   - Two lock objects are initialized to represent shared resources (e.g., train and compartment).

2. **Ticket Cancellation (`cancelticket` function)**:
   - Acquires lock `l2` first and then attempts to acquire lock `l1`.
   - Represents a scenario where one thread is waiting for a resource held by another.

3. **Ticket Booking (`bookticket` function)**:
   - Acquires lock `l1` first and then attempts to acquire lock `l2`.
   - Represents the reverse order of lock acquisition compared to the cancellation operation.

4. **Threads (`t1` and `t2`)**:
   - `t1`: Executes the `bookticket` function.
   - `t2`: Executes the `cancelticket` function.

### Deadlock Scenario

- **Deadlock Condition**: A deadlock occurs when:
  1. `t1` locks `l1` and waits for `l2`.
  2. `t2` locks `l2` and waits for `l1`.
  - Neither thread can proceed, causing the program to hang indefinitely.

## Avoiding Deadlocks

To prevent deadlocks, ensure that all threads acquire locks in a consistent order. For example:

1. Both `bookticket` and `cancelticket` functions should acquire locks in the same order (`l1` followed by `l2` or vice versa).
2. Alternatively, use higher-level synchronization mechanisms like `RLock` or `Semaphore` to manage resource access more flexibly.

## Usage

### Prerequisites

- Python 3.6 or later

### Running the Program

1. Save the script as `003.py`.
2. Execute the script using Python:

   ```bash
   python 003.py
   ```

### Expected Behavior

The program demonstrates a deadlock scenario where both threads block indefinitely. The output will resemble:

```plaintext
Bookticket locked train
Bookticket wants to lock on compartment
Cancelticket locked compartment
Cancelticket wants to lock on train
```

### Resolving Deadlock

To observe a non-deadlocked version of this program, modify the lock acquisition order in the `cancelticket` or `bookticket` function to ensure consistency.

## Key Concepts Demonstrated

- **Threading**: Managing concurrent execution using threads.
- **Locks**: Synchronization primitives to protect shared resources.
- **Deadlock**: A state where two or more threads are waiting for each other to release resources.


