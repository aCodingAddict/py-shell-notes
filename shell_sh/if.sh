#!/usr/bin/env bash

<<'comment'
shell 的 if 是 0 为真,不支持直接用0 或其他整数变量直接 if,但支持字符串变量直接 if
1.
if [[ expression ]];then
    command
else
    command
fi
2.
[ expression ] && command
&&可以理解为 then,如果左边的表达式为真则执行右边的语句
3.
test 可以替换 [[ ]]
test expression && command
或者
if test expression
then
    command
fi
comment

A=1
B=1
#1
if [[ ${A} = ${B} ]];then
    echo '1'
else
    echo '-1'
fi
#2
[[ ${A} = ${B} ]] && echo '2'
#3
test ${A} = ${B} && echo '3'
#4
if test ${A} = ${B}
then
    echo '4'
fi

<<'comment'
[[ $STR1 = STR2 ]] 当两个串有相同内容、长度时为真
[[ -n $STR1 ]] 当串的长度大于0时为真(串非空)
[[ -z $STR1 ]] 当串的长度为0时为真(空串)
[[ $STR1 ]] 当串STR1为非空时为真
注意:STR1 和 STR2 都是带""的,否则 "$STR1"

[[ int1 -eq int2 ]]  int1 = int2
[[ int1 -ne int2 ]]  int1 != int2
[[ int1 -ge int2 ]]  int1 >= int2
[[ int1 -gt int2 ]]  int1 > int2
[[ int1 -le int2 ]]  int1 <= int2
[[ int1 -lt int2 ]]  int1 < int2

-e (exist)
-e filename, 判断文件是否存在
 
-d (directory)
-d filename，判断文件是否为目录
 
-f (file)
-f filename，判断文件是否为常规文件
 
-L (link)
-L filename，判断文件是否问链接文件
 
-r (read)
-r filename，判断文件是否可读
 
-w (write)
-w filename，判断文件是否可写
 
-x (exec)
-x filename,判断文件是否可执行
 
-s (size)
-s filename，判断文件存在且非空
 
-h (hard link)
-h filename,判断文件是否为硬链接文件
 
-nt (newer than)
filename1 -nt filename2，判断文件1是否比文件2新
 
-ot (older than)
filename1 -ot filename2，判断文件1是否比文件2旧

! 非
-a 与
-o 或
comment

STR1='A'
STR2='A'
STR3='A '
STR4='B'
STR5=''

[[ ${STR1} = ${STR2} ]] && echo '1'
[[ ${STR1} = ${STR3} ]] && echo '2'
[[ ${STR1} = ${STR4} ]] && echo '3'
[[ -n ${STR1} ]] && echo '4'
[[ -n ${STR5} ]] && echo '5'
[[ -z ${STR5} ]] && echo '6'
[[ ${STR1} -lt ${STR2} ]] && echo '7'


[[ -f ./awk.sh ]] && echo 'exist'

