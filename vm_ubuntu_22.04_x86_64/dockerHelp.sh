#!/bin/bash

# syntax: dr-cmd <container> <command>
dr-cmd() {
    docker exec -it $1 "${@:2}"
}

# syntax: dr-run <image>
dr-run() {
    docker run -it $1 /bin/sh
}

# syntax: dr-sh <container>
dr-sh() {
   docker exec -it $1 sh
}

# syntax: dr-log <container>
dr-log() {
  docker logs -f $1
}

# syntax: dr-build
dr-build() {
    docker build . -t $1
    docker run -p 8080:$2 $1
}

# syntax: dr-reset
dr-reset() {
    containerId=$(docker ps -a | grep $1 | cut -d" " -f1)
    imageId=$(docker inspect --format='{{.Image}}' $containerId)
    docker rm $containerId -f  && docker rmi $imageId
}

# syntax: dr-run-dead
dr-run-dead() {
  docker commit $1 $1-image > /dev/null
  docker run -it $1-image$*
}

# syntax: dr-reset-log
dr-reset-log() {
    truncate -s 0 $(docker inspect --format='{{.LogPath}}' $1)
}

# syntax: dr-ps
alias dr-ps='docker ps --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Names}}\t{{.Ports}}"'

# syntax: dr-clean
alias dr-clean='docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q) && docker rmi $(docker images -a -q)'
