import datetime
import os


def logger(old_function):
    def new_function(*args, **kwargs):
        date_time = datetime.datetime.now()
        function_name = old_function.__name__
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(f'Дата и время: {date_time}\n'
                    f'Имя функции: {function_name}\n'
                    f'Аргументы: {args}, {kwargs}\n'
                    f'Результат: {result}\n')
            return result
    return new_function


# @logger
# def hello_world(text, **k_text):
#     return f'Результат работы функции: {text}, {k_text}'
#
#
# print(hello_world('Hello, World!', hello='text'))


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path, encoding='utf-8') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
