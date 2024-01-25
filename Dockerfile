FROM python:3.11.0-slim-bullseye

RUN useradd \
    --create-home \
    --home-dir /home/noroot \
    noroot

USER noroot

ENV PATH="$PATH":/home/noroot/.local/bin

WORKDIR /home/noroot

COPY setup.py setup.cfg ./
COPY scale-buddy/ ./scale-buddy

RUN pip3 install --editable .

ENTRYPOINT ["scale-buddy"]

