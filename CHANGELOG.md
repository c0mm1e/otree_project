[TOC]

# 更新日志 Change Log

#### 2024/11/20	Version 2.0

- 已将项目部署至腾讯云服务器。
  - The project has been deployed to Tencent Cloud server.


#### 2024/11/20	Version 1.2

- 修改所有聊天页面（`chat_control`应用中4个，`chat_experimental`应用中2个）的倒计时逻辑和显示文本，将倒计时相关变量存储在服务器端。
  - Modify the countdown logic and display text of all chat pages (4 in the `chat_control` application, 2 in the `chat_experimental` application), and implement countdown-related variables stored on the server side.

- 修复了`pre_survey`应用中页面不能正确显示整个部分的限时的错误。
  - Fixed a bug where the page in the `pre_survey` application did not correctly display the time limit for the entire application. 

- 向`chat_control`应用和`chat_experimental`应用中的导言部分加入了一定时间内隐藏“下一页”按钮逻辑。（详见`HIDE_NEXT_BUTTON_SECONDS`）
  - Added logic to hide the "next page" button for a certain period of time to the introduction part of the `chat_control` application and the `chat_experimental` application. (See `HIDE_NEXT_BUTTON_SECONDS` for details)

- 将`chat_control`应用中，专家的两个聊天页面的填空题（填写自己的创意的文本框）`brainstorm_idea_expert`和`elaboration_idea_expert`移动到各自后面新建的页面`BrainstromExpertUpload`和`ElaborationExpertUpload`。
  - Move the questions (text boxes for filling in experts' own ideas) `brainstorm_idea_expert` and `elaboration_idea_expert` on two chat pages of experts in the `chat_control` application to the newly created pages behind them: `BrainstromExpertUpload` and `ElaborationExpertUpload`.


#### 2024/11/20	Version 1.1

- 更改用户分配到的角色的显示文本（`参赛者`和`专家`分别改为`角色1`和`角色2`）。
  - Changed the display text of roles assigned to users (`参赛者` and `专家` were changed to `角色1` and `角色2` respectively).

- 将`chat_control`应用中专家的两个聊天页面`BrainstormExpert`和`ElaborationExpert`加入“智谱清言”AI的网页链接。
  - Add the web links of the "Zhipu Qingyan" AI to the two chat pages `BrainstormExpert` and `ElaborationExpert` of the experts in the `chat_control` application. 

- 将`chat_control`应用中的`ChatControlIntroContestant`、`ChatControlIntroExpert`、`BrainstormIntroContestant`和`BrainstormIntroExpert`四个页面的内容移动到对应的`BrainstormContestant`和`BrainstormExpert`两个聊天页面，并删除前四个页面。
  - Move the contents of the four pages `ChatControlIntroContestant`, `ChatControlIntroExpert`, `BrainstormIntroContestant` and `BrainstormIntroExpert` in the `chat_control` application to two chat pages `BrainstormContestant` and `BrainstormExpert` respectively, and delete the four pages. 

- 将`chat_experimental`应用中的`ChatExperimentalIntroContestant`和`BrainstormIntroContestant`两个页面的内容移动到对应的`BrainstormExpert`聊天页面，并删除前两个页面。
  - Move the contents of the two pages `ChatExperimentalIntroContestant` and `BrainstormIntroContestant` in the `chat_experimental` application to the corresponding chat page `BrainstormExpert`, and delete the two pages.

- 在`chat_control`应用中新建一个页面`ExpertAIDialogueUpload`供专家提交与AI的对话文本。
  - Create a new page `ExpertAIDialogueUpload` in the `chat_control` application for experts to submit dialogue texts with AI. 

- 在两个提交与AI的对话文本的页面加入提示文本，引导欲提交图片的用户。
  - Add prompt text to the two pages for submitting dialogue text with AI to guide users who want to submit pictures. 

- 将两次聊天页面的限时分开设置（见`BRAINSTORM_TIMEOUT_SECONDS`和`ELABORATION_TIMEOUT_SECONDS`）。
  - Set the time limits of the two chat pages separately (see `BRAINSTORM_TIMEOUT_SECONDS` and `ELABORATION_TIMEOUT_SECONDS`). 


#### 2024/11/18	Version 1.0

- 实现了基本框架。
  - Implemented the basic framework.