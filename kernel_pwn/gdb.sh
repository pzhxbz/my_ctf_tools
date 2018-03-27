gdb            -ex "target remote localhost:1234"       \
               -ex "continue"                           \
               -ex "disconnect"                         \
               -ex "set architecture i386:x86-64:intel" \
               -ex "target remote localhost:1234"       \
	       -ex "add-symbol-file /home/pzhxbz/Desktop/babydriver/babydriver.ko 0xffffffffc0000000" \
	       -ex "b *0xffffffff81063698"

		#-ex "break x86_64_start_kernel"          \
# -ex "b *0xffffffffc0000130"\
