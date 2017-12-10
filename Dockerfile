FROM centos:7

WORKDIR /

RUN yum -y update all && \
    yum -y install software-properties-common \
          python-software-properties \
          ansible

ADD ansible /ansible

ADD app /app

RUN ansible-playbook -i "localhost," -c local /ansible/main_setup.yml

ENTRYPOINT ["python"]

CMD ["/app/api.py"]

EXPOSE 5000

