# -*- coding: utf-8 -*-

ITEM_COUNT_IN_PAGE = 10

TIME_NUMBER_CONVERTER = {
    '오전':0,
    '오후':1,
    '저녁':2
}
WEEKDAY_NUMBER_CONVERTER = {
    'Mon':0,
    'Tue':1,
    'Wed':2,
    'Thu':3,
    'Fri':4,
    'Sat':5,
    'Sun':6,
    0:'Mon',
    1:'Tue',
    2:'Wed',
    3:'Thu',
    4:'Fri',
    5:'Sat',
    6:'Sun'
}

RESPONSE_STR_SUCCESS = 'success'
RESPONSE_STR_FAIL = 'fail'

ERROR_PASSWORD_CONFIRM_NOT_IDENTICAL = 'password confirm not identical'
CODE_ERROR_PASSWORD_CONFIRM_NOT_IDENTICAL = 1

ERROR_USERNAME_MUST_BE_SET = 'username must be set'
CODE_ERROR_USERNAME_MUST_BE_SET = 2

ERROR_ALREADY_EXIST_USERNAME = 'already exsit username'
CODE_ERROR_ALREADY_EXIST_USERNAME = 3

ERROR_NOT_EXIST_ID = 'id does not exist'
CODE_ERROR_NOT_EXIST_ID = 4

ERROR_PASSWORD_NOT_CORRECT = 'password not correct'
CODE_ERROR_PASSWORD_NOT_CORRECT = 5

ERROR_NOT_ACTIVE_USER = 'not active user'
CODE_ERROR_NOT_ACTIVE_USER = 6

ERROR_HAVE_TO_LOGIN = 'have to login'
CODE_ERROR_HAVE_TO_LOGIN = 7

ERROR_DATA_INPUT_FORMAT_NOT_CORRECT = 'data input format not correct'
CODE_ERROR_DATA_INPUT_FORMAT_NOT_CORRECT = 8

ERROR_CLASSES_INQUIRE_FAIL = 'classes inquire fail'
CODE_ERROR_CLASSES_INQUIRE_FAIL = 9

ERROR_CATEGORY_NAME_DOES_NOT_EXIST = 'category name does not exist'
CODE_ERROR_CATEGORY_NAME_DOES_NOT_EXIST = 10

ERROR_SUBCATEGORY_NAME_DOES_NOT_EXIST = 'subcategory name does not exist'
CODE_ERROR_SUBCATEGORY_NAME_DOES_NOT_EXIST = 11