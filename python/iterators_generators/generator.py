def read_logs(fname):

    with open(fname) as f:
        for line in f:
            yield line

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line
