[TOC]

# 更新日志 Change Log

#### 2024/11/22	Version 2.1

- 通过将角色信息存储在参与人层级修复了实验组用户无法浏览参赛者专属页面的错误。
- 删除了`demographic_information`应用最后第二次统计个人信息的部分。

#### 2024/11/20	Version 2.0

- 已将项目部署至腾讯云服务器。


#### 2024/11/20	Version 1.2

- 修改所有聊天页面（`chat_control`应用中4个，`chat_experimental`应用中2个）的倒计时逻辑和显示文本，将倒计时相关变量存储在服务器端。
- 修复了`pre_survey`应用中页面不能正确显示整个部分的限时的错误。
- 向`chat_control`应用和`chat_experimental`应用中的导言部分加入了一定时间内隐藏“下一页”按钮逻辑。（详见`HIDE_NEXT_BUTTON_SECONDS`）
- 将`chat_control`应用中，专家的两个聊天页面的填空题（填写自己的创意的文本框）`brainstorm_idea_expert`和`elaboration_idea_expert`移动到各自后面新建的页面`BrainstromExpertUpload`和`ElaborationExpertUpload`。


#### 2024/11/20	Version 1.1

- 更改用户分配到的角色的显示文本（`参赛者`和`专家`分别改为`角色1`和`角色2`）。
- 将`chat_control`应用中专家的两个聊天页面`BrainstormExpert`和`ElaborationExpert`加入“智谱清言”AI的网页链接。
- 将`chat_control`应用中的`ChatControlIntroContestant`、`ChatControlIntroExpert`、`BrainstormIntroContestant`和`BrainstormIntroExpert`四个页面的内容移动到对应的`BrainstormContestant`和`BrainstormExpert`两个聊天页面，并删除前四个页面。
- 将`chat_experimental`应用中的`ChatExperimentalIntroContestant`和`BrainstormIntroContestant`两个页面的内容移动到对应的`BrainstormExpert`聊天页面，并删除前两个页面。
- 在`chat_control`应用中新建一个页面`ExpertAIDialogueUpload`供专家提交与AI的对话文本。
- 在两个提交与AI的对话文本的页面加入提示文本，引导欲提交图片的用户。
- 将两次聊天页面的限时分开设置（见`BRAINSTORM_TIMEOUT_SECONDS`和`ELABORATION_TIMEOUT_SECONDS`）。


#### 2024/11/18	Version 1.0

- 实现了基本框架。