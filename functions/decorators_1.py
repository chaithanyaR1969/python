def main():
    print("inside main")
def outer(ptr):
    print("inside outer")
    def inner():
        print("entering inner")
        ptr()
        print("leaving inner")
    return inner
ref=outer(main)
ref()
