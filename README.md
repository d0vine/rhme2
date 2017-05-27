# rhme2
Riscure Embedded CTF (RHME2) solutions/helper tools. 

Getting started
===============

Filesystem
----------

The solution relies on the "hashpump" python library, to install it on Mac OS use:

```$ pip install --global-option=build_ext --global-option="-L/usr/local/opt/openssl/lib" --global-option="-I/usr/local/opt/openssl/include" hashpumpy```

I know the solution isn't perfect (with magic sleep synchronization and all), but it suffices. Feel free to play around with it ;)