import time
import concurrent.futures


def do_something(seconds: int) -> str:
    print("Sleeping {}s...".format(seconds))
    time.sleep(seconds)
    return "Done Sleeping...{}s".format(seconds)


if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        my_args: tuple = (5, 4, 3, 2, 1)

        my_futures = executor.map(do_something, my_args)  # return results by the order that they were started

        for f in my_futures:  # join all threads
            try:
                print(f)  # exception will be raised when retrieving result
            except Exception as e:
                print(e)

    finish = time.perf_counter()

    print(f'Finished in {round(finish - start, 2)} second(s)')
