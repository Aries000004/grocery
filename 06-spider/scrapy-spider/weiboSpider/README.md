### 爬取微博博主的关注和粉丝



##### 个人信息接口分析

```shell
# 个人用户的信息 完整接口
https://m.weibo.cn/api/container/getIndex?
uid=1696587952
&luicode=10000011
&lfid=100103type%3D3%26q%3D%E9%AA%86%E6%98%8A%26t%3D0
&featurecode=20000320
&type=all
&containerid=1005051696587952

# 整理接口 简化
https://m.weibo.cn/api/container/getIndex?
uid=1195242865
&containerid=1005051195242865

```

关注接口

```shell

# 完整接口
https://m.weibo.cn/api/container/getIndex?
containerid=231051_-_followers_-_1263498570
&luicode=10000011
&lfid=1076031263498570
&featurecode=20000320
&page=2

# 简化接口
https://m.weibo.cn/api/container/getIndex?
containerid=231051_-_followers_-_1263498570
&page=2


```





粉丝详情接口

```shell

uid = 1263498570

# 完整接口
https://m.weibo.cn/api/container/getIndex?
containerid=231051_-_fans_-_1263498570
&luicode=10000011
&lfid=1076031263498570
&featurecode=20000320
&since_id=2

# 简化接口
https://m.weibo.cn/api/container/getIndex?
containerid=231051_-_fans_-_1263498570
&since_id=2  # 页码

```

