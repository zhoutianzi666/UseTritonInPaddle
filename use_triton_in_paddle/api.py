def make_triton_compatible_with_paddle():
    import triton
    files = [
        triton.__path__[0] + "/backends/amd/driver.py",
        triton.__path__[0] + "/backends/nvidia/driver.py",
        triton.__path__[0] + "/backends/driver.py",
    ]
    for file in files:
        with open(file, 'r') as f:
            new_all_lines = []
            for line in f.readlines():
                line = line.replace("import torch", "import use_triton_in_paddle as torch")
                new_all_lines.append(line)
            with open(file, 'w') as f:
                f.writelines(new_all_lines)
