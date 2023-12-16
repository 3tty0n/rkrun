# RKrun

RPython extention for [krun](https://github.com/softdevteam/krun).

## Prerequisite

- Krun and built `libkrun`

## Usage

```shell
rpython -Ojit targetkruntest.py

LD_LIBRARY_PATH=/path/to/libkrun ./targetkruntest-c
```
