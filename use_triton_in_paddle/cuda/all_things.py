def get_device_capability(idx):
    import paddle
    return paddle.device.cuda.get_device_capability(idx)



def current_device():
    import paddle
    device_num = paddle.device.get_device()
    try:
        gpu_id = device_num.split(':')[1]
        return (int)(gpu_id)
    except IndexError:
        raise RuntimeError("CUDA is not available or No available CUDA device for the specified CUDA_VISIBLE_DEVICES")


def set_device(idx):
    import paddle
    paddle.device.set_device(f'gpu:{idx}')


def is_available():
    import paddle
    return paddle.device.is_compiled_with_cuda()


def current_stream(idx):
    import paddle
    return paddle.device.cuda.current_stream(idx)

