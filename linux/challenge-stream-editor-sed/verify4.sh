#!/bin/zsh

result=`diff result3.txt /tmp/verify4.txt | wc -l`
if [ $result -eq 0 ];then
	exit 0
else
	exit 1
fi