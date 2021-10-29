import time
import threading


def do_something(seconds):
    print("Sleeping {}s...".format(seconds))
    time.sleep(seconds)
    print("Done Sleeping...{}s".format(seconds))


if __name__ == '__main__':
    start = time.perf_counter()

    t1 = threading.Thread(target=do_something, args=(2,))
    t2 = threading.Thread(target=do_something, args=(2,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
