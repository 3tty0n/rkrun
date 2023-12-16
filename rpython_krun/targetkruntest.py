from rkrun import c_krun_init

def rffi_test():
    c_krun_init()


def entry_point(argv):
    rffi_test()
    return 0

# Add LD_LIBRARY_PATH=/path/to/libkrun when running a program
def target(*args):
    c_krun_init()
    return entry_point
