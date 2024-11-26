import sys
sys.path.append("..") 
from my_constants import *

def question_group_generator(template: str, length: int):
    """
    :param template: 字符串模板，使用`{}`占位符标记动态部分。
    :param length: 动态部分的数字索引范围（从1到length）。
    :return: 动态字段组成的列表。
    """
    return [
        template.format(index)
        for index in range(1, length + 1)
    ]

# 预问卷问题组
pre_survey_length_dict = {
    # page : the number of questions
    3:10,
    5:8,
    6:5,
    7:16,
    8:4,
    9:12,
    10:10,
    11:5,
}
for page, length in pre_survey_length_dict.items():
    group_name = f'QUESTION_GROUP_PreP{page}'
    globals()[group_name] = question_group_generator(f'pre_p{page}_q{{}}', length)

QUESTION_GROUP_PreP12 = [
    'name', 
    'student_id', 
    'gender', 
    'age', 
    'grade', 
    'major',
]


# 头脑风暴问题组 参赛者 20个
BRAINSTORM_IDEAS_GROUP = question_group_generator('brainstorm_idea_{}', 20)
# 头脑风暴问题组 专家 1个
BRAINSTORM_IDEA_EXPERT_GROUP = [
    'brainstorm_idea_expert',
]


# 头脑风暴问题评估组 参赛者
# 遍历生成每个idea组，并存储到全局变量中
for idea_index in range(1, 20 + 1):
    group_name = f'BRAINSTORM_IDEA{idea_index}_EVALUATION_GROUP'  # 动态变量名
    globals()[group_name] = [
        f'brainstorm_idea{idea_index}_evaluation_{category}_{index}'
        for category in ['useful', 'novel']
        for index in range(1, 3 + 1)
    ]
    
# 头脑风暴创意选择 参赛者  
IDEA_CHOOSE_BEST1 = [
    'idea_choose_best'
]
IDEA_CHOOSE_BEST2 = [
    'idea_choose_reason',
    'idea_choose_confident1',
    'idea_choose_confident2',
    'idea_choose_confident3',
    'idea_choose_confident4',
]
  
# 头脑风暴问题评估组 专家
BRAINSTORM_IDEA_EVALUATION_EXPERT_GROUP = [
    f'brainstorm_idea_evaluation_expert_{category}_{index}'
    for category in ['useful', 'novel']
    for index in range(1, 3 + 1)
]


# Mid Survey
# 实验中问卷问题组
mid_survey_length_dict = {
    # page : the number of questions
    1:4,
    2:9,
    # page 3 is a slider
    4:4,
    5:3,
}
for page, length in mid_survey_length_dict.items():
    group_name = f'QUESTION_GROUP_MidP{page}'
    globals()[group_name] = question_group_generator(f'mid_p{page}_q{{}}', length)

QUESTION_GROUP_MidP3 = [
    'mid_p3_slider', 
]


# 创意完善 （各填1个空）
ELABORATION_IDEA_CONTESTANT_GROUP = [
    'elaboration_idea_contestant',
]
ELABORATION_IDEA_EXPERT_GROUP = [
    'elaboration_idea_expert',
]

# 对完善后的最终创意评估
ELABORATION_IDEA_EVALUATION_GROUP = [
    f'elaboration_idea_evaluation_{category}_{index}'
    for category in ['useful', 'novel']
    for index in range(1, 3 + 1)
]

# 参赛者 需要多回答的一个问题（Confident）
ELABORATION_CONTESTANT_CONFIDENT_GROUP = [
    'elaboration_contestant_confident',
]

# 专家 提前回答是否累
EXPERT_TIRED_GROUP = question_group_generator('expert_tired_{}', 4)

# 对照组专家 和 实验组参赛者 的额外步骤：提交与AI的对话
AI_DIALOGUE_UPLOAD_GROUP = [
    'ai_dialogue_upload',
]


# 后续问题组
post_survey_length_dict = {
    # page : the number of questions
    2:4,
    3:9,
    # page 4 is a slider
    5:3,
    6:4,
    7:4,
    8:5,
    9:4,
    10:2,
    11:3,
    12:7,
    13:4,
}
for page, length in post_survey_length_dict.items():
    group_name = f'QUESTION_GROUP_PostP{page}'
    globals()[group_name] = question_group_generator(f'post_p{page}_q{{}}', length)

QUESTION_GROUP_PostP4 = [
    'post_p4_slider', 
    'post_p4_choice',
]


# Demographic Information
# 1. Demographic Information 参赛者    
QUESTION_GROUP_DemoInfoContestant = [
    'demo_cont_q1', 
    'demo_cont_q2', 
    'demo_cont_q3',
]

# 2. Demographic Information 专家
QUESTION_GROUP_DemoInfoExpert = [
    'demo_exp_q1', 
    'demo_exp_q2', 
    'demo_exp_q3',
]

# 3. Demographic Information 共同问题
QUESTION_GROUP_AI_Question1 = [
    'demo_ai_q1',
]

QUESTION_GROUP_AI_Question2 = [
    'ai_tool_chat', 
    'ai_tool_code',
    'ai_tool_image',
    'ai_tool_translate',
    'ai_tool_other',
] # Only displayed while Question1 got answer 'Yes'

QUESTION_GROUP_AI_Question3 = [
    'demo_ai_q3',
] # Only displayed while Question1 got answer 'Yes'

QUESTION_GROUP_DemoInfo5 = [
    'demo_p5_q1',
    'demo_p5_q2',
] # final update 







# Likert answer group
LIKERT_ANSWER_GROUP = [
    [1, '非常不同意'], 
    [2, '不同意'], 
    [3, '有点不同意'], 
    [4, '一般'], 
    [5, '有点同意'], 
    [6, '同意'], 
    [7, '非常同意'],
]

POSSIBILITY_ANSWER_GROUP = [
    [1, '非常不可能'],
    [2, '不可能'],
    [3, '中立'],
    [4, '可能'],
    [5, '非常可能'],
]

GENDER_GROUP = [
    ['F','女'], 
    ['M','男'],
]

GRADE_GROUP = [
    [21,'2021级'], 
    [22,'2022级'], 
    [23,'2023级'], 
    [24,'2024级'], 
    [-1,'其他'],
]



# Questions about Useful & Novel
USEFUL_QUESTION_GROUP = [
    '这个想法很实用',
    '这个想法有助于解决用户的问题',
    '这个想法针对问题提出了切实可行的解决方案',
]
NOVEL_QUESTION_GROUP = [
    '这个想法是原创的',
    '这个想法是一种解决问题的新方法',
    '这个想法是一个突破性的想法',
]


# Mid 和 Post 两次评价提交的创意
BELONGING_QUESTION_GROUP = [
    '我对这个创意有很强的个人归属感', 
    '这是我的创意',
    '我觉得这个创意是属于我的',
    '我觉得这是我的创意',
] # mid1 & post2
AUTHOR_QUESTION_GROUP = [
    '我是这个创意内容的主要贡献者',
    '我对这个创意的内容做出了实质性的贡献',
    '我起草了这个创意',
    '我对这个创意进行了关键性的修改',
    '我已最终批准将这个创意上传',
    '我对这个创意的各个方面负有责任',
    '我至少对部分文本负责',
    '我的名字应该出现在这个创意下面',
    '我觉得我是这个创意的作者',
] # mid2 & post3

# Mid 和 Post 两次评价讨论对象
UNIQUE_QUESTION_GROUP = [
    '我的讨论对象在任务中提供了独特的信息',
    '我的讨论对象和我通过开放分享彼此的知识互补',
    '我的讨论对象仔细考虑了所有观点，努力提出最佳解决方案',
    '我的讨论对象仔细考虑了我提供的独特信息',
] # mid4 & post6
SOON_QUESTION_GROUP = [
    '很快，我的讨论对象在创造性任务中的地位会比我高',
    '很快，我的讨论对象在创造性任务中知名度会比我高',
    '很快，我的讨论对象在创造性任务中会得到比我更高的钦佩',    
] # mid5 & post11

# 在后半部分询问用户是否累
# 参赛者 出现在post最后一页
# 专家 出现在elaboration最后一页（专家没有post）
TIRED_QUESTION_GROUP = [
    '此刻我感到非常疲惫',
    '此刻我感到非常疲倦',
    '此刻我感到精疲力竭',
    '此刻我感到精力充沛',
]