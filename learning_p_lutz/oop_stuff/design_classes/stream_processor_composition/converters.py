from learning_p_lutz.oop_stuff.design_classes.stream_processor_composition.streams import Processor
import sys


class Uppercase(Processor):
    """Inherits the stream-processing loop logic. Defines data conversion logic"""

    def converter(self, data):
        return data.upper()


class HTMLize:

    def write(self, line):
        print(f'<PRE>{line.rstrip()}</PRE>')


if __name__ == '__main__':

    obj = Uppercase(open('trispam.txt'), sys.stdout)  # sys.stdout is a writer here
    obj.process()
    # SPAM
    # SPAM
    # SPAM!

    obj2 = Uppercase(open('trispam.txt'), HTMLize())  # HTMLize() is a writer here
    obj2.process()
    # < PRE > SPAM < / PRE >
    # < PRE > SPAM < / PRE >
    # < PRE > SPAM! < / PRE >
