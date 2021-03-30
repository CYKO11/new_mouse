#!/bin/bash

git add .
git commit -m "$1"
git push
ssh pi@192.168.8.120 "curl localhost:8080/kill;cd RPIzero-autodeploy; git reset --hard; git pull; cd node; node server.js"