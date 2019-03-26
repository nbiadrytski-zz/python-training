from multiprocessing import Process


def say_hello(name='world'):
    print(f'Hello {name}')


p = Process(target=say_hello)
p.start()
p.join()  # main process waits until child process is done
