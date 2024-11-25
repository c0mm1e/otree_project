from otree.api import *
import re
import sys 
import time
sys.path.append("..") 
from my_constants import *
from my_question_groups import *



# 字符串分析函数
def is_single_chinese_char(string):
    string = string.strip()
    if len(string) > 1:
        return False
    if len(string) == 0:
        return True
    return ('\u4e00' <= string <= '\u9fff')

def is_valid_name(name):
    name = name.strip()
    # 匹配英文名字
    english_regex = r"^[a-zA-Z]+([ '-][a-zA-Z]+)*$"
    # 匹配中文名字
    chinese_regex = r"^[\u4e00-\u9fff]+$"
    # 判断是否是合法的英文名字
    if re.match(english_regex, name):
        return True
    # 判断是否是合法的中文名字
    elif re.match(chinese_regex, name):
        return True
    else:
        return False
    
    
# 参赛者 填写创意    
def idea_text(index):
    return f'''请描述您的“创意{index}”，
        请在下面的文字框中，
        用示例中的格式（创意名称+
        创意概述）填写您的创意。
    '''

# make choice 部分检查idea是否存在
def idea_is_exist(player, index):
    idea_content = getattr(player, f'brainstorm_idea_{index}')
    return idea_content.strip() not in ['', None]

# make field 相关函数
# pre survey中文字词联想题目
def make_field_word_association(label=None):
    return models.StringField(
        max_length=1,
        blank=True,
        label=label,
    )
    
def make_field_likert(label=None):
    return models.IntegerField(
        widget=widgets.RadioSelect, 
        choices=LIKERT_ANSWER_GROUP, 
        label=label,
    )

def make_field_possibility(label=None):
    return models.IntegerField(
        widget=widgets.RadioSelect,
        choices=POSSIBILITY_ANSWER_GROUP,
        label=label,
    )
    
def make_field_boolean(label=None):
    return models.BooleanField(
        widget=widgets.RadioSelectHorizontal, 
        choices=[
            [True, '是'],
            [False, '否'],
        ],
        label=label, 
    )

# 头脑风暴填写创意    
def make_field_longstring(blank=False, label=''):
    return models.LongStringField(
        initial='',
        blank=blank, 
        label=label,
    )
    
# 对创意的信心调查
def make_field_confident():
    return models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, '一点信心也没有'],
            [2, '几乎没有信心'],
            [3, '有些许信心'],
            [4, '中等程度的信心'],
            [5, '有较多信心'],
            [6, '非常有信心'],
            [7, '极其有信心'],
        ],
        label='您对该创意有多少信心？',
    )
    
# 对照组和实验组的Demographic Information共同的问题
pass
    
    
# 页面函数
# 检查整个pre survey是否超时
pre_remained_text = '完成预问卷的总剩余时间为：'
def get_timeout_seconds(player):
    return player.expiry_pre - time.time()
def is_overtime(player):
    return get_timeout_seconds(player) > 3


# 获取当前页面的编号和总页面数量
def vars_for_page_index(
    page_sequence, 
    page_class, 
    current_offset=0,
    total_offset=0,
):
    current_page = page_sequence.index(page_class) + 1 + current_offset
    total_pages = len(page_sequence) + total_offset
    return {
        'current_page': current_page,
        'total_pages': total_pages
    }
    
# 将LIKERT_ANSWER_GROUP传给页面
def get_likert_answer(get_context_data_method, **kwargs):
    context = get_context_data_method(**kwargs)
    context['likert_answer_group'] = LIKERT_ANSWER_GROUP
    return context

# 身份相关的is_displayed包装
# 仅限参赛者阅览的页面
def is_contestant(player):
    return player.participant.role_in_chat == CONTESTANT_ROLE
# 仅限专家阅览的页面
def is_expert(player):
    return player.participant.role_in_chat == EXPERT_ROLE
# 仅限某种特定角色填空后阅览的页面
def is_right_role_and_idea(player, role, idea):
    return player.participant.role_in_chat == role and idea.strip() not in ['', None]