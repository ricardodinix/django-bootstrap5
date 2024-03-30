FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y
RUN pip install --upgrade pip setuptools wheel
RUN pip install poetry && poetry cache clear pypi --all
RUN apt-get install libaio1 -y
RUN mkdir /opt/oracle  \
    && cd /opt/oracle  \
    && wget https://download.oracle.com/otn_software/linux/instantclient/1918000/instantclient-basic-linux.x64-19.18.0.0.0dbru.zip  \
    && unzip instantclient-basic-linux.x64-19.18.0.0.0dbru.zip
RUN sh -c "echo /opt/oracle/instantclient_19_18 > /etc/ld.so.conf.d/oracle-instantclient.conf"
RUN ldconfig
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_19_18:$LD_LIBRARY_PATH
RUN poetry config virtualenvs.create false
RUN poetry install