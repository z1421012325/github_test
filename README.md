
------------------------------------------------------------------------
![狗头开头](https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1570932373577&di=fcd487f87fae14b117537440d792ced7&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201512%2F15%2F20151215093729_e3wPv.jpeg)

使用git的一些反响

如果在github上做一个仓库来使用的话... 首先手动在github上创建一个空的仓库,默认没有任何东西的

使用git的命令  git pull 创建的github仓库地址     能把创建的空仓库拉下来

或者直接在本地项目有文件下 使用 git init 在项目文件中创建一个隐藏的.get文件(,用来版本控制的)需要上传远程仓库的情况下情况和创建一个空仓库差不多 

使用git remote add origin2(这个可以随意其名字 只不过上传远程仓库时指定为这个名字就可以了) 其他仓库地址   这个情况在以后的情况 使用git push origin2(起的名字) master(分支) 能上传到其他仓库 或者 本地文件但是不知道上传到那个仓库 可以使用这个连接远程仓库,

其中还可以对骚操作,比如将这个本地仓库的东西上传的其他远程仓库中

----------------------------------------------------------------------------------------
简化一下流程把

----------------------------------------------------------------------------------------
下面则是默认在github上创建一个远程的空仓库

git pull 仓库地址   >>>>>>>> 下载空仓库,注意git clone时下载克隆项目,但是没有包含版本控制的一些信息

在这个仓库中创建项目,开发,如果需要保存 

使用 git add * 保存全部文件到暂存区,但是还没有提交的本地仓库

使用 git commit -m "本次提交信息" 提交到本地仓库中

上传到远程仓库中使用 默认情况下使用 git push origin master  >>>>>保存到master主支,如果其他分支则git oush origin 分支名(没有则会由仓库创建)

其中git push 的意思是上传 但是origin是什么意思? 其实使用git remote 能看到有一个origin 默认就是你pull下来仓库的远程地址, 如果需要可以使用 git remote add origin1 其他远程仓库地址 创建一个连接其他仓库的上传 ,上传到其他仓库使用 git push origin1 master(主分支) 就能上传到其他仓库

如果多人协作情况下,最开始将项目pull下来在其中开发内容,想要将其合并,可以直接pull拉去最新的仓库,将本地仓库合并(pull 可以理解为git fetch和merge的两项操作)可以得到合并之后的版本,然后在将push到远程仓库中去.注意文件冲突问题,手动解决冲突 并再次add,commit和push到远程仓库去.



----------------------------------------------------------------------------------------
下面则是 本地已有项目上传至远程仓库

github上创建一个空仓库但是并不pull拉取

本地文件开发过程中使用 git inti 初始化项目文件为一个本地仓库

使用 git add *  和 git commit -m "提交信息" 存在本地

使用git remote add origin 远程地址   连接远程仓库地址作为上传仓库地址

上传 git push origin master(或者分支)









----------------------------------------------
一些常用的git命令
----------------------------------------------
git pull 地址         拉去远程仓库文件(是仓库中的文件,不是文件夹),但需要git init 初始化文件夹(mkdir创建一个)但是没有远程仓库的地址,不能修改后直接push上传到远程仓库中区,只能使用git remote add origin 远程地址  设置为上传地>址


git clone 地址        克隆远程仓库文件夹连同文件一起下载,不需要mkdir创建文件夹

git push origin master(或者分支)     上传到远程中,可以选择是否主支还是分支(分支没有默认创建)

git status            查看文件状态

git add *             保存文件到暂存区

git commit -m "提交信息"        提交到本地仓库

git branch xxx        创建一个本地分支xxx

git branch -d xxx     删除本地分支

git branch -D xxx     强制删除本地分支

git checkout -b xxx   跳转到本地分支,如果没有-b创建

git checkout xxx      跳转本地分支

git push origin --delete xxx    删除远程分支

git merge xxx         合并分支

git log              查看版本和提交信息

git reset --hard 版本号         回退到该版本,使用git log 查看版本或者远程仓库中的commit提交信息中查看



