#!/bin/bash

name=$(basename $PWD)
docker images | grep -q $name
if [[ $? -eq 1 ]] ; then
  docker build -t ${name}:latest .
fi
docker run -v ./.ipstack_key:/app/.ipstack_key ${name}:latest $1
