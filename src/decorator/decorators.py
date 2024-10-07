import logging
from functools import wraps


# Настроим логгер для вывода информации
def log(filename=None):
    def decorator(func):
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
