import threading

from multyAsyncParallel.multithreading.count_three_sum import read_ints, count_three_sum

if __name__=='__main__':
    print('started main')

    ints = read_ints('../data/1Kints.txt')

    # Cоздаем поток. Говорим, что надо запустить функцию count_three_sum и передадим в эту функцию аргумент ints
    # t1 = threading.Thread(target=count_three_sum, args=(ints,)) # foreground
    # t1 = threading.Thread(target=count_three_sum, args=(ints,), daemon=True) # background
    t1 = threading.Thread(target=count_three_sum, daemon=True, kwargs=dict(ints=ints)) # через kwargs аргументы передавать лучше
    t1.start() # запуск потока

    count_three_sum(ints)

    print('What are we waiting for?')
    print('ended main')