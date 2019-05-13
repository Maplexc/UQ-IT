This assignment project is based on client, server architecture,
Base on Ubuntu 18.04 and http v1.1
Please do start the server before running the client,
It can be done in two options:
(1)run: python3 server.py and then run python3 a3.py
(2)run: python3 start.py

The server is running in port 8080, please make the 8080 port available
if it is needed to switch to another port,
Firstly go to the server.py,
in line 117 which is server.listen(8080), modify 8080 to the port
Secondly goto model.py,
in line 119, which is the URL_PREFIX = 'http://localhost:8080/{}' modify the 8080 to the port

Also there are several third party libraries which are the dependencies of this project

If installations of these third party libraries are in need, please make sure
that the administration access is obtained.
It is highly recommended to install them in a virtual python3 environment
simply run: python3 setup.py install
to finish the third party libraries installed.
Further details please visit extensions.doc
