
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
                if ("import torch" in line):
                    copy0_line = line
                    copy1_line = line
                    copy2_line = line
                    copy3_line = line
                    
                    
                    copy0_line = copy0_line.replace("import torch", "try:")
                    copy1_line = copy1_line.replace("import torch", "\timport torch")
                    copy2_line = copy2_line.replace("import torch", "execpt:")
                    copy3_line = copy3_line.replace("import torch", "\timport use_triton_in_paddle as torch")
                    new_all_lines.append(copy0_line)
                    new_all_lines.append(copy1_line)
                    new_all_lines.append(copy2_line)
                    new_all_lines.append(copy3_line)
                else:
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


