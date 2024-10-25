import logging
from functools import wraps


# Настроим логгер для вывода информации
def log(filename=None):
    """
        Декоратор для логирования выполнения функции.

        Логирует начало и конец выполнения функции, а также результаты или ошибки.
        Логи могут выводиться в консоль или записываться в файл.

        Args:
            filename (str, optional): Имя файла для записи логов.
            Если не указано, логи выводятся в консоль.

        Returns:
            function: Декорированная функция с логированием.
        """
    def decorator(func):
        """
               Декоратор, оборачивающий функцию для логирования ее вызовов.

               Args:
                   func (function): Функция, которую нужно обернуть.

               Returns:
                   function: Обернутая функция.
               """
        logger = logging.getLogger(func.__name__)

        # Если указан файл, настраиваем запись в файл
        if filename:
            handler = logging.FileHandler(filename)
        else:
            handler = logging.StreamHandler()  # Иначе вывод в консоль

        # Формат логов
        formatter = logging.Formatter('%(levelname)s: %(message)s')
        handler.setFormatter(formatter)

        # Настраиваем логгер
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        @wraps(func)
        def wrapper(*args, **kwargs):
            """
                        Обертка для логирования вызовов функции.

                        Логирует вызов функции, результат или ошибку.

                        Args:
                            *args: Позиционные аргументы функции.
                            **kwargs: Именованные аргументы функции.

                        Returns:
                            Любое: Результат выполнения обернутой функции.

                        Raises:
                            Exception: Любая ошибка, возникшая при выполнении функции, будет занесена в лог.
                        """
            try:
                logger.info(f"Запуск функции: {func.__name__} с аргументами: {args}, {kwargs}")
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as e:
                logger.error(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                # Убираем хендлер, чтобы избежать дублирования логов при повторном вызове
                logger.removeHandler(handler)

        return wrapper

    return decorator
