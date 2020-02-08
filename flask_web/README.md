# 后端接口描述
## 目录结构
  *zh*
  * config 存储各种变量以及测试用的sqlite.db
  * main 启动目录
  * models 创建表,与视图相对应
  * views 主要为api接口
  * README.md 项目简介
  * requirement.txt 相关包
## 项目相关接口描述
 ### 请求路径
   #### /login
   - get请求:
      当已经登陆过,本地已经有相关cookies,就通过get请求访问此路径,
      若用户本地没有cookies,则需要进行post请求
      \
      相关参数:
      * cookies 
   - post请求:
     用户第一次登陆需要进行,在结束后会发放给用户一个cookies,
     下次登陆就可以get进入
    - 参数提交方式为from表单
    
    - 当前参数:
        * userid
        * password
   #### /registe
   - post请求:
   此方法只有post请求,为注册用,相关参数目前尚未完全确定
    - 参数提交方式为from表单
    
    - 当前参数:
        * userid 用户登陆名
        * password 用户登陆密码
        * phone 用户手机号
        * email 用户电子邮箱
        * name 用户名