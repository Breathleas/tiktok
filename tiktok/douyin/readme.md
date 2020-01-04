#抖音问题

使用appium+模拟器+python+adb方式
##网红：

    安卓端目前可以获得5000条粉丝数据（最新的）
    ios端可以获得1000+
    点赞可以获得1000+（因为历史数据的原因，没有完全测试）
    评论可以获得1500+（因为历史数据的原因，没有完全测试）
    喜欢没有限制
    
##公共：

    安卓端目前可以获得5000条粉丝数据（最新的）
    ios端可以获得1000+
    发布的评论lsit都可以拿到
    
    
##目标：
    获取list全部信息
    
办法，反编译apk，通过反编译得出生成X-G/X-K的与get请求的url对应的方法值。
    
X-Gorgon

X-Khronos

Cookie

X-SS-REQ-TICKE

想办法通过反编译获得该字段生成的方法，和url的联系


目前代码理解：

appium+夜神模拟器+python+adb方式+fidder

步骤


    1、启动夜神模拟器
    2、启动appium
    3、启动fidder并编写js
    4、使用python脚本
    5、解析json文件。
    
代码入口：

  [douyin_get.py](douyin\douyin_get.py):整体代码文件启动前需要配置fidder的js保存数据，模拟器是都可以正确链接。
  
  [into_mysql.py](into_mysql.py):将保存下的文件user\fabu_list解析更新到数据库中，需要注意修改脚本中的入库时间。
  
  执行完成之后需要运行sql
  
    insert into tiktok_user(user_id, json_content, `date`, type, flag) select user_id,json_content,`date`,type,flag from tiktok_user_test;
    insert into tiktok_issue(user_id,issue_id, json_content, `date`, type, flag) select user_id,issue_id,json_content,`date`,type,flag from tiktok_issue_test;


  
函数名|功能介绍|注意事项
---|---|---
get_information_issue|获取网红基本信息以及发布点赞等数量|获得的数据将为json文件分别保存在user、fabu_list下
持续更行其它功能||