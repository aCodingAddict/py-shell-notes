#!/usr/bin/env bash

<<'comment'
curl是利用URL语法在命令行方式下工作的开源文件传输工具

-X 指定http的请求方法HEAD，GET，POST，PUT，DELETE
-d 指定要传输的数据
-H 指定http请求头信息

使用时最好带-H "Content-Type：application/json"
comment