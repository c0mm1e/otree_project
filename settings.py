from os import environ

SESSION_CONFIGS = [
    dict(
        name = 'control_group',
        display_name = '实验1',
        app_sequence = ['pre_survey', 'chat_control', 'post_survey', 'demographic_information'],
        num_demo_participants = 6,
    ), 
    dict(
        name = 'experimental_group',
        display_name = '实验2',
        app_sequence = ['pre_survey', 'chat_experimental', 'post_survey', 'demographic_information'],
        num_demo_participants = 6,
    ),
    dict(
        name = 'test1', 
        display_name = '测试1 chat control',
        app_sequence = ['chat_control'],
        num_demo_participants = 6,        
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
