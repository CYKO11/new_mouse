#!/bin/bash
echo " "
if [ $1 ]
then
    if [ $1 == "hard" ]
    then
        echo "hard_deploy"
        ssh pi@192.168.8.200 rm -rf package;
        ssh pi@192.168.8.200 mkdir package;
        scp -r pythonProject pi@192.168.8.200:/home/pi/package
        if [ $2 == "dep" ]
        then
            ssh pi@192.168.8.200 "cd package/pythonProject;./depend.sh"
        fi
        ssh pi@192.168.8.200 "cd package/pythonProject;python learn.py"
    fi
else 
    echo "soft_deploy"
    scp -r pythonProject pi@192.168.8.200:/home/pi/package
    ssh pi@192.168.8.200 "cd package/pythonProject;python learn.py"
    echo "done"
fi
