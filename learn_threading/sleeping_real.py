import time
import threading


def do_something(seconds: int) -> None:
    print("Sleeping {}s...".format(seconds))
    time.sleep(seconds)
    print("Done Sleeping...{}s".format(seconds))


if __name__ == '__main__':
    start = time.perf_counter()

    threads: list = []
    my_args: tuple = (2, 1, 2, 3, 2, 1, 2, 2, 2)

    for arg in my_args:
        t = threading.Thread(target=do_something, args=[arg])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
