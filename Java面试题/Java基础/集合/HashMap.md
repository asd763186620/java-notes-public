# 是什么
HashMap 是 Java 中基于哈希表实现的键值对集合，允许 key 为 null，非线程安全。

# 底层数据结构
+ JDK1.7：数组 + 链表（头插法）
+ JDK1.8：数组 + 链表 + 红黑树（尾插法）

优化点：

+ 避免链表过长导致 O(n)
+ 转红黑树后 → O(log n)

# 核心属性
+ 默认容量：16
+ 负载因子：0.75
+ 扩容阈值：capacity * loadFactor

# <font style="color:#DF2A3F;">为什么负载因子是0.75</font>⚠️
是基于空间和时间的平衡

如果是1的话虽然数组的利用率较高但是会导致hash冲突变多，链表变长查询变慢

如果是0.5的话虽然冲突少，但是扩容频繁浪费内存

0.75基于统计学验证

# 核心算法
hash算法

```java
hash = (h = key.hashCode()) ^ (h >>> 16)
```

作用：

+ 扰动函数，减少 hash 冲突

 寻址算法

```java
index = (n - 1) & hash
```

条件：

+ n 必须是 2 的幂

# 实现原理
添加数据时会将key进行hash运算将得到的hash值作为数组（桶）的下标，并且将value放入数组。

如果两个key的hash值相同，此时出现了hash冲突，会先判断其key的实际值是否相同如果相同则直接将后面key对应的value存入数据，如果key不同hash值相同则会通过链表的方式将value连接到上一个value

jdk1.8之后如果hash冲突过多导致hash值下标对应的链表的长度大于8并且数组长度大于64此时则会将链表转换为

# put具体流程
1.    判断 table 是否为空 → 初始化
2. 计算 hash
3.    定位桶位置
4.  判断节点：  
  •	key相同 → 覆盖  
  •	红黑树 → 树插入  
  •	链表 → 遍历
5. 链表长度 ≥8 且容量 ≥64 → 转红黑树
6.  size++ → 判断是否扩容

# HashMap扩容流程
## 当HashMap进行初始化或者扩容时会调用resize（）方法，判断数组是否为空
### 否：初始化容量为16的数组
### 是：创建一个新的数组，容量为原数组的两倍<font style="color:rgba(255,0,0,1);">(<<1)</font>，将原数组的数据移动到新的数组，遍历当前数组，判断当前数组的值.next是否为null
#### 是：则无链表或者红黑树代表无hash冲突的节点直接使用<font style="color:rgba(255,0,0,1);">e.hash & 新数组容量 - 1</font>计算新数组的索引位置并存入
#### 否：是红黑树则执行红黑树的添加逻辑
#### 否：是链表遍历链表判断<font style="color:rgba(255,0,0,1);">e.hash & 原数组容量</font> 是否 等于0
##### 是：则将原数组的下标对应的值赋给新的数组（原位置 如果原数组索引是1则新的也是1）
##### 否：将原数组下标对应的值赋给新数组下标（原下标+原数组的容量，如果原位置是1扩容了16位，则新位置是17）
# HashMap的寻址算法
根据源码所得在put元素时，会对key的hash值进行计算，计算公式（(h = key.hashCode()) ^ (h >>> 16)),扰动算，使hash值更加均匀，减少hash冲突

使用(n - 1) & hash 得到索引代替取模运算，性能更好，但是数组长度必须是2的N次幂

因为(n - 1) & hash方法于取模运算相等的情况基于数组长度是2的N次幂实现的，如果不是两种方法计算结果不一样

# HashMap的数组长度为啥是2的N次幂
## 计算索引时效率更高可以代替取模运算
##  HashMap扩容时会通过 <font style="color:rgba(255,0,0,1);">e.hash & 原数组容量</font> 是否 等于0 计算元素是否留在原位置，否则新位置
# 为什么容量必须是2的幂
1. (n-1)&hash 等价于取模
2. 位运算更快
3. hash分布更均匀

# 为什么树化阈值是8
1. 统计学概率：链表长度≥8概率极低
2. 红黑树有额外开销
3. 8是性能平衡点

# 为什么退化阈值是6
避免频繁树化/退化（抖动）

# JDK1.7死循环问题
原因：

头插法 + 并发扩容

导致：

 链表形成环 → CPU 100% 

# <font style="color:#DF2A3F;">多线程下hashmap会出现什么问题</font><font style="color:#DF2A3F;">⚠️</font>
jdk1.7使用的是尾插法进行链表的插入，如果多线程下会导致扩容时，本是a指向b，多线程下操作会出现一个线程扩容迁移时是a指向b另一个是b指向a此时如果再次进入此元素位就回导致死循环

jdk1.8多线程下会导致相同key的值会进行覆盖

# <font style="color:#DF2A3F;">hashmap和hashtable的区别</font><font style="color:#DF2A3F;">⚠️</font>
hashtable是线程安全的hashmap不是

hashmap运行key可以存在单个null值，value可以存储多个null值；hashtable的key和value都不允许是null会抛空指针异常

hashmap初始容量为16扩容为2倍，而hashtable初始为11扩容2n+1

hashtable性能差

# <font style="color:#DF2A3F;">linkedHashMap和treeMap区别</font><font style="color:#DF2A3F;">⚠️</font>
<font style="color:#DF2A3F;">linkedHashMap底层是维护了一个hashmap加上一个双向链表</font>

<font style="color:#DF2A3F;">维护了元素的插入顺序，可以按序查询遍历</font>

<font style="color:#DF2A3F;">可以在需要保证遍历顺序和插入顺序一致时使用</font>

<font style="color:#DF2A3F;">treemap底层就是一个红黑树</font>

<font style="color:#DF2A3F;">会对key进行自动排序默认升序遍历根据key的排序输出</font>

<font style="color:#DF2A3F;">key必须实现comparable接口或者传入comparator</font>

<font style="color:#DF2A3F;">场景:需要对key进行排序时使用，比如排行榜，按时间顺序的任务队列</font>

<font style="color:#DF2A3F;"></font>





















