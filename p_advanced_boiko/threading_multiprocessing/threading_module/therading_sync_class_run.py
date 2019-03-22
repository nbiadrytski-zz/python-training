from p_advanced_boiko.threading_multiprocessing.threading_module.threading_sync_class import MyThread

# create threads
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

# start threads
thread1.start()
thread2.start()

# Wait until the thread terminates.
# This blocks the calling thread until the thread whose join() method is called terminates
thread1.join()
thread2.join()

print('Exiting main thread')
