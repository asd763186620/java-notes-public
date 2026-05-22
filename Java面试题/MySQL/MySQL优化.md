# 如何定位慢查询
页面加载过慢、接口压测时间长大于1秒

## 慢查询分类
1. 多表查询
2. 表中数据量过大
3. 聚合查询
4. 深度分页查询

## 定位慢查询方案
### 方案一开源工具
1. 阿尔萨斯（线上诊断工具调试工具）
2. skywalking（运维工具）
    1. <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1779444793320-9a1cc519-edd6-46e3-aab4-cc453b8d2cfc.png)
    2. <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1779444861373-c65304c3-5794-4f94-8812-65d2fc09f0dc.png)

### 方案二慢日志
1. 在项目中开启MySQL的慢日志记录功能
2. 设置慢SQL时长为2秒
3. <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1779444887870-3ef2f89f-4801-403c-918a-fea07db8fa63.png)

## 总结
1. 对接口进行测试时发现耗时较长
2. 生产环境下通过skywalking查看具体的接口以及是否因为sql执行慢，然后针对慢SQL耗时以及对应执行的sql语句，再根据sql语句查看对应代码
3. 调试环境下配置项目中的慢sql为开启状态设置时间为2秒钟，超过两秒记录到慢日志中

# 如何分析慢SQL
## 如何获取SQL语句执行信息
1. 通过EXPLAIN/DESC分析工具执行对应的sql语句获取sql执行信息
2. 使用方式：EXPLAIN SELECT * FROM USER WHERE id = 1;
3. <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1779445581484-b138d5bb-253e-4ddb-80e8-ad991d5ce508.png)

## SQL执行信息字段含义
1. type（sql语句的连接类型）
+ NULL：未查询表没有使用表
+ system：查询mysql内置的表
+ const：通过主键查询
+ eq_ref：通过主键索引或唯一索引查询
+ ref：通过唯一索引查询
+ rang：通过索引进行范围查询
+ index：通过索引查询遍历索引树
+ all：全盘扫描不经过索引
2. possible_keys：肯能用到的索引
3. key：真实使用的索引
4. key_len：使用的索引的大小
    1. <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1779445842694-14c3535b-4a26-4b77-a751-0461044bad20.png)
5. Extra：执行语句优化建议
    1. Using where；Using index ：查找使用了索引，需要的数据在索引列中可以找到，不需要回表查询
    2. Using index condition：查找使用了索引，但是需要回表查询数据
    3. <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1779445847768-c76d5d5d-5f09-4f0c-898b-b9708c290ded.png)

## 小总结
1. 通过EXPLAIN/DESC查看对应的sql语句的执行计划信息
2. 根据字段key和key_len检查是否命中了索引
3. 通过type查看sql是否有进一步的优化空间
4. 通过extra优化建议查看是否出现了回表，如果出现了回表通过添加索引或修改返回字段修复





























































