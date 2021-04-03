#!/bin/bash

if [ $1 == "server" ]
then
    while [ $1 ]
    do
        # server setup
        python3 ./server/main.py &

        echo "press enter to restart server"
        read
        
        if [ ${REPLY} == "exit" ]
        then
            exit
        fi
    done
else
    if [ $1 ]
    then
        while [ $1 ]
        do
            # $1 = ip address
            ssh pi@$1 rm -rf package
            ssh pi@$1 mkdir package
            scp -r client pi@$1:/home/pi/package

            # $2 = dep / nodep
            if [ $2 == "dep" ]
            then
                ssh pi@$1 sudo apt-get install python-smbus
                ssh pi@$1 pip3 install board
                ssh pi@$1 pip3 install adafruit-circuitpython-ads1x15
            fi

            echo "running script"
            ssh pi@$1 "python3 package/client/main"

            echo ""
            echo "press enter to redeploy client"
            read

            if [ ${REPLY} == "exit" ]
            then
                exit
            fi
        done
    else
        echo "error : no ip specified"
        read
    fi
fi