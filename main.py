def print_hi(name):
    """

    :param name: the to say hi
    :return: None
    """
    # Use a breakpoint in the code line below to debug your script.
    return f"Hi, {name}"  # Press ⌘F8 to toggle the breakpoint.


class Hi:
    def __init__(self):
        self.hi = "hi there!"

    def say(self):
        print(self.hi)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print_hi("PyCharm")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
