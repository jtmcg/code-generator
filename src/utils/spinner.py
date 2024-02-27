import sys
import time
import threading

class Spinner:
    busy = False
    delay = 0.1
    context = ''

    @staticmethod
    def spinning_cursor():
        while 1: 
            for cursor in '|/-\\': yield cursor

    def __init__(self, context = None, delay=None):
        self.spinner_generator = self.spinning_cursor()
        if delay and float(delay): self.delay = delay
        if context and str(context): self.context = context

    def spinner_task(self):
        sys.stdout.write(f'{self.context} ')
        while self.busy:
            sys.stdout.write(next(self.spinner_generator))
            sys.stdout.flush()
            time.sleep(self.delay)
            sys.stdout.write('\b')
            sys.stdout.flush()

    def __enter__(self):
        self.busy = True
        threading.Thread(target=self.spinner_task).start()

    def __exit__(self, exception, _value, _tb):
        self.busy = False
        time.sleep(self.delay)
        if exception is not None:
            return False