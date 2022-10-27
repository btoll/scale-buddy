FROM python:3.11.0-slim-bullseye

RUN useradd \
    --create-home \
    --home-dir /home/noroot \
    noroot

USER noroot

WORKDIR /home/noroot

RUN mkdir scale_buddy

COPY setup.py .
COPY scale_buddy/ ./scale_buddy

ENTRYPOINT ["python", "scale_buddy/main.py"]

