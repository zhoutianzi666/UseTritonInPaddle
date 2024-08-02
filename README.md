# UseTritonInPaddle




- 由于triton源码中部分util函数（如检查当前机器的计算能力，检查当前机器的idx）依赖了triton，这对于paddle用户想要使用triton不是很友好。
- 故此项目，将triton源码中的部分依赖triton的代码，替换为paddle的代码。
- 使用方式，用户只需要安装`python -m pip install git+https://github.com/zhoutianzi666/UseTritonInPaddle.git`即可。
- 由于本项目只有几个文件，所以即使你的网很差，你也应该可以安装成功

# <font color=red size=15> 我们目前只支持在paddle中使用 triton 2.3 和 triton 3.0 ，其他的也许可以但我们没有试过</font>


## install之后用户只需要在终端执行 `python -c "import use_triton_in_paddle; use_triton_in_paddle.make_triton_compatible_with_paddle()"`即可在paddle中使用triton，记住，只需要执行一次就可以啦！之后在任意终端都无需再执行。

- 会自动将triton内部的`import torch`换成`import use_triton_in_paddle as torch`
- 然后就可以在paddle中正常使用triton了。和torch的用法一摸一样
- 如果你想恢复更改，那只需要`python -c "import use_triton_in_paddle; use_triton_in_paddle.restore_triton()"`即可！











