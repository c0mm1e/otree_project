from os import environ
import sys 
sys.path.append("..") 
from my_constants import *

SESSION_CONFIGS = [
    dict(
        name = 'control_group',
        display_name = '实验1',
        app_sequence = ['pre_survey', 'chat_control', 'post_survey', 'demographic_information'],
        num_demo_participants = 6,
        PRE_SURVEY_TIMEOUT_SECONDS = PRE_SURVEY_TIMEOUT_SECONDS,
        HIDE_NEXT_BUTTON_SECONDS = HIDE_NEXT_BUTTON_SECONDS,
        BRAINSTORM_TIMEOUT_SECONDS = BRAINSTORM_TIMEOUT_SECONDS,
        ELABORATION_TIMEOUT_SECONDS = ELABORATION_TIMEOUT_SECONDS,
        doc = '''
            PRE_SURVEY_TIMEOUT_SECONDS：前测总限时\n
            HIDE_NEXT_BUTTON_SECONDS：实验导言部分隐藏下一页按钮时间\n
            BRAINSTORM_TIMEOUT_SECONDS：第一次聊天时间\n
            ELABORATION_TIMEOUT_SECONDS：第二次聊天时间\n
        ''', 
    ), 
    dict(
        name = 'experimental_group',
        display_name = '实验2',
        app_sequence = ['pre_survey', 'chat_experimental', 'post_survey', 'demographic_information'],
        num_demo_participants = 6,
        PRE_SURVEY_TIMEOUT_SECONDS = PRE_SURVEY_TIMEOUT_SECONDS,
        HIDE_NEXT_BUTTON_SECONDS = HIDE_NEXT_BUTTON_SECONDS,
        BRAINSTORM_TIMEOUT_SECONDS = BRAINSTORM_TIMEOUT_SECONDS,
        ELABORATION_TIMEOUT_SECONDS = ELABORATION_TIMEOUT_SECONDS,
        doc = '''
            PRE_SURVEY_TIMEOUT_SECONDS：前测总限时\n
            HIDE_NEXT_BUTTON_SECONDS：实验导言部分隐藏下一页按钮时间\n
            BRAINSTORM_TIMEOUT_SECONDS：第一次聊天时间\n
            ELABORATION_TIMEOUT_SECONDS：第二次聊天时间\n
        ''', 
    ),
    dict(
        name = 'test1', 
        display_name = '测试1 chat control',
        app_sequence = ['chat_control'],
        num_demo_participants = 6,  
        PRE_SURVEY_TIMEOUT_SECONDS = PRE_SURVEY_TIMEOUT_SECONDS,
        HIDE_NEXT_BUTTON_SECONDS = HIDE_NEXT_BUTTON_SECONDS,
        BRAINSTORM_TIMEOUT_SECONDS = BRAINSTORM_TIMEOUT_SECONDS,
        ELABORATION_TIMEOUT_SECONDS = ELABORATION_TIMEOUT_SECONDS,
        doc = '''
            PRE_SURVEY_TIMEOUT_SECONDS：前测总限时\n
            HIDE_NEXT_BUTTON_SECONDS：实验导言部分隐藏下一页按钮时间\n
            BRAINSTORM_TIMEOUT_SECONDS：第一次聊天时间\n
            ELABORATION_TIMEOUT_SECONDS：第二次聊天时间\n
        ''',       
    ),
    dict(
        name = 'test1_1', 
        display_name = '测试pre',
        app_sequence = ['pre_survey'],
        num_demo_participants = 6,        
    ),
    dict(
        name = 'test2', 
        display_name = '测试2chat exp',
        app_sequence = ['chat_experimental'],
        num_demo_participants = 6,        
    ),
    dict(
        name = 'test3', 
        display_name = '测试post',
        app_sequence = ['chat_experimental', 'post_survey', 'demographic_information'],
        num_demo_participants = 6,        
    ), 
]

ROOM = ROOMS = [
    dict(
        name='room1',
        display_name='实验房间1 周三',
        participant_label_file=
            'participant_label/participant_label_1.txt',
    ),
    dict(
        name='room2',
        display_name='实验房间2 周四',
        participant_label_file=
            'participant_label/participant_label_2.txt',
    ),
    dict(
        name='room3',
        display_name='实验房间3 周五',
        participant_label_file=
            'participant_label/participant_label_3.txt',
    ),
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'expiry', # 前测限时
    'role_in_chat', # 参与人层级的角色变量
]

SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'CNY'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '9875103396803'
