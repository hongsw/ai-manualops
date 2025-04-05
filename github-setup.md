# AI-ManualOps 깃허브 설정 가이드

## 레포지토리 설정

### 기본 정보
- **레포지토리 이름**: ai-manualops
- **설명**: 비정형 매뉴얼을 구조화된 DSL로 변환하고 다중 에이전트 시스템을 통해 분석 및 해석하는 AI 시스템
- **가시성**: Public
- **라이선스**: MIT License
- **주제(Topics)**: ai, elixir, python, llm, vector-database, multi-agent-system, mcp, qdrant

### 초기 설정
- README.md 파일 생성
- .gitignore 파일 설정 (Elixir, Python, Node.js 등)
- 라이선스 파일 추가
- 이슈 템플릿 설정
- PR 템플릿 설정
- GitHub Actions 워크플로우 설정

## 이슈 관리 설정

### 이슈 라벨
- **epic**: 큰 기능 단위의 이슈
- **story**: 사용자 관점의 기능 요구사항
- **task**: 구체적인 작업 항목
- **bug**: 버그 수정
- **enhancement**: 기능 개선
- **documentation**: 문서화
- **infrastructure**: 인프라 관련 작업
- **testing**: 테스트 관련 작업
- **research**: 연구 및 조사 작업

### 이슈 우선순위
- **P0**: 즉시 해결 필요 (블로커)
- **P1**: 높은 우선순위 (핵심 기능)
- **P2**: 중간 우선순위 (중요 기능)
- **P3**: 낮은 우선순위 (부가 기능)
- **P4**: 향후 고려 (선택적 기능)

### 이슈 템플릿
- Story 템플릿
- Task 템플릿
- Bug 템플릿

## 프로젝트 보드 설정

### 칸반 보드 구성
- **To Do**: 작업 대기 중
- **In Progress**: 진행 중인 작업
- **Review**: 검토 중인 작업
- **Done**: 완료된 작업

### 마일스톤 설정
- **MVP 개발**: 핵심 기능 개발 (10주)
- **MVP 후 계획**: 추가 기능 개발 (8주)

## 브랜치 전략

### 브랜치 구조
- **main**: 안정적인 프로덕션 코드
- **develop**: 개발 중인 코드
- **feature/**: 기능 개발 브랜치
- **bugfix/**: 버그 수정 브랜치
- **release/**: 릴리즈 준비 브랜치

### 브랜치 네이밍 규칙
- feature/이슈번호-기능명
- bugfix/이슈번호-버그명
- release/버전번호

## 커밋 메시지 규칙

### 커밋 메시지 형식
```
<type>(<scope>): <subject>

<body>

<footer>
```

### 타입 정의
- **feat**: 새로운 기능
- **fix**: 버그 수정
- **docs**: 문서 변경
- **style**: 코드 포맷팅
- **refactor**: 코드 리팩토링
- **test**: 테스트 코드
- **chore**: 빌드 프로세스 또는 보조 도구 변경

## CI/CD 설정

### GitHub Actions 워크플로우
- **테스트**: Elixir 및 Python 테스트 실행
- **린트**: 코드 품질 검사
- **빌드**: 애플리케이션 빌드
- **배포**: 자동 배포 (개발 환경)

## 문서화 가이드라인

### 필수 문서
- README.md: 프로젝트 개요 및 시작 가이드
- CONTRIBUTING.md: 기여 가이드라인
- CHANGELOG.md: 변경 이력
- docs/: 상세 문서

### 문서 구조
- **아키텍처**: 시스템 아키텍처 설명
- **API**: API 문서
- **개발 가이드**: 개발 환경 설정 및 가이드라인
- **배포 가이드**: 배포 프로세스 설명

## 보안 가이드라인

### 보안 정책
- API 키 및 비밀 정보는 환경 변수로 관리
- 민감한 정보는 .env 파일에 저장하고 .gitignore에 추가
- 보안 취약점 발견 시 비공개 이슈로 보고

### 코드 리뷰 가이드라인
- 보안 관련 코드는 특별히 주의하여 리뷰
- 의존성 업데이트 시 보안 취약점 확인
- 코드 스캔 도구 활용 (GitHub Security Alerts) 