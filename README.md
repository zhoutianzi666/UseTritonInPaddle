# UseTritonInPaddle




- 由于triton源码中部分util函数（如检查当前机器的计算能力，检查当前机器的idx）依赖了triton，这对于paddle用户想要使用triton不是很友好。
- 故此项目，将triton源码中的部分依赖triton的代码，替换为paddle的代码。
- 使用方式，用户只需要安装`python3.8 -m pip install git+https://github.com/zhoutianzi666/UseTritonInPaddle.git`即可。
- 由于本项目只有几个文件，所以即使你的网很差，你也应该可以安装成功

`python3.8 -c "import use_triton_in_paddle; use_triton_in_paddle.make_triton_compatible_with_paddle()"``

- 会自动将triton内部的`import torch`换成`import use_triton_in_paddle as torch`
- 当然看起来换成下面这样的语句更保险一些
```py
try:
    import torch
except:
    print("No module named 'torch', we will use_triton_in_paddle as torch inside triton")
    import use_triton_in_paddle as torch
```

- 然后就可以在paddle中正常使用triton了。和torch的用法一摸一样

















