#!/bin/bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.25.4/install.sh | bash
. ~/.nvm/nvm.sh

array=( 0.12.0 iojs-v1.0.0 iojs-v2.5.0 )
for i in "${array[@]}"
do
    nvm install $i
    npm install
    grunt
    grunt clean
done

nvm use system
nvm deactivate
