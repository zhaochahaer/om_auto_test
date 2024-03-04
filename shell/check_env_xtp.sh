#!/bin/bash

# 检查XTP数据库健康状况
function check {
    result=$(su - qianbase -c "qadm node-status" 2>&1)
    if [[ $result == *"cannot dial server"* ]]; then
        echo "Error: 无法连接到数据库，请自行检查数据库状态。"
    else
        health_statuses=$(echo "$result" | awk '{ if ($11 != "") print $11 }')
        all_true=true
        for value in $health_statuses
        do
            if [ $value != "true" ]; then
                all_true=false
                break
            fi
        done
        if [ $all_true = true ]; then
            echo "Success: 所有节点健康状态正常"
        else
            echo "Error: 存在节点健康状态异常"
        fi
    fi
}

# 执行检查
check
