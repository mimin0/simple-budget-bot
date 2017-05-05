HELP_TEXT = 'Я могу помочь тебе контролировать расходы. '\
    'Ты можешь управлять мной с помощью *следующих команд*:\n'\
    '/add - добавить запись о расходе;\n'\
    '/remove - удалить запись о расходе;\n'\
    '/change - редактировать запись о расходе;\n'\
    '/show - показать все имеющиеся данные;\n'\
    '/total - суммарный расход за все время;\n'\
    '/last - расход за последнее время;\n'\
    '/clear - удалить все старые записи;\n'\
    '/start - начать взаимодействие с ботом;\n'\
    '/help - показать справку.\n'\
    '\n'\
    'Более подробная документация на [GitHub]'\
    '(https://github.com/Evgeny-SHL/simple-budget-bot).'

WRONG_NUMBER_OF_ARGUMENTS = 'Неверное число аргументов: '\
    'ожидалось {}, принято {}.'
WRONG_NUMBER_OF_ARGUMENTS_COMMON = 'Неверное число аргументов'

UNEXPECTED_ERROR = 'Возникла неизвестная ошибка...'
BACKEND_ERROR = 'Возникла внутренняя ошибка, повторите запрос позже'

ADD_OK = 'Запись успешно добавлена.'
REMOVE_OK = 'Запись успешно удалена.'
CHANGE_OK = 'Запись успешно изменена.'
CLEAR_OK = 'Старые записи успешно удалены.'

SAY_RECORD = '[{}] {} руб. {}: {}\n'
SAY_OUTCOME = 'Всего вы потратили {} руб.'
SAY_RECENTLY = 'С {} по {} вы потратили {} руб.'
SAY_LAST_DAY = '{} вы потратили {} руб.'

NO_OUTCOME = 'Вы не вносили данных о расходах.'
EMPTY_DATABASE = 'Нет данных о расходах.'
NO_RECENT_OUTCOME = 'С {} по {} вы ничего не потратили.'
NO_LAST_DAY_OUTCOME = '{} вы ничего не потратили.'

NO_SUCH_RECORD = 'Нет записи с идентификатором {}.'

INVALID_COST = 'Стоимость должна быть положительным целым числом.'
INVALID_DATE = 'Дата указывается в формате гг-мм-дд.'
INVALID_ID = 'Идентинтификатором должно быть целое неотрицательное число.'
INVALID_NUMBER = 'Расход считается только за целое положительное число '\
    'единиц времени.'
INVALID_UNIT = 'Единица времени должна быть только дн, нед, мес (без точки '\
    'в конце).'
