FROM jenkins/jenkins:lts

USER root

RUN curl -fsSL https://download.docker.com/linux/static/stable/x86_64/docker-28.3.3.tgz -o docker.tgz \
    && tar -xzf docker.tgz \
    && mv docker/docker /usr/local/bin/docker \
    && chmod +x /usr/local/bin/docker \
    && rm -rf docker docker.tgz

USER jenkins