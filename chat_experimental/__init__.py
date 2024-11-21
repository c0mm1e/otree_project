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
对于实验组的参赛者，
这是一个单人实验。
没有等待页面，没有 专家 角色。
"""


class C(BaseConstants):
    NAME_IN_URL = 'chat_experimental'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    BRAINSTORM_TIMEOUT_SECONDS = BRAINSTORM_TIMEOUT_SECONDS
    ELABORATION_TIMEOUT_SECONDS = ELABORATION_TIMEOUT_SECONDS
    
    CONTESTANT_ROLE = CONTESTANT_ROLE


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # question list
    if True:
        # 20 brainstorm ideas
        # The first 10 are required
        brainstorm_idea_1 = make_field_longstring(False, idea_text(1))
        brainstorm_idea_2 = make_field_longstring(True, idea_text(2))
        brainstorm_idea_3 = make_field_longstring(True, idea_text(3))
        brainstorm_idea_4 = make_field_longstring(True, idea_text(4))
        brainstorm_idea_5 = make_field_longstring(True, idea_text(5))
        brainstorm_idea_6 = make_field_longstring(True, idea_text(6))
        brainstorm_idea_7 = make_field_longstring(True, idea_text(7))
        brainstorm_idea_8 = make_field_longstring(True, idea_text(8))
        brainstorm_idea_9 = make_field_longstring(True, idea_text(9))
        brainstorm_idea_10 = make_field_longstring(True, idea_text(10))
        # The last 10 are optional
        brainstorm_idea_11 = make_field_longstring(True, idea_text(11))
        brainstorm_idea_12 = make_field_longstring(True, idea_text(12))
        brainstorm_idea_13 = make_field_longstring(True, idea_text(13))
        brainstorm_idea_14 = make_field_longstring(True, idea_text(14))
        brainstorm_idea_15 = make_field_longstring(True, idea_text(15))
        brainstorm_idea_16 = make_field_longstring(True, idea_text(16))
        brainstorm_idea_17 = make_field_longstring(True, idea_text(17))
        brainstorm_idea_18 = make_field_longstring(True, idea_text(18))
        brainstorm_idea_19 = make_field_longstring(True, idea_text(19))
        brainstorm_idea_20 = make_field_longstring(True, idea_text(20))

        # evaluation
        brainstorm_idea1_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea1_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea1_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea1_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea1_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea1_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea2_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea2_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea2_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea2_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea2_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea2_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea3_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea3_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea3_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea3_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea3_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea3_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea4_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea4_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea4_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea4_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea4_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea4_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea5_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea5_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea5_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea5_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea5_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea5_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea6_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea6_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea6_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea6_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea6_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea6_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea7_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea7_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea7_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea7_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea7_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea7_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea8_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea8_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea8_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea8_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea8_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea8_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea9_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea9_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea9_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea9_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea9_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea9_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea10_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea10_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea10_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea10_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea10_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea10_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea11_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea11_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea11_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea11_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea11_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea11_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea12_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea12_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea12_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea12_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea12_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea12_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea13_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea13_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea13_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea13_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea13_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea13_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea14_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea14_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea14_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea14_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea14_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea14_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea15_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea15_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea15_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea15_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea15_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea15_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea16_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea16_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea16_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea16_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea16_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea16_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        brainstorm_idea17_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea17_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea17_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea17_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea17_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea17_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])    
        
        brainstorm_idea18_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea18_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea18_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea18_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea18_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea18_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])   
        
        brainstorm_idea19_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea19_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea19_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea19_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea19_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea19_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])    
        
        brainstorm_idea20_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        brainstorm_idea20_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        brainstorm_idea20_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        brainstorm_idea20_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        brainstorm_idea20_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        brainstorm_idea20_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])
        
        # idea choose best contestant
        idea_choose_best = models.IntegerField(label='')
        
        idea_choose_reason = make_field_longstring(
            False, '您选择提交该创意的理由是：（为什么选择该项创意而放弃了其他创意）',
        )
        idea_choose_confident1 = make_field_likert('总体来说，我对我生成的创意很有信心')
        idea_choose_confident2 = make_field_likert('总体来说，我对我生成的创意很满意')
        idea_choose_confident3 = make_field_likert('总体来说，我认为我生成的创意很有潜力')
        idea_choose_confident4 = make_field_confident()
           
                   
        # Mid Survey Page1
        mid_p1_q1 = make_field_likert(BELONGING_QUESTION_GROUP[0])
        mid_p1_q2 = make_field_likert(BELONGING_QUESTION_GROUP[1])
        mid_p1_q3 = make_field_likert(BELONGING_QUESTION_GROUP[2])
        mid_p1_q4 = make_field_likert(BELONGING_QUESTION_GROUP[3])
        
        # Mid Survey Page2
        mid_p2_q1 = make_field_likert(AUTHOR_QUESTION_GROUP[0])
        mid_p2_q2 = make_field_likert(AUTHOR_QUESTION_GROUP[1])
        mid_p2_q3 = make_field_likert(AUTHOR_QUESTION_GROUP[2])
        mid_p2_q4 = make_field_likert(AUTHOR_QUESTION_GROUP[3])
        mid_p2_q5 = make_field_likert(AUTHOR_QUESTION_GROUP[4])
        mid_p2_q6 = make_field_likert(AUTHOR_QUESTION_GROUP[5])
        mid_p2_q7 = make_field_likert(AUTHOR_QUESTION_GROUP[6])
        mid_p2_q8 = make_field_likert(AUTHOR_QUESTION_GROUP[7])
        mid_p2_q9 = make_field_likert(AUTHOR_QUESTION_GROUP[8])
        
        # Mid Survey Page3
        mid_p3_slider = models.IntegerField(
            min=-50,
            max=50,
        )
        
        # Mid Survey Page4
        mid_p4_q1 = make_field_likert(UNIQUE_QUESTION_GROUP[0])
        mid_p4_q2 = make_field_likert(UNIQUE_QUESTION_GROUP[1])
        mid_p4_q3 = make_field_likert(UNIQUE_QUESTION_GROUP[2])
        mid_p4_q4 = make_field_likert(UNIQUE_QUESTION_GROUP[3])
        
        # Mid Survey Page5
        mid_p5_q1 = make_field_likert(SOON_QUESTION_GROUP[0])
        mid_p5_q2 = make_field_likert(SOON_QUESTION_GROUP[1])
        mid_p5_q3 = make_field_likert(SOON_QUESTION_GROUP[2])
        
        # 创意完善
        elaboration_idea_contestant = make_field_longstring(
            False, '请在下面输入您完善后的创意内容：'
        )
        
        # 对完善后的最终创意评估
        elaboration_idea_evaluation_useful_1 = make_field_likert(USEFUL_QUESTION_GROUP[0])
        elaboration_idea_evaluation_useful_2 = make_field_likert(USEFUL_QUESTION_GROUP[1])
        elaboration_idea_evaluation_useful_3 = make_field_likert(USEFUL_QUESTION_GROUP[2])
        elaboration_idea_evaluation_novel_1 = make_field_likert(NOVEL_QUESTION_GROUP[0])
        elaboration_idea_evaluation_novel_2 = make_field_likert(NOVEL_QUESTION_GROUP[1])
        elaboration_idea_evaluation_novel_3 = make_field_likert(NOVEL_QUESTION_GROUP[2])        
        
        # 参赛者 需要多回答的一个问题（Confident）
        elaboration_contestant_confident = make_field_confident()
        
        # 实验组 提交 对话文本
        ai_dialogue_upload = make_field_longstring()
        
        
        
        
# PAGES
if True:
    class ChatExperimentalIntro1(Page):
        # 所有玩家都看到的通用介绍页面
        # 传递角色信息至参与人层级
        def before_next_page(player, timeout_happened=False):
            # 将当前玩家的角色保存到 participant.vars
            player.participant.role_in_chat = player.role


    class ChatExperimentalIntro2(Page):
        # 所有玩家都看到的通用介绍页面
        # 一段时间后再显示下一页按钮
        @staticmethod
        def js_vars(player):
            return{
                'timestamp': int(time.time() + HIDE_NEXT_BUTTON_SECONDS),
            }


    # 聊天房间，30分钟限时
    class BrainstormContestant(Page):
        
        form_model = 'player'
        form_fields = BRAINSTORM_IDEAS_GROUP
        
        is_displayed = is_contestant
    
        def vars_for_template(player):
            # 传递 网站链接 到模板
            return {
                'ai_website': AI_WEBSITE,
            }
        @staticmethod
        def js_vars(player):
            return{
                'timestamp': int(time.time() + BRAINSTORM_TIMEOUT_SECONDS),
            }
            


    class ContestantEvaluationIntro(Page):
        is_displayed = is_contestant



    # 20个参赛者评估页面
    if True:
        # 参赛者评估页面1
        class ContestantEvaluation1(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA1_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_1)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_1.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面2
        class ContestantEvaluation2(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA2_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_2)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_2.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面3
        class ContestantEvaluation3(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA3_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_3)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_3.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面4
        class ContestantEvaluation4(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA4_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_4)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_4.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面5
        class ContestantEvaluation5(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA5_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_5)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_5.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面6
        class ContestantEvaluation6(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA6_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_6)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_6.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面7
        class ContestantEvaluation7(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA7_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_7)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_7.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面8
        class ContestantEvaluation8(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA8_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_8)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_8.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面9
        class ContestantEvaluation9(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA9_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_9)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_9.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面10
        class ContestantEvaluation10(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA10_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_10)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_10.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面11
        class ContestantEvaluation11(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA11_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_11)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_11.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面12
        class ContestantEvaluation12(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA12_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_12)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_12.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面13
        class ContestantEvaluation13(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA13_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_13)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_13.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面14
        class ContestantEvaluation14(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA14_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_14)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_14.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面15
        class ContestantEvaluation15(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA15_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_15)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_15.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面16
        class ContestantEvaluation16(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA16_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_16)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_16.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面17
        class ContestantEvaluation17(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA17_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_17)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_17.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面18
        class ContestantEvaluation18(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA18_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_18)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_18.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面19
        class ContestantEvaluation19(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA19_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_19)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_19.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


        # 参赛者评估页面20
        class ContestantEvaluation20(Page):
            form_model = 'player'
            form_fields = BRAINSTORM_IDEA20_EVALUATION_GROUP

            def is_displayed(player):
                return is_right_role_and_idea(player, C.CONTESTANT_ROLE, player.brainstorm_idea_20)
            def vars_for_template(player):
                # 动态传递 brainstorm_idea 内容到模板
                return {
                    'idea_content': player.brainstorm_idea_20.split('\n'),
                }
            def get_context_data(self, **kwargs):
                return get_likert_answer(super().get_context_data, **kwargs)


    # 头脑风暴创意选择 参赛者  
    class ContestantChooseBest1(Page):
        form_model = 'player'
        form_fields = IDEA_CHOOSE_BEST1

        is_displayed = is_contestant
        
        def vars_for_template(player):
            idea_not_none_index = [
                index for index in range(1, 21)
                if idea_is_exist(player, index)
            ]
            ideas_content = [
                ['创意{}：'.format(index)] + getattr(player, f'brainstorm_idea_{index}').split('\n') + ['']
                for index in idea_not_none_index
            ]
            return {
                'ideas_content': ideas_content,
            }
        @staticmethod
        def error_message(player, values):
            error_messages = dict()
            if not 1 <= values['idea_choose_best'] <= 20:
                error_messages['idea_choose_best'] = '请填写1~20之间的整数。'
            elif not idea_is_exist(player, values['idea_choose_best']):
                error_messages['idea_choose_best'] = '请选择一个您已填写的创意。'
            return error_messages            


    class ContestantChooseBest2(Page):
        form_model = 'player'
        form_fields = IDEA_CHOOSE_BEST2

        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        is_displayed = is_contestant
        
        def vars_for_template(player):
            index = player.idea_choose_best   
            idea_content = getattr(player, f'brainstorm_idea_{index}').split('\n')
            return {
                'index': index,
                'idea_content': idea_content,
            }
        


    # MidSurvey
    # 第一页，共同显示
    class MidSurveyPage1Mutual(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_MidP1

        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)        

       
    # 第二页，共同显示
    class MidSurveyPage2Mutual(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_MidP2

        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        
    # 第三页，共同显示
    class MidSurveyPage3Mutual(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_MidP3
        
        
    # 第四页，仅限参赛者查看
    class MidSurveyPage4Contestant(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_MidP4

        is_displayed = is_contestant
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
        
    # 第五页，仅限参赛者查看
    class MidSurveyPage5Contestant(Page):
        form_model = 'player'
        form_fields = QUESTION_GROUP_MidP5
        
        is_displayed = is_contestant

        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)

    
    # 第二次聊天房间，30分钟限时
    class ElaborationContestant(Page):
        form_model = 'player'
        form_fields = ELABORATION_IDEA_CONTESTANT_GROUP
        
        is_displayed = is_contestant

        def vars_for_template(player):
            # index = player.idea_choose_best   
            # debug
            index = player.field_maybe_none('idea_choose_best') if player.field_maybe_none('idea_choose_best') else 1
            old_idea_content = getattr(player, f'brainstorm_idea_{index}').split('\n')
            return {
                'ai_website': AI_WEBSITE,
                'old_idea_content': old_idea_content,
            }
        @staticmethod
        def js_vars(player):
            return{
                'timestamp': int(time.time() + ELABORATION_TIMEOUT_SECONDS),
            }



    # Useful/Novel 的问题
    class ElaborationEvaluation1(Page):
        form_model = 'player'
        form_fields = ELABORATION_IDEA_EVALUATION_GROUP

        is_displayed = is_contestant
        
        def vars_for_template(player):
            elaboration_idea = player.elaboration_idea_contestant
            return {
                'idea_content': elaboration_idea.split('\n'),
            }
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)
        
    
    # Confident 的问题，仅参赛者回答
    class ElaborationEvaluation2(Page):
        form_model = 'player'
        form_fields = ELABORATION_CONTESTANT_CONFIDENT_GROUP   
        
        is_displayed = is_contestant
        
        def get_context_data(self, **kwargs):
            return get_likert_answer(super().get_context_data, **kwargs)   


    class AIDialogueUpload(Page):
        form_model = 'player'
        form_fields = AI_DIALOGUE_UPLOAD_GROUP  


page_sequence = [
    # 导言（不需要在做完Pre后等待）
    ChatExperimentalIntro1, 
    ChatExperimentalIntro2, 
    # 头脑风暴聊天页面（在外部与AI聊天）
    BrainstormContestant, 
    # 参赛者评估+选择
    ContestantEvaluationIntro,
    ContestantEvaluation1,
    ContestantEvaluation2,
    ContestantEvaluation3,
    ContestantEvaluation4,
    ContestantEvaluation5,
    ContestantEvaluation6,
    ContestantEvaluation7,
    ContestantEvaluation8,
    ContestantEvaluation9,
    ContestantEvaluation10,
    ContestantEvaluation11,
    ContestantEvaluation12,
    ContestantEvaluation13,
    ContestantEvaluation14,
    ContestantEvaluation15,
    ContestantEvaluation16,
    ContestantEvaluation17,
    ContestantEvaluation18,
    ContestantEvaluation19,
    ContestantEvaluation20,
    ContestantChooseBest1,
    ContestantChooseBest2,
    # MidSurvey
    MidSurveyPage1Mutual,
    MidSurveyPage2Mutual,
    MidSurveyPage3Mutual,
    MidSurveyPage4Contestant,
    MidSurveyPage5Contestant,
    # 创意完善
    ElaborationContestant,
    ElaborationEvaluation1,
    ElaborationEvaluation2,
    # 提交与AI的对话
    AIDialogueUpload,
]