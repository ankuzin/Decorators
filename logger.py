from datetime import datetime

LOGFILE = 'log_file.txt'


# Задание №1
def logger(old_function):
    def new_func(*args):
        now = datetime.now()
        a = []
        for argument in args:
            a.append(argument)
        result = old_function(*args)
        with open('logfile.txt', 'a', encoding='utf-8') as log:
            log.write(f'Вызов функции {old_function.__name__}, время вызова - {now},аргументы {a},возвращаемое значение {result} \n')
        return result
    return new_func


# Задание №2
def loggertofile(logfile):
    def logger(old_function):
        def func(*args):
            nonlocal logfile
            a = []
            for argument in args:
                a.append(argument)
            now = datetime.now()
            result = old_function(*args)
            with open(logfile, 'a', encoding='utf-8') as log:
                log.write(f'Вызов функции {old_function.__name__}, время вызова - {now},аргументы {a},возвращаемое значение {result} \n')
            return result
        return func
    return logger


# Задание №3
@loggertofile(LOGFILE)
def ymno(a,b):
    result = a*b
    print(result)

ymno(21,2331)












