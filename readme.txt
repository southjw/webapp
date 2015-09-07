开始学习git:
git init 创建git版本库
git add file 提交前的操作
git commit -m"notes" 提交
git status 查看状态
git diff file 查看差异

版本回退
git log 查看历史版本,增加参数 --pretty=oneline
git reset --hard HEAD^ 回退一次
git reset --hard HEAD~N 回退N次
git reset --hard id redo操作

git reflog 查看每次命令

