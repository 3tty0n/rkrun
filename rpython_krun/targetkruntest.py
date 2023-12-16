from rkrun import krun_init

def rffi_test():
    krun_init()


def entry_point(argv):
    rffi_test()
    return 0

# Add LD_LIBRARY_PATH=/path/to/libkrun when running a program
def target(*args):
    return entry_point
