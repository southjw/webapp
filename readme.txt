开始学习git:
git init 创建git版本库
git add file 提交到暂存区
git commit -m"notes" 提交
git status 查看状态
git diff file 查看差异

版本回退
git log 查看历史版本,增加参数 --pretty=oneline
git reset --hard HEAD^ 回退一次
git reset --hard HEAD~N 回退N次
git reset --hard id redo操作

git reflog 查看每次命令

git reset HEAD file 把暂存区的修改撤销掉
git checkout -- readme.txt 撤销修改

rm file 删除文件
git rm file 删除版本中文件
git checkout -- file 版本库里的文件替换工作区的文件

创建远程仓库(github)  
ssh-keygen -t rsa -C "youremail@example.com" 创建SSH Key
参考网址：http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374385852170d9c7adf13c30429b9660d0eb689dd43a000

要关联一个远程库，使用命令git remote add origin git@server-name:path/repo-name.git；
关联后，使用命令git push -u origin master第一次推送master分支的所有内容；
此后，每次本地提交后，只要有必要，就可以使用命令git push origin master推送最新修改；