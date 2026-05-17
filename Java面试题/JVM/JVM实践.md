# JVM调优参数如何设置
## war包
war包部署在tomcap中设置在tomcat中设置具体路径为：TOMCAT_HOME/bing/catalina.sh

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778837787885-304059cc-3d3d-4cfe-bb4c-b30a22b689b4.png)

## jar包
jar包部署时，可以在启动参数设置启动命令java -jar中间设置java -Xms512m -Xmx1024m -jar xxx.jar

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778837803530-b12a45f0-d326-42f0-a9c1-8617f7d1f812.png)

# JVM调优参数
对于JVM调优，主要是调整年轻代、老年代、元空间的内存空间大小以及使用的垃圾回收器类型。

1. 堆空间大小设置
2. 虚拟机栈的设置
3. 年轻代中Eden区和两个幸存者区的大小比例
4. 年轻代晋升老年代的阈值
5. 指定垃圾回收器

## 设置堆空间大小
设置初始堆大小和堆最大的大小，为了防止垃圾回收器在初始大小与最大大小之间收缩堆产生额外的空间，通常将初始大小和最大大小设置为相同值。

通过：-Xms指定初始堆大小-Xmx指定堆最大大小（不指定单位默认为字节，指定单位则根据单位设置）  
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778854305396-68a1347c-223f-4fb6-a682-0c1c7c631f7c.png)

1. 堆空间大小的默认值是物理内存的1/4，初始大小是物理内存的1/64
2. 堆太小可能导致频繁的垃圾回收，产生stw，暂停用户线程
3. 堆内存大，好是好但是有风险，如果产生了FullGC的话，会扫描整个堆空间，暂停用户线程等待时间长
4. 设置参考：尽量大，同时考察当前计算机其他程序的内存使用情况

## 虚拟机栈的设置
虚拟机栈的设置：每个线程默认1m的内存，用户存放栈帧、参数、局部变量、返回地址等，但一般256k够用，通过减少线程的堆栈信息，可以产生更多的线程，实际受限于操作系统

通过：-Xss指定每个线程stack的大小例如-Xss128k

## 设置年轻代中伊甸园区和幸存者区比例
设置年轻代中伊甸园区和幸存者区的比例，如果不设置默认是1:1:8。通过增大伊甸园区的大小，可以减少年轻代垃圾回收的次数，但是虽然次数减少了，但是当伊甸园区内存满时，由于占有内存空间过大，导致进行垃圾回收释放内存时缓慢，stw等待时间过长，因此需要根据程序情况去调优

具体参数为：-XXSurvivorRatio=8

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778854706895-936e9398-95d2-4803-a7ae-068b575d866b.png)

## 年轻代晋升老年代阈值
年轻代晋升老年代，指的时经过多次GC移动后存活的对象，默认是15次晋升老年代，可以设置取值范围为：0-15

具体参数为：-XX:MaxTenuringThreshold=threshold

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778854776601-0a22bb36-ea3c-46b8-934d-bbdf9397e766.png)

## 设置垃圾回收器类型
通过指定具体的垃圾回收器增大吞吐量提高性能

jdk1.8默认是并行垃圾回收器

具体参数为：-XX:UseParallerlGC;-XX:UseParallerOldGC

也可指定：-XX:UseG1GC

# JVM调优工具
## 命令行工具
1. jps
+ 查看java进程状态信息
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778855139197-9e15d955-3202-446c-82f3-dbf89c20ec70.png)
2. jstack
+ 查看具体java进程内的堆栈信息
+ jastack [pid] pid指的是jps查出来的java进程信息
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778855276394-fc4f17f6-2549-47ea-a646-308cff98d248.png)
3. jmap
+ 用于生成堆转内存快照、内存使用情况
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778856215233-21ebf41c-c485-4076-b167-34b7ba2dc351.png)
+ 程序运行前通过vm参数获取dump文件
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778858278819-12d4f816-5ded-4851-9cb0-cec485ca5eb4.png)
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778857094333-06f5af35-b2b3-40d8-a8f8-b22ba0e0688e.png)
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778855831999-2cdde10f-660c-461c-aa97-49fcb5c2e0d5.png)
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778856074745-b145ef9b-10e3-4bd1-aa1f-e9ad18f89df4.png)
4. jhat
+ 堆栈储快照分析工具
5. jstat
+ JVM统计检测工具

## 图形化工具
1. jconsole
+ 用于对jvm的内存、线程、类的监控，是一个基于jmx的GUI性能监控工具
+ 工具目录：JAVA_HOME/bin/jconsole.exe
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778857420770-d98b5058-3dfd-4bb1-8074-9756fbf876a1.png)
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778857433262-b66ef352-90cf-4e5a-a8bf-fc288f793a85.png)
2. VisualVM
+ 监控线程、内存情况，查看方法的CPU时间和内存中的对象，已被gc的对象，反向查看分配的堆栈
+ 目录：JAVA_HOME/bin/jvisualvm.exe
+ 查看运行中的dump，dump文件是进程的内存镜像，可以把程序的执行状态通过调试器保存到dump文件中
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778857582483-cc5ffcd2-157e-4cff-bccc-81299058a7d5.png)
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778857600522-8ee273d5-5858-4978-8b4d-d68162849420.png)
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778857695888-f7f8d3ea-8389-4008-870f-c954d4cfceaf.png)

# Java内存泄漏的排查思路
产生内存泄漏的区域：

1. 虚拟机栈
+ 递归调用产生死循环，创建栈帧导致内存溢出：SOF（栈内存溢出）
+ 方法中有占有内存过大的局部变量导致栈溢出
2. 方法区/元空间
+ 动态加载的类太多，导致元空间内存溢出OOMmetaspace
3. 堆内存空间
+ 较大对象一直存活导致内存泄漏OOMjava head space

排查思路：

1. 获取堆内存快照dump
2. 使用VisualVM分析dump文件
3. 通过查看堆栈信息，定位内存溢出问题
4. jmap是程序运行时获取程序的dump文件，一般出现内存溢出时，程序已经中断了因此通过下方vm参数的方式获取
5. 在程序运行前制定vm参数
+ -XX:+HeapDumpOnOutOfMemoryError-XXHeapDumpPath=/Users/lijia/Documents/headDump
6. 通过visualVM分析dump文件
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778858809148-d7a593b0-97e5-4c8d-934a-cfc336d00b3a.png)
7. 通过堆栈信息的情况，大概定位内存溢出的代码
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778858849720-43bb583b-3112-4c2a-b925-5dede8a80ff6.png)

# CPU飙高的排查方案和思路
1. 通过top命令在服务器查看占用cpu高的进程
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778859086446-38e6ca57-9e72-4aeb-a199-97a383af9b37.png)
2. 通过新开一个当前服务器会话通过命令：ps -h -eo pid,tid,%cpu | grep pid(通过top查看的占用cpu高的进程pid) 此时返回的tid是java层面的线程id
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778859197489-60c72e3b-834c-48e7-92d5-d115e9b5b66c.png)
3. 通过命令jstack [pid]
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778859285347-541f7875-efd3-44e5-ac09-9afcc86112e7.png)
4. 由于通过jstack展示出来的堆栈信息中的tid是十六进制展示的因此需要通过命令：printf "%x\n" tid(通过ps -h -eo pid,tid,%cpu | grep pid)获取到的高cpu占用的tid 如图为2276
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778859416041-dc7e0930-b901-4c41-8c43-545f38ffe365.png)
5. 从jstack日志中找到操作系统层面的原生的十六进制的线程id（nid）
+ <!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1778859602737-1cdd02e7-e9db-416b-90f3-55819040418d.png)
6. 在通过返回的日志去代码中查看具体的上下文



































































