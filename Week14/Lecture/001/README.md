
# Railway Reservation System

This project is a Python-based multi-threaded application that demonstrates a railway reservation system. It allows multiple users (threads) to request berths simultaneously while avoiding race conditions using thread synchronization.

## Application Logic

The application simulates the process of reserving railway berths. The main components are:

1. **Railway Class**:
   - The `Railway` class manages berth availability and ensures thread-safe access using a threading lock.
   - The class has two attributes:
     - `available`: Number of available berths.
     - `l`: A lock object to synchronize threads.

2. **Reserve Method**:
   - The `reserve` method is responsible for handling berth reservations.
   - Threads acquire the lock before checking or updating berth availability.
   - If the requested number of berths is available, the reservation is processed; otherwise, a message is displayed stating no berths are available.
   - After processing, the lock is released to allow other threads to access the method.

3. **Main Logic**:
   - An instance of `Railway` is created with a predefined number of available berths (in this case, 1).
   - Two threads (`t1` and `t2`) are started, each requesting 1 berth.
   - The program ensures that the threads execute sequentially without interfering with each other's data.

## Avoiding Race Conditions

A **race condition** occurs when multiple threads access shared data simultaneously, leading to inconsistent or unexpected results. To prevent this, the `Lock` object from the `threading` module is used:

- The `acquire` method ensures that only one thread can execute the critical section (checking and updating berth availability) at a time.
- The `release` method allows other threads to enter the critical section after the current thread completes its execution.

### Example Scenario

- Initially, 1 berth is available.
- Thread `t1` acquires the lock and reserves the berth.
- Thread `t2` attempts to reserve but finds no berths available since the lock ensures sequential access.

## Usage

### Prerequisites

- Python 3.6 or later

### Running the Program

1. Clone the repository or copy the script to a local file, e.g., `railway_reservation.py`.
2. Run the script using Python:

   ```bash
   python railway_reservation.py
   ```

### Output

The program produces output similar to the following:

```plaintext
Available no. of berths = 1
1 berths are allotted for First Person
Available no. of berths = 0
Sorry, no berths to allot
Reservation process completed.
```

## Key Concepts Demonstrated

- **Threading**: The use of threads to handle multiple users simultaneously.
- **Locks**: Synchronization mechanism to avoid race conditions.
- **Concurrency**: Managing shared resources among multiple threads.

## Extending the Program

- Modify the number of available berths to simulate different scenarios.
- Add more threads to test concurrent access and ensure thread safety.

## License

This project is licensed under the MIT License - feel free to use and modify it.

