#!/usr/bin/env python3
#coding:utf-8
import subprocess


def main():
    """
    just a simple one step script to start the server and client
    if under the system the command for python3 is just python,
    modify the commandTemplate to 'python {}'
    
    Also in this start script, the multiprocess is used.
    There is a chance that client has already finished started up and server is still starting
    and in the very first couple of seconds client end seem to have no data
    don't panic, wait for a couple of more seconds till the server start up and client side would get the data cause client side keep requesting periodically
    """
    commandTemplate = 'python {}'
    processes = [
        subprocess.Popen(commandTemplate.format(target), shell=True)
        for target in ['server.py', 'a3.py']
    ]
    [_.wait() for _ in processes]


if __name__ == "__main__":
    main()
