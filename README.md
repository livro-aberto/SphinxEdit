# SphinxEdit

An online Sphinx editor


## Installation

These are some installation instructions (for Debian or Ubuntu):

    sudo apt-get install python python-pip python-dev python-virtualenv

    sudo apt-get install poppler-utils

    sudo apt-get install libffi-dev libssl-dev python-bcrypt

    virtualenv vir
    source vir/bin/activate

when needed, use `deactivate` to exit the virtualenv.

Then type

    pip install -r requirements.txt

Copy the config files

    cp config_default.py config.py

    cp conf/conf_default.py conf/conf.py

(If you are opening this to the internet, edit the `conf.py` file, specially changing your secret key.)

Run it using

    ./runserver

then access it in your browser through the address:

    http://127.0.0.1:5000/




