# RKrun

RPython extention for [krun](https://github.com/softdevteam/krun).

## Prerequisite

- Krun and built `libkrun`

## Usage

```shell
rpython -O2 rpython_krun/targetkruntest.py

LD_LIBRARY_PATH=/path/to/libkrun ./targetkruntest-c
```
