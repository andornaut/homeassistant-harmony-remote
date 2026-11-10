ARG NODE_VERSION=24.21.0
ARG PYTHON_VERSION=3.12
FROM node:${NODE_VERSION} AS node
FROM python:${PYTHON_VERSION} AS python
FROM koalaman/shellcheck:v0.11.0 AS shellcheck
FROM kicad/kicad:10.0.8
USER root
COPY --from=python /usr/local /opt/python
ENV LD_LIBRARY_PATH=/opt/python/lib
COPY --from=node /usr/local /opt/node
COPY --from=shellcheck /bin/shellcheck /usr/local/bin/shellcheck
ENV PATH="/opt/node-deps/node_modules/.bin:/opt/node/bin:/opt/venv/bin:${PATH}" \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1
COPY package.json package-lock.json /opt/node-deps/
RUN cd /opt/node-deps && HUSKY=0 npm ci --no-audit --no-fund && chmod -R a+rX /opt/node-deps
COPY requirements-dev.txt /opt/check/requirements-dev.txt
RUN /opt/python/bin/python3 -m venv /opt/venv && /opt/venv/bin/python -m pip install -r /opt/check/requirements-dev.txt
COPY tests/container/check /opt/check/run
COPY --chmod=0644 tests/container/check-yaml.py /opt/check/check-yaml.py
WORKDIR /work
USER 19001:19001
