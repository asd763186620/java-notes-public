## i++问题
```java
public static void main(String[] args) {
        int i = 1;
        System.out.println("i:" + i); // 1
        System.out.println("++i:" + ++i); //2
        System.out.println("i++:" + i++); //2
        System.out.println("i:" + i);//3
        System.out.println("--i:" + --i);//2
        System.out.println("i--:" + i--);//2
        System.out.println("i:" + i);//1
    }

```

## 服务可用性多少个9什么意思
<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765957765950-317a781f-ca25-40cb-b8ff-0732a040895c.png)

## Arrays.asList()坑
```java
List<Integer> list = new ArrayList<>(Arrays.asList(1,2,3,4,5));
        list.add(6);
        list.forEach(System.out::println);
```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765958150418-f6ed9b2c-b90c-429d-96de-6e72e2151822.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765958310040-9ddc8916-78e6-48fc-8dae-fc7f8065c493.png)

## 遍历集合时remove/add注意事项
```java
Iterator<Integer> iterator = list.iterator();
        while (iterator.hasNext()){
            if (iterator.next() == 3){
                iterator.remove();
            }
        }
        list.removeIf(item->item==4);
        list.forEach(System.out::println);
```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765958896696-c598f0a0-8ebf-4e29-9d67-7bad12c88353.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765958909490-07b0bbf8-7d7b-4a93-995d-04114588d7f0.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765958817545-a6992e8c-c6f9-425f-8985-d45b6b239fce.png)

## hashcode冲突案例
```java
 System.out.println("Aa" + "Aa".hashCode());
 System.out.println("BB" + "BB".hashCode());
```

```java
public static void main(String[] args) {
    HashSet<Integer> hashSet = new HashSet<>();
    for (int i = 1; i <= 11 * 10000; i++) {
        int hashCode = new Object().hashCode();
        if (!hashSet.contains(hashCode)){
            hashSet.add(hashCode);
        } else {
            System.out.printf("发生了hash冲突在%d次,值是%d",i,hashCode);
        }
    }
    System.out.println(hashSet.size());
}
```

## Integer包装类对象
```java
public static void main(String[] args) {
        Integer a = Integer.valueOf(600);
        Integer b = Integer.valueOf(600);
        int c = 600;
        System.out.println(a == b); // false
        System.out.println(a.equals(b)); // true
        System.out.println(a == c); // true
        System.out.println("---------------");
        Integer x = Integer.valueOf(99);
        Integer y = Integer.valueOf(99);
        System.out.println(x.equals(y)); // true
        System.out.println(x == y); // true
    }
```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765960881053-9bf5a059-1503-4bd1-94f6-f112eff552a3.png)

## BigDecimal坑
```java
package com.atguigu.interview2.utils;

import java.math.BigDecimal;

/**用于高精确处理常用的数学运算
 * @auther zzyy
 * @create 2024-05-02 17:21
 */
public class ArithmeticUtils
{
    //默认除法运算精度
    private static final int DEF_DIV_SCALE = 10;

    /**
     * 提供精确的加法运算
     *
     * @param v1 被加数
     * @param v2 加数
     * @return 两个参数的和
     */

    public static double add(double v1, double v2) {
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return b1.add(b2).doubleValue();
    }

    /**
     * 提供精确的加法运算
     *
     * @param v1 被加数
     * @param v2 加数
     * @return 两个参数的和
     */
    public static BigDecimal add(String v1, String v2) {
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        return b1.add(b2);
    }

    /**
     * 提供精确的加法运算
     *
     * @param v1    被加数
     * @param v2    加数
     * @param scale 保留scale 位小数
     * @return 两个参数的和
     */
    public static String add(String v1, String v2, int scale) {
        if (scale < 0) {
            throw new IllegalArgumentException(
                    "The scale must be a positive integer or zero");
        }
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        return b1.add(b2).setScale(scale, BigDecimal.ROUND_HALF_UP).toString();
    }

    /**
     * 提供精确的减法运算
     *
     * @param v1 被减数
     * @param v2 减数
     * @return 两个参数的差
     */
    public static double sub(double v1, double v2) {
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return b1.subtract(b2).doubleValue();
    }

    /**
     * 提供精确的减法运算。
     *
     * @param v1 被减数
     * @param v2 减数
     * @return 两个参数的差
     */
    public static BigDecimal sub(String v1, String v2) {
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        return b1.subtract(b2);
    }

    /**
     * 提供精确的减法运算
     *
     * @param v1    被减数
     * @param v2    减数
     * @param scale 保留scale 位小数
     * @return 两个参数的差
     */
    public static String sub(String v1, String v2, int scale) {
        if (scale < 0) {
            throw new IllegalArgumentException(
                    "The scale must be a positive integer or zero");
        }
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        return b1.subtract(b2).setScale(scale, BigDecimal.ROUND_HALF_UP).toString();
    }

    /**
     * 提供精确的乘法运算
     *
     * @param v1 被乘数
     * @param v2 乘数
     * @return 两个参数的积
     */
    public static double mul(double v1, double v2) {
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return b1.multiply(b2).doubleValue();
    }

    /**
     * 提供精确的乘法运算
     *
     * @param v1 被乘数
     * @param v2 乘数
     * @return 两个参数的积
     */
    public static BigDecimal mul(String v1, String v2) {
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        return b1.multiply(b2);
    }

    /**
     * 提供精确的乘法运算
     *
     * @param v1    被乘数
     * @param v2    乘数
     * @param scale 保留scale 位小数
     * @return 两个参数的积
     */
    public static double mul(double v1, double v2, int scale) {
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return round(b1.multiply(b2).doubleValue(), scale);
    }

    /**
     * 提供精确的乘法运算
     *
     * @param v1    被乘数
     * @param v2    乘数
     * @param scale 保留scale 位小数
     * @return 两个参数的积
     */
    public static String mul(String v1, String v2, int scale) {
        if (scale < 0) {
            throw new IllegalArgumentException(
                    "The scale must be a positive integer or zero");
        }
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        return b1.multiply(b2).setScale(scale, BigDecimal.ROUND_HALF_UP).toString();
    }

    /**
     * 提供（相对）精确的除法运算，当发生除不尽的情况时，精确到
     * 小数点以后10位，以后的数字四舍五入
     *
     * @param v1 被除数
     * @param v2 除数
     * @return 两个参数的商
     */

    public static double div(double v1, double v2) {
        return div(v1, v2, DEF_DIV_SCALE);
}

    /**
     * 提供（相对）精确的除法运算。当发生除不尽的情况时，由scale参数指
     * 定精度，以后的数字四舍五入
     *
     * @param v1    被除数
     * @param v2    除数
     * @param scale 表示表示需要精确到小数点以后几位。
     * @return 两个参数的商
     */
    public static double div(double v1, double v2, int scale) {
        if (scale < 0) {
            throw new IllegalArgumentException("The scale must be a positive integer or zero");
        }
        BigDecimal b1 = new BigDecimal(Double.toString(v1));
        BigDecimal b2 = new BigDecimal(Double.toString(v2));
        return b1.divide(b2, scale, BigDecimal.ROUND_HALF_UP).doubleValue();
    }

    /**
     * 提供（相对）精确的除法运算。当发生除不尽的情况时，由scale参数指
     * 定精度，以后的数字四舍五入
     *
     * @param v1    被除数
     * @param v2    除数
     * @param scale 表示需要精确到小数点以后几位
     * @return 两个参数的商
     */
    public static String div(String v1, String v2, int scale) {
        if (scale < 0) {
            throw new IllegalArgumentException("The scale must be a positive integer or zero");
        }
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v1);
        return b1.divide(b2, scale, BigDecimal.ROUND_HALF_UP).toString();
    }

    /**
     * 提供精确的小数位四舍五入处理
     *
     * @param v     需要四舍五入的数字
     * @param scale 小数点后保留几位
     * @return 四舍五入后的结果
     */
    public static double round(double v, int scale) {
        if (scale < 0) {
            throw new IllegalArgumentException("The scale must be a positive integer or zero");
        }
        BigDecimal b = new BigDecimal(Double.toString(v));
        return b.setScale(scale, BigDecimal.ROUND_HALF_UP).doubleValue();
    }

    /**
     * 提供精确的小数位四舍五入处理
     *
     * @param v     需要四舍五入的数字
     * @param scale 小数点后保留几位
     * @return 四舍五入后的结果
     */
    public static String round(String v, int scale) {
        if (scale < 0)
        {
            throw new IllegalArgumentException("The scale must be a positive integer or zero");
        }
        BigDecimal b = new BigDecimal(v);
        return b.setScale(scale, BigDecimal.ROUND_HALF_UP).toString();
    }

    /**
     * 取余数
     *
     * @param v1    被除数
     * @param v2    除数
     * @param scale 小数点后保留几位
     * @return 余数
     */
    public static String remainder(String v1, String v2, int scale) {
        if (scale < 0) {
            throw new IllegalArgumentException(
                    "The scale must be a positive integer or zero");
        }
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        return b1.remainder(b2).setScale(scale, BigDecimal.ROUND_HALF_UP).toString();
    }

    /**
     * 取余数  BigDecimal
     *
     * @param v1    被除数
     * @param v2    除数
     * @param scale 小数点后保留几位
     * @return 余数
     */
    public static BigDecimal remainder(BigDecimal v1, BigDecimal v2, int scale) {
        if (scale < 0)
        {
            throw new IllegalArgumentException("The scale must be a positive integer or zero");
        }
        return v1.remainder(v2).setScale(scale, BigDecimal.ROUND_HALF_UP);
    }

    /**
     * 比较大小
     *
     * @param v1 被比较数
     * @param v2 比较数
     * @return 如果v1 大于v2 则 返回true 否则false
     */
    public static boolean compare(String v1, String v2) {
        BigDecimal b1 = new BigDecimal(v1);
        BigDecimal b2 = new BigDecimal(v2);
        int bj = b1.compareTo(b2);
        boolean res;
        if (bj > 0)
            res = true;
        else
            res = false;
        return res;
    }
}


 


```

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765961546318-91d0208f-70d8-4151-ae8d-dbf870a38f81.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765961638182-15707315-800e-409b-8fc3-d7167f835e2f.png)

```java
public static void main(String[] args) {
        BigDecimal bigDecimal = new BigDecimal("0.02");
        BigDecimal bigDecimal1 = new BigDecimal("0.03");
        // System.out.println(bigDecimal.divide(bigDecimal1)); // 报错 必须指定对应的小数点后面位数和计算方式
        // 指定四舍五入
        System.out.println(bigDecimal.divide(bigDecimal1,2,BigDecimal.ROUND_HALF_UP));
    }
```

科学计数

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2025/png/43313275/1765962708513-24512800-ac43-4aee-9af7-f3899c94ea7e.png)

## list去重有几种方法,至少写出三个
```java
package com.lj.list;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.Objects;

/**
 * @Classname ListDemo
 * @Date 2026/4/1 20:04
 * @Author 花非
 * @Version 1.0
 * @Description list去重
 */
public class ListDemo {
    public static void main(String[] args) {
        ArrayList<Integer> integers = new ArrayList<>();
        integers.add(0);
        integers.add(1);
        integers.add(1);
        integers.add(2);
        integers.add(2);
        integers.add(3);
        // list去重
        // hashSet
        // ListDemo.hashSetRemoveDuplicates(integers);
        // 循环验证是否包含
        // ListDemo.circulation(integers);
        // stream流
        // ListDemo.streamMethod(integers);
        // 利用类似双指针的打法,根据值找下标下标相同则删除元素
        ListDemo.doublePointer(integers);
        // 利用双重for循环解决
        ListDemo.doubleFor(integers);


    }
    // 利用双重for循环解决
    private static void doubleFor(ArrayList<Integer> integers) {
        ArrayList<Integer> newList = new ArrayList<>(integers);
        for (int i = 0; i < newList.size() - 1; i++) {
            for (int j = newList.size() - 1;  j > i; j--) {
                if (Objects.equals(newList.get(i), newList.get(j))){
                    newList.remove(j);
                }
            }
        }
        newList.forEach(System.out::println);
    }

    // 利用类似双指针的打法,根据值找下标下标不同则删除元素
    private static void doublePointer(ArrayList<Integer> integers) {
        ArrayList<Integer> srcList = new ArrayList<>(integers);
        ArrayList<Integer> newList = new ArrayList<>(integers);
        for (Integer element : srcList) {
            if (newList.indexOf(element) != newList.lastIndexOf(element)){
                newList.remove(newList.lastIndexOf(element));
            }
        }
        newList.forEach(System.out::println);
    }

    // stream流 去重
    private static void streamMethod(ArrayList<Integer> integers) {
        integers.stream().distinct().forEach(System.out::println);
    }

    // 循环验证去重
    private static void circulation(ArrayList<Integer> integers) {
        ArrayList<Integer> arrayList = new ArrayList<>();
        for (Integer i1 : integers) {
            if (!arrayList.contains(i1)) {
                arrayList.add(i1);
            }
        }
        for (Integer i : arrayList) {
            System.out.println(i);
        }
    }

    // hashSet
    public static void hashSetRemoveDuplicates(ArrayList<Integer> integers){
        HashSet<Integer> hashSet = new HashSet<>(integers);
        for (Integer i : hashSet) {
            System.out.println(i);
        }
    }
}

```

## ==和equals对比
### == 关键看是比较基础数据类型还是引用数据类型
1. == 可以比较基础数据类型  比较值大小
2. == 引用数据类型比较内存地址

### equals看比较的引用数据类型是否重写equals和hashcode
1. equals 比较规则不知道,看是否类进行覆写object类中的equals和hashcode
2. 引用数据类型如果没有覆写,使用equals对比此时使用的object内的原比较方法用的==比较的内存地址
3. hashset底层使用的hashmap相当与使用的hashmap的key+一个常量value组成
4. hashmap的key是无序且无重复的,但是hashmap重写了hashcode方法,hashmap的put方法实际上比较的是key的hash值

此时person没有重写equals和hashcode方法

```java
package com.lijia.javase;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.HashSet;
import java.util.Set;

/**
 * @Classname JavaBaseQuestions
 * @Date 2026/4/2 10:15
 * @Author 花非
 * @Version 1.0
 * @Description java基础面试题
 *   == 和 equals
 *  1 比较范围
 *    1.1 == 既可以比较基本类型也可以比较引用类型，

 *
 *    1.2 equals
 *    只能比较引用类型，equals(Object obj)
 *
 *  2 比较规则
 *     ==对于基本类型值是否相等，对于引用类型内存地址是否相等
 *    equals比较规则，看是否被重写过。
 *    没有被重写，出厂默认就是==
 *    如果被重写，具体看实现方法
 */
public class JavaBaseQuestions {
    public static void main(String[] args) {
        String s1 = new String( "abc");
        String s2 = new String( "abc");
        String s3 = "abc";
        System.out.println(s1 == s2); // false
        System.out.println(s1.equals(s2)); //true
        System.out.println(s1 == s3); //false
        Set<String> set01 = new HashSet<>();
        set01.add(s1);
        set01.add(s2);
        System.out.println(set01.size()); // 1
        System.out.println("===================");
        Person p1 = new Person("abc");
        Person p2 = new Person("abc");
        System.out.println(p1 == p2); // false
        System.out.println(p1.equals(p2)); // false
        Set<Person> set02 = new HashSet<>();
        set02.add(p1);
        set02.add(p2);
        System.out.println(set02.size()); // 2
        System.out.println("===================");

    }
}

@NoArgsConstructor
@Getter
@Setter
class Person{
    private int id;
    private String personName;
    public Person (String personName){
        this.personName = personName;
    }
}
```

## 值传递,传值还是引用
```java
 搜索

便笺
package com.atguigu.interview2.javase;

import com.atguigu.interview2.entities.Person;

/**
 * @auther zzyy
 * @create 2024-05-01 21:11
 */
public class TransmitValueOrRef
{
    public void changeValue1(int age){
        age = 30;
    }
    public void changeValue2(Person person){
        person.setPersonName("xxx");
    }
    public void changeValue3(String str){
        str = "xxx";
    }
    public static void main(String[] args){
        TransmitValueOrRef test = new TransmitValueOrRef();
        int age = 20;
        test.changeValue1(age);
        System.out.println("age----"+age);

        Person person = new Person("abc");
        test.changeValue2(person);
        System.out.println("personName-----"+person.getPersonName());

        String str = "abc";
        test.changeValue3(str);
        System.out.println("String-----"+str);
    }
}


 


```

## 深拷贝和浅拷贝
1. 对象拷贝:将一个对象的属性拷贝到另一个有这相同类型的对象中去,在程序中拷贝对象是常见的,只要是为了在新的上下文中复用对象的部分或全部数据.
2. 浅拷贝:浅拷贝只复制指向某个对象的指针,而不是复制对象本身,新旧对象用的是同一个引用地址,共享内存.
    1. 拷贝基本类型时,拷贝的是基本类型的值
    2. 拷贝引用类型就是拷贝的对象的内存地址
    3. 多个引用指向同一个对象,如果其中一个引用改变了对象,会影响到其他的引用
3. 深拷贝:深拷贝会创造出一个一模一样的对象,新旧对象不共享内存

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1775120060629-6c9a0438-2af6-47f3-ae17-4665bbd6529b.png)

4. 为什么使用深拷贝:复制一个对象能确保复制对象是复制的真正的副本,与原对象没有引用关系,多线程的环境中如果不使用深拷贝会导致多个线程同时访问和修改同一对象,会导致数据不一致的情况,但使用深拷贝,每个线程可以有自己独立的对象副本,线程可以在自己独立的副本上进行操作,从而避免了线程安全问题.
5. serializable和cloneable都属于只声明了接口没有对应的实现
6. 如果使用clone()方法时,如果使用的类没有实现cloneable接口的话会报错

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1775129194719-2aaff11b-7ee5-40d0-a1d1-5bd593e726a7.png)

<!-- 这是一张图片，ocr 内容为： -->
![](https://cdn.nlark.com/yuque/0/2026/png/43313275/1775129201189-c0c0ac30-4d04-42cd-b3a4-84554bbdc9f4.png)

```java
package com.atguigu.interview2.javase;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

/**
 * @auther zzyy
 * @create 2024-05-29 17:29
 */
public class ShallowDeepCopyDemo
{
    public static void main(String[] args) throws CloneNotSupportedException
    {
        m1();
    }

    private static void m1() throws CloneNotSupportedException
    {
        Emp emp = new Emp("z3",15,"雷军","CEO");
        System.out.println("原始对象："+emp.getBoss().getTitle());

        Emp emp2 = (Emp)emp.clone();
        System.out.println("拷贝对象："+emp2.getBoss().getTitle());

        System.out.println();
        emp2.getBoss().setTitle("CTO");
        System.out.println("------emp2拷贝对象修改Title=CTO,是否会影响原始对象");


        System.out.println("原始对象："+emp.getBoss().getTitle());
        System.out.println("拷贝对象："+emp2.getBoss().getTitle());
    }
}


@Data
@AllArgsConstructor
@NoArgsConstructor
class Boss implements Cloneable
{
    private String bossName;
    private String title;

    @Override
    protected Object clone() throws CloneNotSupportedException
    {
        return super.clone();
    }
}
@Data
@AllArgsConstructor
@NoArgsConstructor
class Emp implements Cloneable
{
    private String empName;
    private Integer age;

    private Boss boss;

    public Emp(String empName, Integer age, String bossName,String title)
    {
        this.empName = empName;
        this.age = age;
        this.boss = new Boss(bossName,title);
    }

    @Override
    protected Object clone() throws CloneNotSupportedException
    {
        return super.clone();
    }
    //深拷贝
    /*@Override
    protected Object clone() throws CloneNotSupportedException
    {
        return new Emp(empName,age,boss.getBossName(),boss.getTitle());
    }*/
}
```

## Arraylist和LinkedList区别
### 底层数据结构:
+ ArrayList底层是动态数组数据结构,连续内存空间占用内存小节省内存
+ LinkedList底层是双向链表数据结构,除数据之外还需要维护前后两个指针占用内存比ArrayList大

### 操作数据效率
+ ArrayList按照下标来查询时间复杂度O1,如果不按照下标那时间复杂度是On,新增时如果在尾部新增则复杂度是O1除此之外复杂度是On,修改删除同理知道下标则为O1不知道则为On
+ LinkedList无下标,但是有头尾节点,如果在头尾节点添加修改删除时间复杂度O1如果不是头尾节点则是On

### 如何保证线程安全
两个都是线程不安全的.

如果使用在方法内部使用定义局部变量线程是安全的

可以使用collections.synchronizedList(new ArrayList<>())

可以使用collections.synchronizedList(new LinkedList<>())

