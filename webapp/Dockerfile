FROM projectmirror/baseimage:1.0

WORKDIR /webapp
COPY . /webapp

RUN pip3 install -r /webapp/requirements.txt

CMD cd / && python -m webapp.run