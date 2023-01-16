#!/bin/bash
cd $CODE_DIR
docker run -e CODE_DIR -v ${PWD}:${PWD}  -i  scanmycode/scanmycode3-ce:worker-cli /bin/sh -c 'cd $CODE_DIR && checkmate init'
docker run -e CODE_DIR -v ${PWD}:${PWD}  -i  scanmycode/scanmycode3-ce:worker-cli /bin/sh -c 'cd $CODE_DIR && checkmate git init'
docker run -e CODE_DIR -v ${PWD}:${PWD}  -i  scanmycode/scanmycode3-ce:worker-cli /bin/sh -c 'cd $CODE_DIR && checkmate git analyze --branch `git rev-parse --abbrev-ref HEAD`'
docker run -e CODE_DIR -v ${PWD}:${PWD}  -i  scanmycode/scanmycode3-ce:worker-cli /bin/sh -c 'cd $CODE_DIR && checkmate issues html'
