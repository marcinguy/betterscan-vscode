# Built using vscode-ext

import sys

import vscode
import subprocess
import os


ext = vscode.Extension(name="Betterscan", display_name="Betterscan", version="0.0.1")
cwd = os.getcwd()


@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"


@ext.command()
def betterscan_scan1():
    cwd = os.getcwd()
    mount = cwd+":"+cwd

    subprocess.call("docker run -e CODE_DIR -e LIC -v "+mount+" -i scanmycode/scanmycode3-ce:worker-cli /bin/sh -c 'cd $CODE_DIR && git config --global --add safe.directory $CODE_DIR && checkmate init'", shell=True)

def betterscan_scan2():
    cwd = os.environ["CODE_DIR"]
    mount = cwd+":"+cwd
    subprocess.call("docker run -e CODE_DIR -e LIC -v "+mount+" -i scanmycode/scanmycode3-ce:worker-cli /bin/sh -c 'git config --global --add safe.directory $CODE_DIR && cd $CODE_DIR && checkmate git init'",  shell=True)


def betterscan_scan3():
    cwd = os.environ["CODE_DIR"]
    mount = cwd+":"+cwd
    subprocess.call("docker run -e CODE_DIR -e LIC -v "+mount+" -i scanmycode/scanmycode3-ce:worker-cli /bin/sh -c 'git config --global --add safe.directory $CODE_DIR && cd $CODE_DIR && checkmate git analyze --branch `git rev-parse --abbrev-ref HEAD` && checkmate issues html '",  shell=True)



def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
