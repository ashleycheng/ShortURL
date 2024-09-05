FROM python:3.8.8

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

EXPOSE 8000

VOLUME /usr/src/app/log

COPY . .

# Copy docker-entrypoint.sh
RUN mv ./docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

RUN pip install pip -U
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "docker-entrypoint.sh" ]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
