FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV VIRTUAL_HOST group-adventure.do.freyc.xyz
COPY . .

CMD [ "python", "./app.py" ]
