
FROM python:3.5-slim
ADD . /root/pinnacle/
RUN pip install -r /root/pinnacle/requirements.txt
WORKDIR /root/pinnacle/
RUN python setup.py install