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
Pre Survey
前测问卷部分
"""




class C(BaseConstants):
    NAME_IN_URL = 'pre_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # 前测限时
    expiry_pre = models.FloatField(initial=float('inf'))
    # question list
    if True:
        # pre_survey page3
        pre_p3_q1 = make_field_word_association('1. 线索字：梦、法、象    答案字：')
        pre_p3_q2 = make_field_word_association('2. 线索字：夹、坦、休    答案字：')
        pre_p3_q3 = make_field_word_association('3. 线索字：留、宣、论    答案字：')
        pre_p3_q4 = make_field_word_association('4. 线索字：韵、望、尾    答案字：')
        pre_p3_q5 = make_field_word_association('5. 线索字：顺、方、随    答案字：')
        pre_p3_q6 = make_field_word_association('6. 线索字：历、典、营    答案字：')
        pre_p3_q7 = make_field_word_association('7. 线索字：妥、完、改    答案字：')
        pre_p3_q8 = make_field_word_association('8. 线索字：贞、劳、纵    答案字：')
        pre_p3_q9 = make_field_word_association('9. 线索字：宿、弃、得    答案字：')
        pre_p3_q10 = make_field_word_association('10. 线索字：劫、司、良    答案字：')
        
        # pre_survey page5
        pre_p5_q1 = make_field_likert('我认为我是傲慢的')
        pre_p5_q2 = make_field_likert('我认为我是果敢的')
        pre_p5_q3 = make_field_likert('我认为我是自夸的')
        pre_p5_q4 = make_field_likert('我认为我是自负的')
        pre_p5_q5 = make_field_likert('我认为我是自我主义的')
        pre_p5_q6 = make_field_likert('我认为我是自我为中心的')
        pre_p5_q7 = make_field_likert('我认为我是爱炫耀的')
        pre_p5_q8 = make_field_likert('我认为我是容易激动的')

        # pre_survey page6
        pre_p6_q1 = make_field_likert('当人们更多地了解我时，他们开始认识到我的独特之处')
        pre_p6_q2 = make_field_likert('我感到自己很特别')
        pre_p6_q3 = make_field_likert('我想不出多少能够让我与他人区分开来的特殊特质')
        pre_p6_q4 = make_field_likert('我认为我的一些特质与他人不同')
        pre_p6_q5 = make_field_likert('我觉得我的某些特质是完全独一无二的')
        
        # pre_survey page7
        pre_p7_q1 = make_field_likert('我知道自己很优秀，因为每个人都这么告诉我')
        pre_p7_q2 = make_field_likert('我喜欢成为众人瞩目的焦点')
        pre_p7_q3 = make_field_likert('我认为自己是个特别的人')
        pre_p7_q4 = make_field_likert('我喜欢支配别人')
        pre_p7_q5 = make_field_likert('我觉得操纵别人很容易')
        pre_p7_q6 = make_field_likert('我坚持要得到应有的尊重')
        pre_p7_q7 = make_field_likert('如果有机会，我很容易表现自己')
        pre_p7_q8 = make_field_likert('我总是知道自己在做什么')
        pre_p7_q9 = make_field_likert('每个人都喜欢听我讲故事')
        pre_p7_q10 = make_field_likert('我对别人的期望很高')
        pre_p7_q11 = make_field_likert('我非常喜欢成为众人瞩目的焦点')
        pre_p7_q12 = make_field_likert('人们似乎总是认可我的权威')
        pre_p7_q13 = make_field_likert('我将成为一个伟大的人')
        pre_p7_q14 = make_field_likert('我可以让任何人相信我想让他们相信的任何事情')
        pre_p7_q15 = make_field_likert('我比别人更有能力')
        pre_p7_q16 = make_field_likert('我是一个非凡的人')

        # pre_survey page8
        pre_p8_q1 = make_field_likert('我认为我很善于创新')
        pre_p8_q2 = make_field_likert('我相信自己有能力用创意去解决问题')
        pre_p8_q3 = make_field_likert('我有能力使他人的点子更加完善')
        pre_p8_q4 = make_field_likert('我很善于找到创新的方法来解决问题')

        # pre_survey page9
        pre_p9_q1 = make_field_likert('我能够用许多不同方式去交流一个想法')
        pre_p9_q2 = make_field_likert('我避免新的和不寻常的情况')
        pre_p9_q3 = make_field_likert('我觉得我永远无法做出决定')
        pre_p9_q4 = make_field_likert('我能找到可行的办法去解决那些看似无法解决的问题')
        pre_p9_q5 = make_field_likert('在决定如何表现时，我很少有选择')
        pre_p9_q6 = make_field_likert('我愿意用创造性的方法来解决问题')
        pre_p9_q7 = make_field_likert('我在任何情况下都能采取适当的行动')
        pre_p9_q8 = make_field_likert('我的行为是有意识的决定的结果')
        pre_p9_q9 = make_field_likert('我在任何情况下都有很多可能的行为方式')
        pre_p9_q10 = make_field_likert('在现实生活中，我很难运用我对某一主题的知识')
        pre_p9_q11 = make_field_likert('我愿意倾听并考虑解决问题的其它方法')
        pre_p9_q12 = make_field_likert('我有自信去尝试不同的行为方式')

        # pre_survey page10
        pre_p10_q1 = make_field_likert('我一直在寻找新的方式来改善我的生活')
        pre_p10_q2 = make_field_likert('无论我在哪里，我都有能力做出建设性的改变')
        pre_p10_q3 = make_field_likert('没有什么比看见我的想法变成现实更令人兴奋')
        pre_p10_q4 = make_field_likert('如果我看见某些我不喜欢的事情，我会改进它')
        pre_p10_q5 = make_field_likert('无论有多大的可能性，只要我有信念，我就会实现它')
        pre_p10_q6 = make_field_likert('我喜欢成为自己想法的捍卫者，即使是反对别人的意见')
        pre_p10_q7 = make_field_likert('我善于发现机会')
        pre_p10_q8 = make_field_likert('我一直在寻找更好的做事方法')
        pre_p10_q9 = make_field_likert('如果我相信一个想法，没有任何障碍能阻止我实现它')
        pre_p10_q10 = make_field_likert('我能够比别人更早发现好机会')

        # pre_survey page11
        pre_p11_q1 = make_field_likert('困难来临时，我会坚持不懈')
        pre_p11_q2 = make_field_likert('人们说我是一个即使遇到困难也能坚持到底的人')
        pre_p11_q3 = make_field_likert('即使难以理解，我也会读完一整本书直到我“搞懂”为止')
        pre_p11_q4 = make_field_likert('挫折不会使我气馁')
        pre_p11_q5 = make_field_likert('即使某事很困难，我也会努力坚持')
        
        # pre_survey page12 个人信息
        name = models.StringField(
            label='您的姓名',
        )
        student_id = models.StringField(
            label='您的学号',
        )
        gender = models.StringField(
            choices=GENDER_GROUP, 
            label='您的性别',
        )
        age = models.IntegerField(
            min=16, 
            max=100, 
            label='您的年龄',
        )
        grade = models.IntegerField(
            choices=GRADE_GROUP, 
            label='您的年级',
        )
        major = models.StringField(
            label='您的专业',
        )


# PAGES
if True:
    class PreSurveyPage1(Page):
        # 加入pre survey的20分钟限时
        @staticmethod
        def before_next_page(player, timeout_happened):
            new_expiry = time.time() + player.session.config['PRE_SURVEY_TIMEOUT_SECONDS']
            player.expiry_pre = min(new_expiry, player.expiry_pre)
            
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage1)
        
        
    class PreSurveyPage2(Page):
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage2)


    class PreSurveyPage3(Page):
        timeout_seconds = 2*60
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP3

        @staticmethod
        def error_message(player, values):
            error_messages = dict()
            for field_name in QUESTION_GROUP_PreP3:
                if not is_single_chinese_char(values[field_name]):
                    error_messages[field_name] = '请输入一个汉字。'
            return error_messages
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage3)
        
        
    class PreSurveyPage4(Page):
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage4)


    class PreSurveyPage5(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP5
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)

        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage5)


    class PreSurveyPage6(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP6
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage6)


    class PreSurveyPage7(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP7
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage7)


    class PreSurveyPage8(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP8
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage8)


    class PreSurveyPage9(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP9
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage9)


    class PreSurveyPage10(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP10
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage10)



    class PreSurveyPage11(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP11
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime
        
        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage11)


    class PreSurveyPage12(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_PreP12

        @staticmethod
        def error_message(player, values):
            error_messages = dict()
            if not is_valid_name(values['name']):
                error_messages['name'] = '请输入正确的姓名。'
            elif not values['student_id'].isdigit():
                error_messages['student_id'] = '学号应仅包含数字。'
            elif not is_valid_name(values['major']):
                error_messages['major'] = '请输入正确的专业。'
            return error_messages

        timer_text = pre_remained_text
        get_timeout_seconds = get_timeout_seconds
        is_displayed = is_overtime

        def vars_for_template(player):
            return vars_for_page_index(page_sequence, PreSurveyPage12)

    

page_sequence = [
    PreSurveyPage1, 
    PreSurveyPage2, 
    PreSurveyPage3, 
    PreSurveyPage4, 
    PreSurveyPage5, 
    PreSurveyPage6, 
    PreSurveyPage7, 
    PreSurveyPage8, 
    PreSurveyPage9, 
    PreSurveyPage10, 
    PreSurveyPage11, 
    PreSurveyPage12,
]
