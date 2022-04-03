# 输出结果

```sh
线程id：13 耗时：2.835000

线程id：15 耗时：2.846000

线程id：14 耗时：2.848000

三次add函数运行完毕后：1 耗时：2.848000

开始运行add函数
线程id：1 耗时：2.854000


Process finished with exit code 0
```

# 分析

1. java开启多线程是可以使用多核的。
2. 同样的函数，java循环10亿次的时间也比python循环一亿次耗时短。余python的对比，python同样的代码在readme.md中有输出结果。
