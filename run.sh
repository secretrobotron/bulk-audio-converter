#!/bin/sh
IMAGE=secretrobotron/bulkaudioconverter
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" "$@"
