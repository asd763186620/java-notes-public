# 是什么
线程安全的高效Map集合

# 数据结构
jdk1.7底层采用分段数组+链表实现

jdk1.8与hashmap1.8的结构一样，链表+数组/红黑树

# 核心属性
jdk1.7：Segment数组（不可扩容）->HashEntry数组（可扩容）->链表

jdk.18：数据结构与hashmap一样（放弃了1.7的segment数组），但是采用了cas+synchronized来保证并发安全

# put流程
## JDK1.8
1. 通过CAS控制数组节点的添加
2. synchronized只锁定当前链表或红黑树的首节点，只要hash不冲突，就不会产生并发问题，效率提升（例如当前初始化为16的数组，一个线程通过hash的到key的下标为1，此时只使用synchronized锁下标为1的数组位，其余数组位仍然可以通过多线程访问，只有在hash值一样出现hash冲突时，才会导致多线程下的并发问题，此时多个相同的hash值的key只会有抢到synchronized锁的一个线程执行）

## JDK1.7
1. 先将map的key通过hash计算得到segment数组中的下标
2. 获取segment下标之后通过reentranlock和cas操作获取锁
    1. 获取到锁之后再次通过hash操作获取key对应的hashentry的下标将值存入，如果存在hash冲突则形成链表
    2. 获取锁失败进行自旋重试
3. 如果有多个相同key通过hash得到相同值，则也只有一个线程进行数据操作因为加了锁
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1777025246518-4aa7a05b-fae3-4c98-83f1-922ed0ec40c7.png)

