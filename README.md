# Betterscan-Extension

## **Table of contents**
### 1. [**About**](#about)
### 2. [**Usage**](#usage)
### 3. [**Documentation**](#documentation)
### 4. [**Issues**](#issues)
### 5. [**Contributing**](#contributing)
### 6. [**License**](#license)


## **About**

This repository contains a [**Betterscan CLI**](https://github.com/marcinguy/betterscan-ce) extension for the integrated development environment (IDE) **Visual Studio Code**. With this extension, you will be able to perform a static code analysis (SAST), Code Scanning, Secret scanning also for Cloud Infrastructure (IaC) in search of vulnerabilities.

## **Usage**

### Requirements

You must have [**Docker**](https://www.docker.com/) installed, click [**here**](https://github.com/marcinguy/betterscan-ce) to check more detailed information about **Betterscan-CLI** requirements.

Download [cli-html.sh](https://raw.githubusercontent.com/marcinguy/betterscan-vscode/master/cli-html.sh)

`curl https://raw.githubusercontent.com/marcinguy/betterscan-vscode/master/cli-html.sh --output cli-html.sh`

Make it executable (`chmod a+x cli-html.sh`)

Set environmental variable `BETTERSCAN_HOME` to folder you saved the file

`export BETTERSCAN_HOME=/home/user`

That's it

### Executing an analysis

Ctrl-P and then type > Betterscan Scan

## **Documentation**

For more information about Betterscan, please check out the [**documentation**](https://betterscan.io).

## **Issues** 

To open or track an issue for this project, in order to better coordinate your discussions, we recommend that you use the [**Issues tab**](https://github.com/marcinguy/betterscan-ce/issues) in the main [**Betterscan-CLI**](https://github.com/marcinguy/betterscan-ce) repository.

## **Contributing**

If you want to contribute to this repository, access our [**Contributing Guide**](https://github.com/marcinguy/betterscan-ce/blob/master/CONTRIBUTING.md). 

## **License**
Apache License 2.0
