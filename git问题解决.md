[TOC]

#### git显示中文

通过将Git配置变量 core.quotepath 设置为false，就可以解决中文文件名称在这些Git命令输出中的显示问题，

​        示例：

​                `$ git config --global core.quotepath false`

​                `$ git status -s`

#### 备份, 解决冲突

`git stash`备份当前工作区的内容, 从最近一次提交哦中读取内容



#### 查看单个文件修改记录

- git log -p 文件名



#### LF 换行符不统一

`建议：统一换行符为 LF 方案： Git 命令行输入如下命令，禁止自动转换换行符`

- git config --global core.autocrlf false

