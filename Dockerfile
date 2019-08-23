FROM 303363518858.dkr.ecr.ap-southeast-1.amazonaws.com/belong/base:py3
ADD ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt
ADD . /code
WORKDIR /code
RUN python manage.py collectstatic --noinput
RUN chown -R deployuser:deployuser /code
USER deployuser