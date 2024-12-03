
# Thread Synchronization and Deadlock Avoidance in Python

This Python application demonstrates thread synchronization techniques to safely handle shared resources and avoid deadlocks. It uses consistent lock acquisition order to ensure thread safety while performing railway ticket booking and cancellation operations.

## Application Logic

The program simulates a railway ticketing system with two operations: **ticket booking** and **ticket cancellation**. Both operations require access to two shared resources represented by locks (`lock1` and `lock2`).

### Key Components

1. **Locks (`lock1` and `lock2`)**:
   - Two lock objects are initialized to control access to shared resources (e.g., train and compartment).

2. **Ticket Cancellation (`cancel_ticket` function)**:
   - Acquires locks in a consistent order (`lock1` followed by `lock2`) to avoid deadlocks.
   - Simulates the ticket cancellation process.

3. **Ticket Booking (`book_ticket` function)**:
   - Also acquires locks in the same consistent order (`lock1` followed by `lock2`).
   - Simulates the ticket booking process.

4. **Threads (`thread1` and `thread2`)**:
   - `thread1`: Executes the `book_ticket` function.
   - `thread2`: Executes the `cancel_ticket` function.

### Deadlock Avoidance

Deadlocks are avoided by ensuring both functions acquire locks in the same order:

- `lock1` is always acquired before `lock2` in both `book_ticket` and `cancel_ticket` functions.
- This eliminates circular wait conditions, a primary cause of deadlocks.

## Usage

### Prerequisites

- Python 3.6 or later

### Running the Program

1. Save the script as `004.py`.
2. Execute the script using Python:

   ```bash
   python 004.py
   ```

### Expected Output

The program executes without deadlocks and produces the following output:

```plaintext
Bookticket: Locked train
Bookticket: Wants to lock compartment
Bookticket: Locked compartment
Bookticket: Booking is done.
Cancelticket: Locked train
Cancelticket: Wants to lock compartment
Cancelticket: Locked compartment
Cancelticket: Cancellation is done.
Both operations completed successfully.
```

### Key Features

- **Thread Synchronization**: Ensures safe access to shared resources.
- **Deadlock Avoidance**: Consistent lock acquisition order prevents deadlocks.

## Key Concepts Demonstrated

- **Threading**: Managing concurrent execution using threads.
- **Locks**: Synchronization primitives to protect shared resources.
- **Deadlock Prevention**: Eliminating circular wait by acquiring locks in a consistent order.
