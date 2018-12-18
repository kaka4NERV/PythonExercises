from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print(f'Run task {name} {os.getpid()}...')
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task {} runs {:.2f} seconds'.format(name, (end - start)))


if __name__ == '__main__':
    print(f'Parent process {os.getpid()}.')
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
