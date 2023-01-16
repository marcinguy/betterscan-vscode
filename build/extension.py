# Built using vscode-ext

import sys

import vscode
import subprocess


ext = vscode.Extension(name="Betterscan", display_name="Betterscan", version="0.0.1")



@ext.event
def on_activate():
    return f"The Extension '{ext.name}' has started"


@ext.command()
def betterscan_scan():
    subprocess.call(["bash","-c","$BETTERSCAN_HOME/cli-html.sh"])





def ipc_main():
    globals()[sys.argv[1]]()

ipc_main()
