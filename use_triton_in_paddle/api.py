
files = []



import triton
if triton.__version__[0] == '3':
    files = [
        triton.__path__[0] + "/backends/amd/driver.py",
        triton.__path__[0] + "/backends/nvidia/driver.py",
        triton.__path__[0] + "/backends/driver.py",
    ]
elif triton.__version__[0:3] == '2.3':
    files = [
        triton.__path__[0] + "/runtime/driver.py",
        triton.__path__[0] + "/common/build.py",
    ]
else:
    raise Exception('Unsupported Triton version: {}'.format(triton.__version__))

def make_triton_compatible_with_paddle():
    if triton.__version__[0:3] == '2.3':
        # fix a bug in 2.3 version
        link_file = triton.__path__[0] + "/tools/link.py"
        new_all_lines = []
        with open(link_file, 'r') as f:
            for line in f.readlines():
                line = line.replace("(int)sizeof({meta.orig_kernel_name}_kernels);", "(int)(sizeof({meta.orig_kernel_name}_kernels) / sizeof({meta.orig_kernel_name}_kernels[0]));")
                new_all_lines.append(line)
        with open(link_file, 'w') as f:
            f.writelines(new_all_lines)

    for file in files:
        new_all_lines = []
        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.replace("import torch", "import use_triton_in_paddle as torch")
                new_all_lines.append(line)
        with open(file, 'w') as f:
            f.writelines(new_all_lines)



def restore_triton():
    for file in files:
        new_all_lines = []
        with open(file, 'r') as f:
            for line in f.readlines():
                line = line.replace("import use_triton_in_paddle as torch", "import torch")
                new_all_lines.append(line)
        with open(file, 'w') as f:
            f.writelines(new_all_lines)


