��ʼѧϰgit:
git init ����git�汾��
git add file �ύ���ݴ���
git commit -m"notes" �ύ
git status �鿴״̬
git diff file �鿴����

�汾����
git log �鿴��ʷ�汾,���Ӳ��� --pretty=oneline
git reset --hard HEAD^ ����һ��
git reset --hard HEAD~N ����N��
git reset --hard id redo����

git reflog �鿴ÿ������

git reset HEAD file ���ݴ������޸ĳ�����
git checkout -- readme.txt �����޸�

rm file ɾ���ļ�
git rm file ɾ���汾���ļ�
git checkout -- file �汾������ļ��滻���������ļ�

����Զ�ֿ̲�(github)  
ssh-keygen -t rsa -C "youremail@example.com" ����SSH Key
�ο���ַ��http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374385852170d9c7adf13c30429b9660d0eb689dd43a000

Ҫ����һ��Զ�̿⣬ʹ������git remote add origin git@server-name:path/repo-name.git��
������ʹ������git push -u origin master��һ������master��֧���������ݣ�
�˺�ÿ�α����ύ��ֻҪ�б�Ҫ���Ϳ���ʹ������git push origin master���������޸ģ�