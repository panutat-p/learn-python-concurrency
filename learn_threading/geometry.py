import threading
import time

# https://www.youtube.com/watch?v=cdPZ1pJACMI

def print_cube(num: int, res: list):
    """
    function to print cube of given num
    """
    time.sleep(2)
    print("Cube: {}".format(num * num * num))
    res.append(num * num * num)


def print_square(num:int, res: list):
    """
    function to print square of given num
    """
    time.sleep(5)
    print("Square: {}".format(num * num))
    res.append(num * num)


if __name__ == '__main__':
    # shared resource
    result = []

    # creating thread
    t1 = threading.Thread(target=print_square, args=(10, result,))
    t2 = threading.Thread(target=print_cube, args=(10, result,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    print("t1 terminated")
    # wait until thread 2 is completely executed
    t2.join()
    print("t2 terminated")

    print("result: {}".format(result))

    # both threads completely executed
    print("Done!")
