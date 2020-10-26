FROM python:3-alpine

RUN apk update && apk upgrade && apk add git bash wget curl tmux htop openssh openrc nano sysstat

RUN touch /etc/ssh/sshd_config

RUN rc-update add sshd
RUN rc-status
RUN touch /run/openrc/softlevel
RUN /etc/init.d/sshd start

RUN mkdir app
RUN git clone https://github.com/Arslan-Akautdinov/template_flask_api_service.git app