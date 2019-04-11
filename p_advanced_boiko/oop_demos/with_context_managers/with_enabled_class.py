class WithEnabled:  # context manager
    def __enter__(self):
        print('__enter__')
        return self

    # Params describe the exception that caused the context to be exited.
    # If the context was exited without an exception, all three arguments will be None.
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')
        print(exc_type, 'exc_type')  # <class 'Exception'> exc_type
        print(exc_val, 'exc_val')  # This is an exception!!! exc_val
        print(exc_tb, 'exc_traceback')  # <traceback object at 0x109b30108> exc_traceback


# with WithEnabled() as we_exception:  # we_exception is an object of WithEnabled()
#     raise Exception('This is an exception!!!')


with WithEnabled() as we_no_exception:  # we_exception is an object of WithEnabled()
    print('There is no exception!!!')
# __enter__
# There is no exception!!!
# __exit__
# None exc_type
# None exc_val
# None exc_traceback
