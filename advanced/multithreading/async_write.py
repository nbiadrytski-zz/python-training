import threading
import time


class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out

    def run(self):
        f = open(self.out, "a")
        f.write(self.text + "\n")
        f.close()
        time.sleep(2)
        print("Finished Background file write to " + self.out)


def main():
    message = input("Enter a string to store:")
    background = AsyncWrite(message, "out.txt")
    background.start()
    print("The program can continue to run while writing in another thread")
    print(100 + 400)

    background.join()  # waits until thread is finished before resuming
    print("Waited until thread was completed")


if __name__ == "__main__":
    main()
