# Use Triton in Paddle


- 由于triton源码中部分util函数（如检查当前机器的计算能力，检查当前机器的idx）依赖了torch，这对于paddle用户想要使用triton不是很友好。
- 故，此项目将triton源码中的部分依赖triton的代码，替换为paddle的代码。
- 操作步骤如下：
~~~bash
python -m pip install git+https://github.com/zhoutianzi666/UseTritonInPaddle.git

# 仅需执行 一次 如下命令，之后在任意终端都可以使用triton。无需重复执行
python -c "import use_triton_in_paddle; use_triton_in_paddle.make_triton_compatible_with_paddle()"
~~~


- 上述命令会自动将triton内部的`import torch`换成
~~~python
try:
    import torch
except:
    print("No module named 'torch', we will use_triton_in_paddle as torch inside triton")
    import use_triton_in_paddle as torch
~~~

- 由于本项目只有几个文件，所以即使你的网很差，你也应该可以安装成功。
- 然后就可以在paddle中正常使用triton了。和torch的用法一摸一样


<font color=red size=3> 我们目前只支持在paddle中使用 triton 2.3 和 triton 3.0 ，其他的也许可以但我们没有试过</font>














