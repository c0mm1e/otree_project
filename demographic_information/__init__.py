import random
from otree.api import *
import re
import time
import sys 
sys.path.append("..") 
from my_functions import *
from my_question_groups import *

author = 'Mengyen Chung, ShanghaiTech Univ.'

doc = """
Demographic Information Experimental
补充问题部分
"""


class C(BaseConstants):
    NAME_IN_URL = 'demographic_information'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # question list
    if True:
        # demographic information page1 参赛者
        demo_cont_q1 = models.BooleanField(
            choices=[
                ['AI', 'AI'],
                ['Human', '人类专家'],
            ],
            widget=widgets.RadioSelectHorizontal, 
            label='在上面的创意过程中，您的讨论对象是：'
        ) 
        demo_cont_q2 = make_field_possibility('您觉得您的讨论对象是人类吗？')
        demo_cont_q3 = make_field_possibility('您觉得您的讨论对象是AI吗？')
        
        # demographic information page1 专家
        demo_exp_q1 = make_field_boolean('您的队友是否察觉出了您的回答是由AI生成的？')
        demo_exp_q2 = models.IntegerField(
            choices=[
                [1, '非常失败'],
                [2, '比较失败'],
                [3, '中立'],
                [4, '比较成功'],
                [5, '非常成功']
            ],
            widget=widgets.RadioSelect, 
            label='在整个创意过程中，您认为您在多大程度上成功隐藏了AI工具的痕迹？'
        )
        demo_exp_q3 = models.IntegerField(
            choices=[
                [1, '一点也不敏感'],
                [2, '不敏感'],
                [3, '中立'],
                [4, '敏感'],
                [5, '非常敏感']
            ],
            widget=widgets.RadioSelect, 
            label='您的队友对AI生成的内容的敏感程度有多高？'
        )
        
        # demographic information page2
        demo_ai_q1 = make_field_boolean('您平时是否使用过AI工具？（例如：ChatGPT、Kimi、智谱清言等）')
        
        # demographic information page3
        ai_tool_chat = make_field_boolean("对话生成工具（如ChatGPT，智谱清言）")
        ai_tool_code = make_field_boolean("代码生成工具（如Copilot）")
        ai_tool_image = make_field_boolean("图像生成工具 （如Midjourney, Stable Diffusion）")
        ai_tool_translate = make_field_boolean("AI翻译工具")
        
        ai_tool_other = models.StringField(
            label="其他：", 
            blank=True
        ) 
        
        # demographic information page4
        demo_ai_q3 = models.IntegerField(
            choices=[
                [5, '非常频繁，平均每天对话超过50次'],
                [4, '经常使用，平均每天对话10次至50次'],
                [3, '偶尔使用，平均每天对话少于10次'],
                [2, '很少使用，平均每周对话少于5次'],
                [1, '基本不用，平均每周内对话少于2次']
            ],
            widget=widgets.RadioSelect, 
            label='在过去的两个星期里您使用这些AI工具的频率如何？'
        )
        
        

# PAGES
if True:
    class DemoInfoExp1Contestant(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_DemoInfoContestant
        
        is_displayed = is_contestant
            
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, DemoInfoExp1Contestant, 0, -1)
        

    class DemoInfoExp1Expert(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_DemoInfoExpert

        is_displayed = is_expert   

        def vars_for_template(player):
            return vars_for_page_index(page_sequence, DemoInfoExp1Expert, -1, -1)


    class DemoInfoExp2(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_AI_Question1

        def vars_for_template(player):
            return vars_for_page_index(page_sequence, DemoInfoExp2, -1, -1)


    class DemoInfoExp3(Page):
        form_model = 'player'    
        form_fields = QUESTION_GROUP_AI_Question2
        
        def is_displayed(player):
            return player.demo_ai_q1
        
        def before_next_page(player, timeout_happened=False):
            # 如果选择了“否”，清空后两个问题的答案
            if player.demo_ai_q1 == False:
                player.ai_tool_chat = None
                player.ai_tool_code = None
                player.ai_tool_image = None
                player.ai_tool_translate = None
                player.ai_tool_other = None

        def vars_for_template(player):
            return vars_for_page_index(page_sequence, DemoInfoExp3, -1, -1)


    class DemoInfoExp4(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_AI_Question3

        def is_displayed(player):
            return player.demo_ai_q1
        
        def before_next_page(player, timeout_happened=False):
            # 如果选择了“否”，清空后两个问题的答案
            if player.demo_ai_q1 == False:
                player.demo_ai_q3 = None
    
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, DemoInfoExp4, -1, -1)


    class Fin(Page):
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, Fin, -1, -1)



page_sequence = [
    DemoInfoExp1Contestant, 
    DemoInfoExp1Expert, 
    DemoInfoExp2, 
    DemoInfoExp3,
    DemoInfoExp4,
    Fin,
]
