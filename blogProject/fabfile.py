from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/Eddliy/django-blog.git"

env.user = 'eddie'
env.password = 'qwmj433QP'

# 填写你自己的主机对应的域名
env.hosts = ['111.67.197.68']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/eddie/sites/111.67.197.68/django-blog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip3 install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('systemctl restart eddie.service')
    sudo('service nginx reload')
