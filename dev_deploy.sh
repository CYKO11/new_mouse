#!/bin/bash

echo " "
rm out.txt
if [ $2 ]
then
    while [ $2 ]
    do
        if [ $2 == "dev" ]
        then
            echo "dev_deploy"
            ssh pi@192.168.8.200 rm -rf package;
            ssh pi@192.168.8.200 mkdir package;
            scp -r project pi@192.168.8.200:/home/pi/package
            if [ $3 == "dep" ]
            then
            echo "deploying"
                ssh pi@192.168.8.200 "cd package/project;./depend.sh"
                
            fi
            echo "running script"
            ssh pi@192.168.8.200 "cd package/project;python3 $1.py"
            read
            if [ ${REPLY} == "exit" ]
            then
                exit
            fi
        else
            exit
        fi
    done
else 
    echo "soft_deploy"
    scp -r project pi@192.168.8.200:/home/pi/package
    ssh pi@192.168.8.200 "cd package/project;python3 $1.py" >> out.txt
    echo "done"
fi
