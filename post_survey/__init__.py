import random
from otree.api import *
import re
import time
import sys 
sys.path.append("..") 
from my_constants import *
from my_functions import *
from my_question_groups import *

author = 'Mengyen Chung, ShanghaiTech Univ.'

doc = """
Post Survey
后续问卷部分
"""
 


class C(BaseConstants):
    NAME_IN_URL = 'post_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # question list
    if True:
        # post_survey page2
        post_p2_q1 = make_field_likert(BELONGING_QUESTION_GROUP[0])
        post_p2_q2 = make_field_likert(BELONGING_QUESTION_GROUP[1])
        post_p2_q3 = make_field_likert(BELONGING_QUESTION_GROUP[2])
        post_p2_q4 = make_field_likert(BELONGING_QUESTION_GROUP[3])
        
        # post_survey page3
        post_p3_q1 = make_field_likert(AUTHOR_QUESTION_GROUP[0])
        post_p3_q2 = make_field_likert(AUTHOR_QUESTION_GROUP[1])
        post_p3_q3 = make_field_likert(AUTHOR_QUESTION_GROUP[2])
        post_p3_q4 = make_field_likert(AUTHOR_QUESTION_GROUP[3])
        post_p3_q5 = make_field_likert(AUTHOR_QUESTION_GROUP[4])
        post_p3_q6 = make_field_likert(AUTHOR_QUESTION_GROUP[5])
        post_p3_q7 = make_field_likert(AUTHOR_QUESTION_GROUP[6])
        post_p3_q8 = make_field_likert(AUTHOR_QUESTION_GROUP[7])
        post_p3_q9 = make_field_likert(AUTHOR_QUESTION_GROUP[8])
        
        # post_survey page4
        post_p4_slider = models.IntegerField(
            min=-50,
            max=50,
        )
        post_p4_choice = make_field_possibility()

        # post_survey page5
        post_p5_q1 = make_field_likert('未来我愿意与讨论对象在创意任务上合作')
        post_p5_q2 = make_field_likert('未来我会寻求与讨论对象在创意项目上的合作')
        post_p5_q3 = make_field_likert('如果有需要，我会继续与讨论对象在涉及创意的项目上合作')
    
        # post_survey page6
        post_p6_q1 = make_field_likert(UNIQUE_QUESTION_GROUP[0])
        post_p6_q2 = make_field_likert(UNIQUE_QUESTION_GROUP[1])
        post_p6_q3 = make_field_likert(UNIQUE_QUESTION_GROUP[2])
        post_p6_q4 = make_field_likert(UNIQUE_QUESTION_GROUP[3])
    
        # post_survey page7
        post_p7_q1 = make_field_likert('我会把这个想法交给竞赛主办方，以便付诸实施')
        post_p7_q2 = make_field_likert('我在与竞赛主办方交谈时会支持这个创意')
        post_p7_q3 = make_field_likert('我认为这个创意应该被实施')
        post_p7_q4 = make_field_likert('我认为这个创意是有价值的')
        
        # post_survey page8
        post_p8_q1 = make_field_likert('如果我在任务中遇到困难，我可以向我的讨论对象寻求帮助')
        post_p8_q2 = make_field_likert('我相信我的讨论对象在做与任务相关的决策时会考虑我的利益')
        post_p8_q3 = make_field_likert('我相信我的讨论对象会让我了解与我的任务相关的问题')
        post_p8_q4 = make_field_likert('我可以依赖我的讨论对象保守任务的隐私')
        post_p8_q5 = make_field_likert('我信任我的讨论对象')
        
        # post_survey page9
        post_p9_q1 = make_field_likert('我从我的讨论对象那里得到了我所需要的情感帮助和支持')
        post_p9_q2 = make_field_likert('我的讨论对象是我的安慰来源')
        post_p9_q3 = make_field_likert('我的讨论对象尽力帮助我')
        post_p9_q4 = make_field_likert('当事情出错时，我可以依靠我的讨论对象')
        
        # post_survey page10
        post_p10_q1 = make_field_likert('提供情感支持（例如，给予安慰、表达关心、积极反馈）')
        post_p10_q2 = make_field_likert('提供实际支持（例如，建议、行动方案建议、直接提供帮助）')
        
        # post_survey page11
        post_p11_q1 = make_field_likert(SOON_QUESTION_GROUP[0])
        post_p11_q2 = make_field_likert(SOON_QUESTION_GROUP[1])
        post_p11_q3 = make_field_likert(SOON_QUESTION_GROUP[2])
        
        # post_survey page12
        post_p12_q1 = make_field_likert('我和我的讨论对象看了彼此的想法')
        post_p12_q2 = make_field_likert('我和我的讨论对象公正地考虑了每个人的想法')
        post_p12_q3 = make_field_likert('在创意生成期间，我感到很放松')
        post_p12_q4 = make_field_likert('我的讨论伙伴对我的想法的反应非常批判')
        post_p12_q5 = make_field_likert('我不希望我的名字和讨论对象的某些想法关联在一起')
        post_p12_q6 = make_field_likert('我一直在想，我的讨论伙伴会批评我的想法')
        post_p12_q7 = make_field_likert('我没有发送我所有的想法，因为我不想让我的讨论对象认为我很奇怪或疯狂')

        # post_survey page13
        post_p13_q1 = make_field_likert(TIRED_QUESTION_GROUP[0])
        post_p13_q2 = make_field_likert(TIRED_QUESTION_GROUP[1])
        post_p13_q3 = make_field_likert(TIRED_QUESTION_GROUP[2])
        post_p13_q4 = make_field_likert(TIRED_QUESTION_GROUP[3])
        

# PAGES
if True:
    class PostSurveyPage1(Page):
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage1)


    class PostSurveyPage2(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP2
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage2)


    class PostSurveyPage3(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP3
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage3)


    class PostSurveyPage4(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP4
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage4)


    class PostSurveyPage5(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP5
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage5)


    class PostSurveyPage6(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP6
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage6)


    class PostSurveyPage7(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP7
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage7)


    class PostSurveyPage8(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP8
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage8)


    class PostSurveyPage9(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP9
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage9)


    class PostSurveyPage10(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP10
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage10)
        
        
    class PostSurveyPage11(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP11
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage11)
        

    class PostSurveyPage12(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP12
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage12)


    class PostSurveyPage13(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PostP13
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PostSurveyPage13)



page_sequence = [
    PostSurveyPage1, 
    PostSurveyPage2, 
    PostSurveyPage3, 
    PostSurveyPage4, 
    PostSurveyPage5, 
    PostSurveyPage6, 
    PostSurveyPage7, 
    PostSurveyPage8, 
    PostSurveyPage9, 
    PostSurveyPage10, 
    PostSurveyPage11, 
    PostSurveyPage12,
    PostSurveyPage13,
]
