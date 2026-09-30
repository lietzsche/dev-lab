#!/usr/bin/env bash

set -u

printf '%s\n' '== shell execution context =='
printf 'BASH_VERSION=%s\n' "${BASH_VERSION:-not-bash}"
printf 'PID=%s PPID=%s\n' "$$" "${PPID:-unknown}"
printf 'PWD=%q\n' "${PWD}"
printf 'positional_count=%d\n' "$#"
printf 'command_name=%q\n' "$0"

index=1
for argument in "$@"; do
    printf 'argument[%d]=%q\n' "${index}" "${argument}"
    index=$((index + 1))
done

printf '%s\n' '== selected environment =='
printf 'HOME=%q\n' "${HOME:-}"
printf 'PATH=%q\n' "${PATH:-}"
printf 'SHELL=%q\n' "${SHELL:-}"

if [ -d "/proc/$$/fd" ]; then
    printf '%s\n' '== open file descriptors =='
    for descriptor in 0 1 2; do
        target=$(readlink "/proc/$$/fd/${descriptor}" 2>/dev/null || printf '%s' unavailable)
        printf 'fd[%d]=%s\n' "${descriptor}" "${target}"
    done
else
    printf '%s\n' 'FD inspection unavailable: /proc is not mounted.'
fi
