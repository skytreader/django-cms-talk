# The Slides, In Detail

I'd assume you are using a \*nix-like environment. The commands work for Ubuntu 12.04 but
adapting them for your distro of choice should be trivial.

**Help! I'm getting all sorts of weird errors installing MySQL-python!**

Yep. It's really not as easy as it looks. Here's how I do it:

  1. Install MySQL dev headers: `sudo apt-get install libmysqlclient-python`.
  2. If you don't have it yet, you may also need Python's dev headers: `sudo apt-get install python-dev`.
  3. Pip should install fine now: `pip install MySQL-python`.
      - MySQL-python requires a more-recent distribute library than the one that ships by
        default in Ubuntu 12.04 . I ran into all sorts of problems upgrading distribute because,
        apparently, my global Python environment (the one outside virtualenvs) uses the shipped
        version of distribute. I just had to upgrade the distribute in my global Python
        environment.  
        **Warning:** In case the distribute update you are installing is not
        backwards-compatible, this may break some things; proceed at your own risk.

**You recommend not using sqlite for trying out Django CMS. Can I use DB engine _x_?**

As long as it supports `ALTER TABLE` statements, you're good. But then, there's also the question
of having a Django DB backend for your flavor of choice...

**Where to now?**

[Check this out!](https://github.com/pythonph/pyph-web)
