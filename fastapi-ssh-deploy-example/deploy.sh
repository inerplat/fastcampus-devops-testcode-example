#!/bin/bash

APP_NAME="calculator-api"
DEPLOY_PATH="/home/$USER"
PID_FILE="$DEPLOY_PATH/app.pid"

echo ">>> 현재 실행 중인 애플리케이션 종료"
if [ -f $PID_FILE ]; then
    CURRENT_PID=$(cat $PID_FILE)
    if ps -p $CURRENT_PID > /dev/null; then
        echo ">>> kill -15 $CURRENT_PID"
        kill -15 $CURRENT_PID
        sleep 5
    fi
fi

echo ">>> 새 애플리케이션 배포"
cd $DEPLOY_PATH
nohup python3 main.py > app.log 2>&1 & echo $! > $PID_FILE

echo ">>> 배포 완료"
