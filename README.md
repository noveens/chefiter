# Chefitter

##Install the Web2py Software
Your Ubuntu server instance should already come with Python installed by default. This takes care of one of the only things that web2py needs to run successfully.

The only other software that we need to install is the unzip package, so that we can extract the web2py files from the zip file we will be downloading:

```
sudo apt-get update
sudo apt-get install unzip
```

Now, we can get the framework from the project's website. We will download this to our home folder:

```
cd ~
wget http://www.web2py.com/examples/static/web2py_src.zip
```

Now, we can unzip the file we just downloaded and move inside:

```
unzip web2py_src.zip
cd web2py
```

Now that we are inside the web2py directory, how do we install it? Well, one of the great things about web2py is that you do not install it. You can run it right from this folder by typing:

```
python web2py.py
```

This will launch the web2py server, now simply goto: 

/views/default/home.html page
