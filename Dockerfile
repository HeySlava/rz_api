FROM python:3.10-slim-bullseye

ARG RZ_USER=app
ARG RZ_HOME=/opt/app

RUN useradd -ms /bin/bash -d $RZ_HOME $RZ_USER
ENV PATH="$RZ_HOME/.local/bin:$PATH"

USER $RZ_USER 

WORKDIR $RZ_HOME

COPY --chown=$RZ_USER:$RZ_USER requirements.txt requirements.txt

RUN pip install pip -U --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY --chown=$RZ_USER:$RZ_USER . .

CMD ["python",  "main.py"]
