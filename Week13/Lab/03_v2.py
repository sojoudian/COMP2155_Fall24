from threading import Thread, active_count

counter = 0


def increment():
    global counter
    for _ in range(200000000):
        counter += 1


threads = [Thread(target=increment) for _ in range(6)]  # 6 * 5 = 25
print(f"Active threads before starting: {active_count()}")

for t in threads:
    t.start()
    print(f"Active threads after starting {t.name}: {active_count()}")

for t in threads:
    t.join()
    print(f"Active threads after joining {t.name}: {active_count()}")

print(f"Counter Value: {counter}")