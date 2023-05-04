import subprocess
from chardet import detect


def task_1():
    """Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
        проверить тип и содержание соответствующих переменных. Затем с помощью
        онлайн-конвертера преобразовать строковые представление в формат Unicode и также
        проверить тип и содержимое переменных."""

    words = ('разработка', 'сокет', 'декоратор')
    for i in words:
        print(f'Type - {type(i)}, value - {i}')

    unicod_words = ('\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430', '\u0441\u043e\u043a\u0435\u0442',
                    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440')
    for i in unicod_words:
        print(f'Type - {type(i)}, value - {i}')


def task_2():
    """Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
    последовательность кодов (не используя методы encode и decode) и определить тип,
    содержимое и длину соответствующих переменных."""

    words = (b'class', b'function', b'method',)
    for i in words:
        print(f'Type - {type(i)}, Len - {len(i)}')


def task_3():
    """Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
    байтовом типе.
    """

    words = ('attribute', 'класс', 'функция', 'type',)
    for i in words:
        try:
            x = i.encode('ascii')
            print(x.decode())
        except UnicodeEncodeError:
            print('Латинские буквы преоброзовать не получится')


def task_4():
    """Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
    строкового представления в байтовое и выполнить обратное преобразование (используя
    методы encode и decode).
    """

    words = ('разработка', 'администрирование', 'protocol', 'standard')
    for i in words:
        i = i.encode()
        print(f'Байтовое представление {i}')
        i = i.decode()
        print(f'Строка - {i}')


def task_5():
    """Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
    байтовового в строковый тип на кириллице.
    """

    ping = subprocess.Popen(['ping', 'youtube.com'], stdout=subprocess.PIPE).stdout.readlines()
    for i in ping:
        print(i.decode('cp866'))


def task_6():
    """Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
    программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
    Принудительно открыть файл в формате Unicode и вывести его содержимое.
    """

    words = ('сетевое программирование', 'сокет', 'декоратор')
    words = map(lambda i: i+'\n', words)
    with open('test_file.txt', 'w') as f:
        f.writelines(words)

    with open('test_file.txt', 'rb') as f:
        data = f.read()
        encode = detect(data)
        print(encode)
        print(data.decode(encode['encoding']))

