# AI-ManualOps 서브모듈 구조

## 1. 코어 모듈

### 1.1 차원 변환 엔진 (Dimension Engine)
- **역할**: 비정형 매뉴얼을 구조화된 DSL로 변환
- **주요 기능**:
  - 텍스트/표/이미지 등 비정형 데이터 처리
  - LLM + Vision 모델 통합
  - DSL 자동 생성
  - 문맥 정규화
- **의존성**:
  - OpenAI GPT, Claude, HuggingFace Transformers
  - Donut/MMGPT (Vision 모델)

### 1.2 에이전트 오케스트레이터 (Agent Orchestrator)
- **역할**: 다중 에이전트 시스템 조율
- **주요 기능**:
  - 에이전트 생명주기 관리
  - 에이전트 간 통신 조율
  - 작업 분배 및 우선순위 관리
  - 에이전트 상태 모니터링
- **의존성**:
  - LangGraph / AutoGen / CrewAI
  - Elixir/OTP GenServer

### 1.3 MCP 통합 레이어 (MCP Integration Layer)
- **역할**: MCP 프로토콜 기반 도구 통합
- **주요 기능**:
  - MCP 서버 연결 관리
  - 도구 호출 추상화
  - JSON-RPC 메시징
  - SSE 기반 스트리밍
- **의존성**:
  - MCP 서버 구현체
  - Pythonx / python-erlastic

## 2. 에이전트 모듈

### 2.1 구조화 전문가 (Structure Specialist)
- **역할**: 매뉴얼 구조 분석 및 변환
- **주요 기능**:
  - 문서 구조 파싱
  - 계층 구조 추출
  - 관계 매핑
  - 구조 검증

### 2.2 의미 통역사 (Semantic Interpreter)
- **역할**: 의미 기반 매뉴얼 해석
- **주요 기능**:
  - 의미 분석
  - 컨텍스트 이해
  - 의도 파악
  - 모호성 해결

### 2.3 절차 감독관 (Procedure Supervisor)
- **역할**: 절차 검증 및 관리
- **주요 기능**:
  - 절차 검증
  - 순서 확인
  - 예외 처리
  - 피드백 제공

### 2.4 위험 평가사 (Risk Assessor)
- **역할**: 위험 요소 식별 및 평가
- **주요 기능**:
  - 위험 식별
  - 영향 평가
  - 완화 전략 제안
  - 모니터링

### 2.5 응답 설계자 (Response Architect)
- **역할**: 사용자 응답 생성
- **주요 기능**:
  - 응답 템플릿 관리
  - 컨텍스트 기반 응답 생성
  - 개인화
  - 피드백 통합

## 3. 인프라 모듈

### 3.1 벡터 데이터베이스 관리자 (Vector DB Manager)
- **역할**: Qdrant 기반 벡터 데이터 관리
- **주요 기능**:
  - 임베딩 저장 및 검색
  - 메타데이터 관리
  - 인덱스 최적화
  - 백업 및 복구
- **의존성**:
  - Qdrant
  - qdrant-client (Python)
  - Qdrant Elixir 클라이언트

### 3.2 모니터링 시스템 (Monitoring System)
- **역할**: 시스템 모니터링 및 알림
- **주요 기능**:
  - 성능 메트릭 수집
  - 리소스 사용량 모니터링
  - 알림 관리
  - 로그 분석
- **의존성**:
  - OpenTelemetry
  - Phoenix LiveDashboard

### 3.3 인증 및 권한 관리 (Auth & Permission)
- **역할**: 보안 및 접근 제어
- **주요 기능**:
  - 사용자 인증
  - 권한 관리
  - API 키 관리
  - 감사 로깅
- **의존성**:
  - JWT / OAuth2
  - Elixir Guardian

## 4. 통합 모듈

### 4.1 Elixir-Python 브릿지 (Elixir-Python Bridge)
- **역할**: Elixir와 Python 간 통신
- **주요 기능**:
  - 프로세스 관리
  - 데이터 직렬화/역직렬화
  - 오류 처리
  - 성능 최적화
- **의존성**:
  - Pythonx
  - python-erlastic
  - Port / NIF

### 4.2 API 게이트웨이 (API Gateway)
- **역할**: 외부 API 통합
- **주요 기능**:
  - API 라우팅
  - 요청/응답 변환
  - 캐싱
  - 속도 제한
- **의존성**:
  - Phoenix
  - HTTPoison

### 4.3 이벤트 버스 (Event Bus)
- **역할**: 이벤트 기반 통신
- **주요 기능**:
  - 이벤트 발행/구독
  - 메시지 큐 관리
  - 이벤트 필터링
  - 백프레셔 처리
- **의존성**:
  - Phoenix PubSub
  - RabbitMQ / Kafka

## 5. 유틸리티 모듈

### 5.1 로깅 시스템 (Logging System)
- **역할**: 통합 로깅
- **주요 기능**:
  - 구조화된 로깅
  - 로그 수집
  - 로그 분석
  - 로그 보관
- **의존성**:
  - Logger
  - Telemetry

### 5.2 설정 관리자 (Config Manager)
- **역할**: 시스템 설정 관리
- **주요 기능**:
  - 환경별 설정
  - 동적 설정 변경
  - 설정 검증
  - 비밀 관리
- **의존성**:
  - Config
  - Vault

### 5.3 테스트 프레임워크 (Test Framework)
- **역할**: 테스트 자동화
- **주요 기능**:
  - 단위 테스트
  - 통합 테스트
  - 성능 테스트
  - 테스트 보고서
- **의존성**:
  - ExUnit
  - Mox
  - Wallaby 