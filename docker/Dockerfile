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

# Git 기본 설정 (Learner 기본 계정 및 main 기본 브랜치)
RUN git config --global user.name "Learner" \
    && git config --global user.email "learner@devlab.local" \
    && git config --global init.defaultBranch main \
    && git config --global core.editor "vim"

# 작업 디렉터리 준비
WORKDIR /workspace

# 컨테이너 시작 시 실행될 쉘
CMD ["/bin/bash"]
