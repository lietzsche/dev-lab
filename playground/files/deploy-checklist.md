# 배포 점검 체크리스트 (Deploy Checklist)

1. **디스크 및 메모리 여유 확인**
   - `df -h`로 루트 파일시스템 사용량이 80% 미만인지 확인
   - `free -h`로 `available` 메모리가 충분한지 확인
2. **기존 프로세스 및 포트 확인**
   - `ss -tulnp`로 대상 포트 점유 상태 확인
3. **설정 파일 검증**
   - `application-prod.yml`의 DB 풀 크기 및 타임아웃 설정 확인
4. **기동 후 헬스체크**
   - `curl -i http://localhost:18080/health` 응답이 `200 OK`인지 검증
   - `tail -f`로 초기 에러 로그가 없는지 30초간 모니터링
