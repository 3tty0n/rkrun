from rpython.rtyper.lltypesystem import rffi, lltype
from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.rlib.rarithmetic import r_int32, r_int64, r_longlong

eci = ExternalCompilationInfo(includes=['stdint.h', 'time.h', 'stdlib.h', 'errno.h', 'libkruntime.h'],
                              include_dirs=['/home/yusuke/src/github.com/softdevteam/krun/libkrun'],
                              libraries=['kruntime'],
                              library_dirs=['/home/yusuke/src/github.com/softdevteam/krun/libkrun'])

c_krun_init = rffi.llexternal('krun_init',
                              [],
                              lltype.Void,
                              compilation_info=eci)

c_krun_done = rffi.llexternal('krun_done',
                              [],
                              lltype.Void,
                              compilation_info=eci)

c_krun_measure = rffi.llexternal('krun_measure',
                                 [rffi.INT],
                                 lltype.Void,
                                 compilation_info=eci)

c_krun_get_wall_clock = rffi.llexternal('krun_get_wall_clock',
                                         [rffi.INT],
                                         rffi.DOUBLE,
                                         compilation_info=eci)

c_krun_get_core_cycles_double = rffi.llexternal('krun_get_core_cycles_double',
                                                [rffi.INT, rffi.INT],
                                                rffi.DOUBLE,
                                                compilation_info=eci)

def krun_init():
    c_krun_init()


def krun_done():
    c_krun_done()


def krun_measure(mdata_idx):
    c_krun_measure(mdata_idx)


def krun_get_wall_clock(mdata_idx):
    return c_krun_get_wall_clock(mdata_idx)


def krun_get_core_cycles_double(mdata_idx, core):
    return c_krun_get_core_cycles_double(mdata_idx, core)
