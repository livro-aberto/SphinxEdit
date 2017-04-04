# SphinxEdit

A collaborative platform to write books based on git


## Installation

These are some installation instructions (for Debian):

    sudo apt-get install python python-pip python-dev python-virtualenv

    sudo apt-get install libapache2-mod-wsgi

    sudo apt-get install poppler-utils

    sudo apt-get install libffi-dev libssl-dev python-bcrypt

    virtualenv vir
    source vir/bin/activate

when needed use `deactivate` to exit the virtualenv

    pip install -r requirements.txt

Create config file

    cp conf_default.py conf.py

    cp conf/conf_default.py conf/conf.py

edit the `conf.py` file. Specially:

    Change your secret key


