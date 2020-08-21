#!/bin/bash

sum=0
for arg; do
    re='^[0-9|¥-]+$'
    if [[ $arg =~ $re ]] ; then
        sum=$(($sum+$arg))
    fi
done

echo $sum