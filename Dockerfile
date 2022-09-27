FROM docker.io/library/python:3-slim

# Non-root user for security purposes.
#
# UIDs below 10,000 are a security risk, as a container breakout could result
# in the container being ran as a more privileged user on the host kernel with
# the same UID.
#
# Static GID/UID is also useful for chown'ing files outside the container where
# such a user does not exist.
RUN groupadd --gid 10000 nonroot && \
    useradd  --home-dir /home/nonroot \
             --create-home \
             --shell /bin/bash \
             --gid nonroot \
             --groups nonroot \
             --uid 10000 nonroot
USER nonroot
WORKDIR /home/nonroot/do_nothing_app

COPY . .

CMD [ "python", "./do_nothing_app.py" ]