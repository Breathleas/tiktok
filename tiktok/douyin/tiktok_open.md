## 抖音公开接口

api|type|描述
---|---|---
https://open.douyin.com/oauth/userinfo/|GET|用来获取用户的基本信息

请求参数

access_token （string）

    调用/oauth/access_token/生成的token，此token需要用户授权。

open_id （string）
    
    通过/oauth/access_token/获取，用户唯一标志

返回

Responses （application/json）

    {
      "data": {
        "error_code": 0,
        "description": "",错误码描述
        "open_id": "0da22181-d833-447f-995f-1beefea5bef3",用户在当前应用的唯一标识
        "union_id": "1ad4e099-4a0c-47d1-a410-bffb4f2f64a4",用户在当前开发者账号下的唯一标识（未绑定开发者账号没有该字段）
        "nickname": "张伟",
        "avatar": "https://example.com/x.jpeg",
        "city": "上海",
        "province": "上海",
        "country": "中国",
        "gender": 0
      }
    }
    
api|type|描述
---|---|---
https://open.douyin.com/fans​/list​/|GET|获取用户最近的粉丝列表

Parameters

Name|Description
---|---
open_id string |通过/oauth/access_token/获取，用户唯一标志
access_token string|调用/oauth/access_token/生成的token，此token需要用户授权。
cursor integer|分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。
count integer  |每页数量

Responses

    {
      "data": {
        "error_code": 0,
        "description": "",
        "cursor": 0,
        "has_more": false,
        "list": [
          {
            "open_id": "0da22181-d833-447f-995f-1beefea5bef3",
            "union_id": "1ad4e099-4a0c-47d1-a410-bffb4f2f64a4",
            "nickname": "张伟",
            "avatar": "https://example.com/x.jpeg",
            "city": "上海",
            "province": "上海",
            "country": "中国",
            "gender": 0
          }
        ]
      }
    }

api|type|描述
---|---|---
https://open.douyin.com​/following​/list​/|GET|获取关注列表


Parameters

Name|Description
---|---
open_id *string|通过/oauth/access_token/获取，用户唯一标志
access_token *string|调用/oauth/access_token/生成的token，此token需要用户授权。
cursor integer|分页游标, 第一页请求cursor是0, response中会返回下一页请求用到的cursor, 同时response还会返回has_more来表明是否有更多的数据。
count *integer|每页数量

Responses

code=200

Description

    {
      "data": {
        "error_code": 0,
        "description": "",错误码描述
        "cursor": 0,用于下一页请求的cursor
        "has_more": false,
        "list": [
          {
            "open_id": "0da22181-d833-447f-995f-1beefea5bef3",用户在当前应用的唯一标识
            "union_id": "1ad4e099-4a0c-47d1-a410-bffb4f2f64a4",用户在当前开发者账号下的唯一标识（未绑定开发者账号没有该字段）
            "nickname": "张伟",
            "avatar": "https://example.com/x.jpeg",
            "city": "上海",
            "province": "上海",
            "country": "中国",
            "gender": 0,    0 - 未知
                            1 - 男性
                            2 - 女性



          }
        ]
      }
    }



api|type|描述
---|---|---
https://open.douyin.com​/fans/data/|GET|关注列表

Parameters

Name|Description
---|---
open_id *string|通过/oauth/access_token/获取，用户唯一标志
access_token *string|调用/oauth/access_token/生成的token，此token需要用户授权。


    {
      "data": {
        "error_code": 0,
        "description": "",#错误码描述
        "fans_data": {
          "all_fans_num": 10000,所有粉丝的数量
          "gender_distributions": [粉丝性别分布 item: ["1","2"] (男:1,女:2)
            {
              "item": 1,分布的种类
              "value": 6000 分布的数值
            },
            {
              "item": 2,
              "value": 4000
            }
          ],
          "age_distributions": [粉丝年龄分布 item: ["<=25","26-32","33-39","40-46",">46"]
            {
              "item": "<=25",
              "value": 5000
            },
            {
              "item": "26-32",
              "value": 3000
            },
            {
              "item": "33-39",
              "value": 1000
            },
            {
              "item": "40-46",
              "value": 600
            },
            {
              "item": ">46",
              "value": 400
            }
          ],
          "geographical_distributions": [粉丝地域分布 item: ["北京","福建","香港"...]
            {
              "item": "北京",分布的种类
              "value": 6000
            },
            {
              "item": "上海",分布的数值
              "value": 4000
            }
          ],
          "active_days_distributions": [粉丝活跃天数分布 item: ["0-1","2-5","6-10","11-31"]
            {
              "item": "0-1",
              "value": 1000
            },
            {
              "item": "2-5",
              "value": 500
            },
            {
              "item": "6-10",
              "value": 400
            },
            {
              "item": "11-31",
              "value": 300
            }
          ],
          "device_distributions": [粉丝设备分布 item: ["苹果","华为","三星","小米"...]
            {
              "item": "苹果",
              "value": 500
            },
            {
              "item": "华为",
              "value": 300
            }
          ],
          "interest_distributions": [粉丝兴趣分布 item: ["生活"","美食","旅行"...]
            {
              "item": "时尚",
              "value": 1000
            },
            {
              "item": "亲子",
              "value": 800
            },
            {
              "item": "生活",
              "value": 500
            }
          ],
          "flow_contributions": [粉丝流量贡献 flow: ["vv","like_cnt","comment_cnt","share_video_cnt"]
            {
              "flow": "vv",
              "all_sum": 1000,
              "fans_sum": 1000
            },
            {
              "flow": "like_cnt",
              "all_sum": 800,
              "fans_sum": 800
            },
            {
              "flow": "comment_cnt",
              "all_sum": 500,
              "fans_sum": 500
            },
            {
              "flow": "share_video_cnt",
              "all_sum": 300,
              "fans_sum": 300
            }
          ]
        }
      }
}