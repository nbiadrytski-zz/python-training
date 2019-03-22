from p_advanced_boiko.threading_multiprocessing.threading_module.threading_module_class import MyThread

# craete threads
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

# start threads
thread1.start()
thread2.start()

print('Exiting main thread')



