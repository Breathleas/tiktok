# douyin

## Fan attention

```python
'insert into tiktok.tiktok_fans_tests(user_id,fans_user_id,short_id,unique_id,json_content,date,flag)
             values ({uid},{fans.get('uid')},'{fans.get('short_id')}','{fans.get('unique_id')}',
                                '{pymysql.escape_string(json.dumps(fans, ensure_ascii=False))}',
                                {time.strftime("%Y%m%d", time.localtime())},0)'
```

- Source: mitm_fans_lsit.py
- Description:
  - 通过mitmdump进行数据包的拦截，主要数据是粉丝的信息.
- Data:
  - user_id: bigint - 网红id
  - fans_user_id : bigint - 粉丝id
  - short_id & unique_id: varchar - 搜索id(抖音号)
  - json_content: json - 截获的数据包中一条粉丝的详细信息
  - date: varchar - 爬虫日期
  - flag: 标志位
   
## comment
```python
'insert into tiktok.tiktok_comment_tests(issue_id,user_id,comment_id,search_id,
                json_content,date,flag) values ('{data.get('aweme_id')}','{use.get('uid')}','{data.get('cid','')}',
                '{use.get('short_id') if use.get('short_id') else use.get(
                    'unique_id')}','{pymysql.escape_string(json.dumps(data, ensure_ascii=False))}','{data.get(
                    'create_time')}',0)'
```

- Source: mitm_comment.py
- Description: 
  - 通过拦截评论数据包，进行分析获取评论内容.
- Data:
  - issue_id: bigint - 发布的
  - user_id: bigint - 评论人的id
  - comment_id : varchar - 评论的id
  - search_id : varchar - 搜索id
  - json_content: json - 拦截的json数据
  
## publish/user
```python
'insert into tiktok.tiktok_issue_test(user_id,issue_id,json_content,date,type,flag) values (
                                {user.get('author_user_id')},{user.get('aweme_id')},
                                '{pymysql.escape_string(json.dumps(user, ensure_ascii=False))}',{time.strftime("%Y%m%d", time.localtime())},0,0)'
```

- Source: mitm_issue_user.py
- Description: 
  - 通过拦截发布数据包，获得发布的详细资料.
- Data:
  - issue_id: bigint - 发布的id
  - user_id: bigint - 网红id
  - json_content: json - 拦截的json数据

```python
'insert into tiktok.tiktok_user_test(id,`user_id`,`json_content`,`date`,`type`,`flag`) values (
                      0,{dd.get('uid')},'{pymysql.escape_string(flow.response.text)}',{time.strftime("%Y%m%d", time.localtime())},0,0)'
```

- Source: mitm_issue_user.py
- Description: 
  - 通过拦截用户数据包，获得用户的基本信息.
- Data:
  - user_id: bigint - 网红id
  - json_content: json - 拦截的json数据
  
## 每10分
         for user in json.loads(flow.response.text)['aweme_list']:
            print(user)
            insert_sql = f"""
            insert into tiktok.tiktok_new_issue(user_id,issue_id,json_content,issue_date,present_time,flag) values (
                                {user.get('author_user_id')},{user.get('aweme_id')},
                                '{pymysql.escape_string(json.dumps(user, ensure_ascii=False))}',{user.get(
                'create_time')},{int(time.time())},0)"""
            try:
                cursor.execute(insert_sql)
                connect.commit()
            except Exception as err:
                logging.error(err)

- Source: new_issue_porxy.py
- Description: 
  - 通过拦截发布数据包，获得大约最新的15条发布.
- Data:
  - user_id: bigint - 网红id
  - issue_id: bigint - 发布id
  - issue_date: bigint -发布时间
  - json_content: json - 拦截的json数据
  - present_time：bigint -爬虫时间