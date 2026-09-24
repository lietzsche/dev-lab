FROM python:3.12-slim-bookworm

# 기본 필수 유틸리티 및 Git 설치
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    bash \
    tree \
    vim \
    nano \
    less \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Git 전역 기본 설정
RUN git config --global user.name "Learner" \
    && git config --global user.email "learner@devlab.local" \
    && git config --global init.defaultBranch main \
    && git config --global core.editor "vim"

# 분석 도구 및 엔트리포인트 스크립트 복사
COPY scripts/inspect_object.py /usr/local/bin/inspect_object
RUN chmod +x /usr/local/bin/inspect_object

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 작업 디렉터리 준비
WORKDIR /workspace

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]
