FROM python:3.9.6-alpine3.14

# copy src code
RUN mkdir /code
WORKDIR /code/

# just copy the requirements file and install
ADD requirements.txt /code/requirements.txt
# installing project requirements
RUN pip install -r requirements.txt

# add the rest of code
ADD . /code/    

# Making CLI executable
RUN chmod +x /code/kv
RUN cp /code/kv /usr/local/bin

# makes sure logs are not missing when system crashes
ENV PYTHONUNBUFFERED 1

EXPOSE 5000

RUN adduser keystore -D

RUN chown -R keystore /code

USER keystore

CMD ["gunicorn", "-w", "1", "--thread", "5", "-b", "0.0.0.0:5000", "main:app"]