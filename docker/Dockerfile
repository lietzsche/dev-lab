FROM bash:5.2-alpine

RUN apk add --no-cache coreutils findutils grep sed gawk procps util-linux strace shellcheck

COPY docker/entrypoint.sh /usr/local/bin/bash-lab-entrypoint
RUN chmod +x /usr/local/bin/bash-lab-entrypoint

WORKDIR /lab/workspace
ENTRYPOINT ["bash-lab-entrypoint"]
CMD ["tail", "-f", "/dev/null"]
