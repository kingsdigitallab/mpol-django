FROM python:${PYTHON_VERSION:-3.8-slim-bookworm}

ARG APP_HOME=/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN addgroup --system django \
  && adduser --system --ingroup django django

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # ldap dependencies
  libldap2-dev libsasl2-dev ldap-utils \
  # lxml dependencies
  libxml2-dev libxslt-dev python3-dev \
  # pillow dependencies
  libjpeg-dev libpng-dev zlib1g-dev \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

WORKDIR ${APP_HOME}

COPY ./volumes/django/requirements.txt /requirements/
RUN pip install --no-cache-dir -U pip \
  && pip install --no-cache-dir -r /requirements/requirements.txt

COPY --chown=django:django ./compose/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint \
  && chmod +x /entrypoint

RUN mkdir -p ${APP_HOME}/logs \
  && mkdir -p ${APP_HOME}/static/media \
  && chown -R django:django ${APP_HOME} \
  && chmod -R 775 ${APP_HOME}/logs \
  && chmod -R 775 ${APP_HOME}/static

USER django

ENTRYPOINT ["/entrypoint"]
