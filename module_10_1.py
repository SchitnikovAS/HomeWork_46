from threading import Thread
from time import sleep
from time import time


def write_words(word_count: int, file_name: str) -> None:
    with open(file_name, "a", encoding="utf-8") as file:
        for line in range(word_count):
            file.write(f'Какое-то слово № {line + 1} \n')

    print(f"Завершилась запись в файл {file_name}")
    sleep(0.1)


start_time = time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

finish_time = time()
print(f'Работа потоков {finish_time - start_time}')

start_time_2 = time()

the_first = Thread(target=write_words, args=(10, 'example5.txt',))
the_second = Thread(target=write_words, args=(30, 'example6.txt',))
the_third = Thread(target=write_words, args=(200, 'example7.txt',))
the_fourth = Thread(target=write_words, args=(100, 'example8.txt',))

the_first.start()
the_second.start()
the_third.start()
the_fourth.start()

the_first.join()
the_second.join()
the_third.join()
the_fourth.join()

finish_time_2 = time()
print(f'Работа потоков {finish_time_2 - start_time_2}')
