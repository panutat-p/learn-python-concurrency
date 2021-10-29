import time
import concurrent.futures


def do_something(seconds: int) -> str:
    print("Sleeping {}s...".format(seconds))
    time.sleep(seconds)
    return "Done Sleeping...{}s".format(seconds)


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        f1 = executor.submit(do_something, 2)  # submit() schedule thread and return future object
        f2 = executor.submit(do_something, 2)  # submit() schedule thread and return future object

        print(f1.result())  # wait until future return result

        print(f2.result())  # wait until future return result

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
