---
layout:     post                    # 使用的布局（不需要改）
title:      阿南带你理解无偏估计      # 标题 
subtitle:   走进科学                 # 副标题
date:       2020-02-06              # 时间
author:     Nam                     # 作者
header-img: img/post-bg-unbiased_estimate-highway.jpg    # 这篇文章标题背景图片
mathjax: true                       # 使用mathjax
catalog: true                       # 是否归档
tags:                               # 标签
    - 面试不被怼系列
    - 数学基础
---

# 理解无偏估计

## 前言

今天阿南来讲一下***无偏估计 (unbiased estimate)***。

无偏估计是本科阶段概率论与数理统计课程里的内容，现在却只能记个大概轮廓***（基础不牢，地动山摇）***。然而，研究生阶段在对数据分析时经常要用到这个概念，并且在面试阶段也经常会考察面试者对其的理解与推导。于是今天我重新复习梳理了一遍，希望我今天的博文对大家能有所帮助 :)

## 正文

***无偏估计***, 顾名思义，就是没有偏差的估计。 与其对应的就是***有偏估计***，即有偏差的估计。

众所周知，机智的人类总是喜欢没有偏差的事物，比如说在大陆的小伙伴深有体会的高考估分！准确地估分对于填报志愿来说非常重要，所以霸霸麻麻也常说考的好不如报的好！（越长大越觉得高考很重要~）。闲话少说，进入今天的正题。

首先是关于***总体均值*** $\mu$ 的无偏估计

假设我们要去估计全海南省每颗椰子树上椰子个数的平均值，最简单粗暴且最准确的方法就是把全省的每颗椰子树情况都统计一遍就可以得出结果了。然鹅，这个方法是不可行的（因为不可能花费这么多人力物力去干这件事 - -！），所以我们就要另辟蹊径！ 作为当代优秀青年的你脱口而出：“我们抽样调查，用部分样本估计总体！” 

![此处应该有掌声！](http://i2.tiimg.com/708786/a7faeea6a06fe891.png)

机智的我们就跑去全海南的各个市县随机采样，三亚选10棵、海口选二十棵，文昌选50棵, etc. 有的小伙伴可能又会问了，为啥子文昌要选50棵而别的地方才选那么少？ 这是因为我们要按比例抽样，比方我们选择比例为1%，由于三亚的面积小椰子树总量少，我们只选取10棵，同理海口面积大我们就选择20棵。而对于文昌 - 东郊椰林，那里的椰子树数量远远超过其他地方，故按1%的比例我们就要选取50棵椰子树。

费了一番功夫后样本也采集完了，我们将得到的样本集标记为 $X_{sample}=[x_1, x_2, x_3, ..., x_n]$，而全海南省的椰子树样本我们标记为 $X=[x_1,x_2,...,x_N], N \gg n$。现在我们的目的是用这有限的$n$个样本去估计全海南省每棵树的平均椰子产出 $E[X]$。

阿南悄咪咪地告诉你，只需将所有样本 $x_i, i\in n$ 累加起来后简单地求平均，其值就是总体期望的 **无偏估计** 了！即：

$$
E[\bar X_{Sample}]=E[\frac{1}{n}\sum_{i=1}^{n}x_i]=\frac{1}{n}\sum_{i=1}^{n}E[x_i]  = E[X] = \mu \tag{1}
$$

乍一看似乎有悖常理，为啥这么小的部分就可以用来估计总体呢？接下来让阿南来讲解讲解。

>样本$x_1,x_2,...,x_n$是从总体$X$中随机采样，故样本集$X_{sample}$与总体$X$出自同种分布。所以各个样本的期望均为总体期望。

<br/>

今天的重点来了！接下来讲解关于***总体方差*** $\sigma^2$的无偏估计

首先摆出两个个关于方差的基本公式：

$$
\sigma^2=\frac{\sum_{i=1}^{N}(x_i-\mu)^2}{n} \tag{2}
$$

$$
\sigma^2 = E[X^2] - E^2[X] \tag{3}
$$

大家可能就说：“那就直接用上面的公式求方差鸭！”  但是阿南告诉大家，这事儿没那么简单。

注意，(2) 式中 $N$ 及 (3) 中 $X$ 为总体样本。所以又回到了之前的问题，就是我们很难获得所有的样本。机智的大家马上又会想到：“那我们用部分样本来估计整体的方差鸭！”

![安排](https://southeastasia1-mediap.svc.ms/transform/thumbnail?provider=spo&inputFormat=jpg&cs=fFNQTw&docid=https%3A%2F%2Fportland-my.sharepoint.com%3A443%2F_api%2Fv2.0%2Fdrives%2Fb!yCrE13FFC0eBwOhmDqozXFPw37e9aTlJr89PZtB_EX9piw4nyuaPToJQynbnXS0C%2Fitems%2F01LSWDOLKEQSXPLSIN7RGZTOTA7FWFNZ2N%3Fversion%3DPublished&access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvcG9ydGxhbmQtbXkuc2hhcmVwb2ludC5jb21AMjEwOWNlODMtN2RlNC00NDcxLTkxZmYtMjA1M2Y5MGExZmQ5IiwiaXNzIjoiMDAwMDAwMDMtMDAwMC0wZmYxLWNlMDAtMDAwMDAwMDAwMDAwIiwibmJmIjoiMTU4MTI5OTgxNyIsImV4cCI6IjE1ODEzMjE0MTciLCJlbmRwb2ludHVybCI6IlFJQko1OGdCbjdmYk52YUE2OElsMzRYQ2JTdDVrTTBtWmlhSDVSM2g3V3M9IiwiZW5kcG9pbnR1cmxMZW5ndGgiOiIxMTgiLCJpc2xvb3BiYWNrIjoiVHJ1ZSIsImNpZCI6IlpETmxaak16T1dZdFpUQXlNeTB3TURBd0xUUTJOV0l0TldRMk9UWmxNelV6TURsbSIsInZlciI6Imhhc2hlZHByb29mdG9rZW4iLCJzaXRlaWQiOiJaRGRqTkRKaFl6Z3RORFUzTVMwME56QmlMVGd4WXpBdFpUZzJOakJsWVdFek16VmoiLCJuYW1laWQiOiIwIy5mfG1lbWJlcnNoaXB8dXJuJTNhc3BvJTNhYW5vbiM2MGRlODFlMGUyOGIyMzRhZTM3NjRiZTJjMTk5NjA2M2ZmMDdjN2MxYTMzODZmMmQxZGI0NzNjNDA0ZTA1MTQ5IiwibmlpIjoibWljcm9zb2Z0LnNoYXJlcG9pbnQiLCJpc3VzZXIiOiJ0cnVlIiwiY2FjaGVrZXkiOiIwaC5mfG1lbWJlcnNoaXB8dXJuJTNhc3BvJTNhYW5vbiM2MGRlODFlMGUyOGIyMzRhZTM3NjRiZTJjMTk5NjA2M2ZmMDdjN2MxYTMzODZmMmQxZGI0NzNjNDA0ZTA1MTQ5Iiwic2hhcmluZ2lkIjoiVi82UTZSdUM3VVNFSHJPaUJOSXhNUSIsInR0IjoiMCIsInVzZVBlcnNpc3RlbnRDb29raWUiOiIyIn0.Vm5nNVFkTXN6dHVGR01YUzU2SDQxTm5RREp2WFpyVGFHR3pReTRaQUpUYz0&encodeFailures=1&srcWidth=&srcHeight=&width=400&height=400&action=Access)

这里先给出总体方差无偏估计的结论：

$$
\sigma^2 = E[\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2] \tag{4}
$$

刚开始的我也和大家一样迷惑，为啥子这里分母是 $n-1$ 而不是 $n$ ？ 后来经过在网上查阅了大量资料以及手动推导，发现事情的真相就是因为 (4) 式中的样本均值 $\bar x$ 与 总体均值 $\mu$ 是不相等的（除非瞎猫碰到死耗子刚好这次的样本集的均值等于总体均值），故乘子 $\frac{1}{n-1}$ 在此处是一个放大的作用 $(\frac{1}{n-1}>\frac{1}{n})$。

用文字描述可能不太直观，于是我们可以先用 $\frac{1}{n}$ 带入（4）式看看其结果是否等于总体方差 $\mu$。

$$
\begin{aligned}
E[s^2]
& = E[\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar x)^2] \\
& = \frac{1}{n}E[\sum_{i=1}^{n}((x_i-\mu)-(\bar x-\mu))^2] \\
& = \frac{1}{n}E[\sum_{i=1}^{n}\{(x_i-\mu)^2-2(x_i-\mu)(\bar x-\mu)+(\bar x-\mu)^2\}] \\
& = \frac{1}{n}E[\sum_{i=1}^{n}(x_i-\mu)^2]-\frac{1}{n}\sum_{i=1}^{n}E[(\bar x-\mu)^2] \\
& = \sigma^2 - \frac{1}{n}\sigma^2 \\
& = \frac{n-1}{n} \sigma^2
\end{aligned} \tag{5}
$$

其中第四步右半部分 $E[(\bar x-\mu)^2$ 是样本均值 $\bar x$ 的方差，其值为$\frac{1}{n} \sigma^2$。推导如下：

$$
\begin{aligned}
E[(\bar x-\mu)^2] 
& = \frac{1}{n^2} E[(\sum_{i=1}^{n}x_i-n\mu)^2] \\
& = \frac{1}{n^2} E[[(x_1-\mu)+(x_2-\mu)+...+(x_n-\mu)]^2] \\
& = \frac{1}{n^2} E[(x_1-\mu)^2+...+(x_n-\mu)^2+\sum_{i\ne j}(x_i-\mu)(x_j-\mu)]\\
& = \frac{1}{n^2} \cdot n \sigma ^2 \\
& = \frac{1}{n} \sigma ^2
\end{aligned} \tag{6}
$$

在 $(6)$ 式关于样本均值的方差的推导中，我们发现 $\sum_{i\ne j}(x_i-\mu)(x_j-\mu)$ 表示是 $x_i与x_j$两者的协方差，即：$Cov[x_i,x_j]$ 在这里两个样本之间是相互独立的，不具有相关性。

故协方差$Cov[x_i,x_j]=\sum_{i\ne j}(x_i-\mu)(x_j-\mu)=0$。

从 $(5)$ 式的推导中我们可以看出，若系数采用$\frac{1}{n}$ 则最终结果为$\frac{n-1}{n} \sigma^2$ 而并非 $\sigma^2$，故为**有偏估计**。

综合上文，为得到关于总体方差$\sigma^2$的无偏估计，我们只需要将系数变为 $\frac{n-1}{n}$，即：
$$
\sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2 \tag{7}
$$

好了，关于 **总体均值** $\mu$ 和**总体方差** $\sigma^2$ 无偏估计的推导到这里就结束了。总结一下：

>**总体均值** $\mu$ 的无偏估计：
>$$
\frac{1}{n}\sum_{i=1}^{n}x_i \tag{8}
$$

>**总体方差** $\sigma^2$ 的无偏估计：
>$$
\frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar x)^2 \tag{9}
$$

最后再用上个学期回归课程里关于***自由度*** (degree of freedom) 的概念来解释一下方差的无偏估计为什么少了个 $\underline{1}$

观察（9）式，由于 $\bar x$ 的存在导致整体的自由度由 $n$ 减少至 $n-1$。 因为 $\bar x$ 的值只能通过这 $n$ 个样本计算得到，我们可以认为其被限制住了。换句话说，当我们知道 $\bar x$ 之后，我们只需要只要 $n-1$ 个样本，剩下的那个数就可以通过 $\bar x$ 和任意 $n-1$ 个样本计算出来。
