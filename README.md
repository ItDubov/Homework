# Проект Виджета Банковских Операций

## Описание
Это проект виджета, предназначенного для обработки и маскирования данных о банковских операциях клиента. Проект предоставляет функции для маскировки номеров карт и счетов, фильтрации операций по статусу и сортировки операций по дате.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/ваш-репозиторий

# Тестирование: 
Добавление тестов для модулей `masks` и `processing`

### Описание:
В рамках данного Pull Request были добавлены тесты для следующих функций:
- `get_mask_card_number`: тестирование различных случаев маскирования номеров карт.
- `get_mask_account`: проверка работы с номерами счетов различных форматов.
- `mask_account_card`: тестирование распознавания карт и счетов, а также проверка на некорректные данные.
- `filter_by_state`: тестирование фильтрации операций по статусу.
- `sort_by_date`: проверка сортировки операций по дате в обоих направлениях.

### Покрытие:
- Покрытие тестами 80% кода.
- Использованы фикстуры для создания тестовых данных и параметризация для тестирования различных сценариев.
