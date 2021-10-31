import time
import concurrent.futures


def do_something(seconds: int) -> str:
    print("Sleeping {}s...".format(seconds))
    time.sleep(seconds)
    return "Done Sleeping...{}s".format(seconds)


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        my_futures: list = []
        my_args: tuple = (1, 2, 2, 1, 2, 3, 2)

        for arg in my_args:
            f = executor.submit(do_something, arg)
            my_futures.append(f)

        for f in concurrent.futures.as_completed(my_futures):
            print(f.result())

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
