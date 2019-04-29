#!/bin/sh

#musl-gcc -static exp.c -o poc
#strip --strip-all poc
cp ./poc coref/tmp
./gen_initramfs_list.sh coref/ > filelist
./gen_init filelist > core.cpio
gzip core.cpio
