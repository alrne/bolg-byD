# 说明文档

#### 接口

localhost:5000/user/ 

localhost:5000/acc/

localhost:5000/blog/

localhost:5000/collect/

#### 接口说明

1. /user/     # 用户操作

   | 动作 | 提交方式 | key1       | key2       | key3    |
   | ---- | -------- | ---------- | ---------- | ------- |
   | 新建 | put      | username   | password   | email   |
   | 登陆 | post     | username   | password   |         |
   | 修改 | get      | [username] | [password] | [email] |
   | 删除 | delete   |            |            |         |

2. /acc/    # 邮箱激活

3. /blog/  # 博客操作

   | 动作 | 提交方式 | key1  | key2    | key3    |
   | ---- | -------- | ----- | ------- | ------- |
   | 新建 | put      | title | subject | content |
   | 修改 | get      | title | subject | content |
   | 删除 | delete   |       |         |         |

4. /collect/  # 收藏

   | 动作 | 提交方式 | key              |
   | ---- | -------- | ---------------- |
   | 收藏 | put      |                  |
   | 查找 | get      | info=[blog,user] |

   [^每一个登陆或者操作博客都会将当前userid或blog.id 存入session，当进行收藏删除等操作时只需要对session进行读取即可进行操作。]: 
