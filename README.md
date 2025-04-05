# 📘 AI-ManualOps: 차원 변환 기반 AI 업무 매뉴얼 대응 시스템

## 🎯 목표 (Objective)

실시간 업무 행동이 **매뉴얼에 기반한 것인지**, 또는 **긴급 대응의 예외인지**를 AI가 판단하고, 필요한 절차를 안내/검증할 수 있는 **확장 가능한 Agentic AI 시스템**을 구축한다.  
이를 위해 **MCP (Model Context Protocol)**, **Agentic AI 패턴**, **Elixir 기반 분산처리**, **VectorDB 기반 문맥 관리**, 그리고 **컴퓨터 사이언스 기반 인프라 구조**를 통합하여 실행 가능한 설계 및 구현 체계를 제공한다.

---

## 🧱 시스템 구조 핵심 축

### ✅ 1. 차원 변환: Domain Knowledge → 추론 가능한 구조화 표현
- **기능**: 텍스트/표/이미지 등 비정형 매뉴얼 → 절차 DSL로 변환
- **기술**:
  - LLM + Vision (Donut/MMGPT)
  - 벡터화 + 구조 태깅
  - DSL 자동 생성 + 문맥 정규화

### ✅ 2. AI 협력 시스템: Agentic 패턴 + MCP 기반 Tool 사용
- **기능**: 판단 Agent, 긴급성 Agent, 피드백 Agent 분리 운영
- **기술**:
  - LangGraph / AutoGen / CrewAI 등 Agent 프레임워크
  - MCP로 Tool 추상화 및 통신
  - Planner, ReAct, Reflection 등 실행 전략 조합

### ✅ 3. CS 기반 운영 인프라
- **검증**: Self-eval, gold data, 평가 loop  
- **동기화**: 버전 관리 + 임베딩 자동 업데이트  
- **관찰성**: OpenTelemetry, LiveDashboard, log tracing  
- **차원 매핑**: FAISS/Weaviate + 메타데이터 기반 검색

---

## ⚙ 기술 스택 및 통합 전략

| 요소             | 기술/프레임워크 예시                         | 설명 |
|------------------|-----------------------------------------------|------|
| LLM              | OpenAI GPT, Claude, HuggingFace Transformers  | 판단 및 추론 |
| MCP 서버         | `modelcontextprotocol/servers`                | Tool abstraction |
| Agent Framework  | LangGraph, AutoGen, CrewAI, `lastmile-ai/mcp-agent` | 에이전트 분기 및 흐름 제어 |
| Agent Host       | **Elixir/OTP** 기반 GenServer 구조            | 병렬 실행/장애 복구 |
| Vector DB        | FAISS, Qdrant, Weaviate                        | 의미 기반 검색 |
| 관찰/모니터링    | OpenTelemetry, Phoenix LiveDashboard          | 성능 및 행위 모니터링 |
| 통합             | JSON-RPC, STDIO/SSE(MCP), HTTP/Port           | MCP 기반 연결 |

---

## 🛠 시스템 실행 로드맵

### ✅ 1단계: MCP 서버 통합 및 Agent Host PoC
- Elixir → MCP Client 구현
- MCP 공식 서버와 연결 테스트 (fetch, filesystem 등)

### ✅ 2단계: 차원변환 Agent 구현
- 매뉴얼 임베딩 + DSL 변환
- 사용자 행동 → 절차 매핑 판단 Agent 개발

### ✅ 3단계: 벡터 DB 통합 및 검색 연동
- 메타 기반 검색, 필터링, Context Retrieval 적용

### ✅ 4단계: Agent 통합 및 MCP 기반 Tool 호출
- Reflection/ReAct 패턴 적용, 다중 MCP 서버 호출 구조 구현

### ✅ 5단계: 모니터링 및 최적화
- 처리량, 병목점 분석 → Agent 병렬화, 캐시, 요약 도입

---

## 📈 확장성 포인트

- **처리량 확장**: Elixir/OTP 병렬 구조 + MCP 서버 수평 확장  
- **문제 확장**: Agent 모듈화 → 새로운 절차/도메인 쉽게 추가  
- **Tool 확장**: MCP 표준 기반 → 신규 Tool 서버 손쉽게 추가  
- **LLM 대체**: 외부 API 또는 내부 LLM 교체 용이 (API abstraction)

---

## 📌 참고 오픈소스 / 리소스

- `modelcontextprotocol/servers`: https://github.com/modelcontextprotocol/servers  
- `lastmile-ai/mcp-agent`: https://github.com/lastmile-ai/mcp-agent  
- `LangGraph`: https://docs.langchain.com/langgraph/  
- `CrewAI`: https://github.com/joaomdmoura/crewAI  
- `AutoGen`: https://github.com/microsoft/autogen  
- `Jido (Elixir agents)`: https://github.com/jidobuilder/jido  

---

## 👷 향후 계획

- CLI 기반 테스트 도구 제작  
- 현장 실사용 테스트 → 피드백 반영  
- 엘릭서 기반 Agent 오케스트레이터 오픈소스화 고려  




# High-Performance AI Agent System Design

## Overview

이 프로젝트는 MCP(Model Context Protocol), Agentic AI 시스템, Elixir 기반 분산 아키텍처의 설계와 통합 가능성을 다룬 기술 문서입니다. 각 기술에 대한 심층 분석과 통합 시 고려사항, 아키텍처 설계를 제공합니다.

## 목차

1. [MCP: Model Context Protocol and Open-Source Implementations](1-mcp-overview.md)
   - MCP의 개념 및 구조
   - 참조 서버 구현
   - 주요 MCP 구현체

2. [Agentic AI Frameworks](2-agentic-ai-frameworks.md)
   - LangGraph
   - CrewAI
   - AutoGen
   - 기타 주요 프레임워크

3. [Elixir-Based Distributed Agent Architectures](3-elixir-distributed-architecture.md)
   - Elixir가 AI 에이전트에 적합한 이유
   - Jido 프레임워크
   - Axon(Elixir) 프로젝트
   - 기타 Elixir 기반 접근법

4. [Communication Patterns Between MCP and Agentic AI Systems](4-mcp-agentic-integration.md)
   - JSON-RPC 메시징
   - 도구 검색 메커니즘
   - 도구 호출 프로세스
   - 병렬 및 다단계 상호작용
   - MCP vs 직접 통합의 장단점

5. [MCP Integration in an Elixir Environment](5-mcp-elixir-integration.md)
   - Elixir에서 JSON-RPC 활용
   - Elixir의 MCP 클라이언트 및 서버 구현
   - Elixir 에이전트 프레임워크와의 통합
   - 구현 가능성 및 선행 사례

6. [System Architecture Design and Scalability Analysis](6-system-architecture-scalability.md)
   - 통합 시스템 아키텍처 설계
   - 주요 컴포넌트 및 데이터 흐름
   - 병렬 처리 및 배포 고려사항
   - 확장성 및 병목 지점 분석
   - 잠재적 문제점 및 해결책

## 주요 기술 스택

- **LLM(Large Language Model)**: 에이전트의 핵심 추론 엔진
- **MCP(Model Context Protocol)**: 도구와 데이터 소스 연결을 위한 표준 프로토콜
- **Agentic AI 프레임워크**: 에이전트 오케스트레이션 및 작업 관리
- **Elixir/OTP**: 분산 처리 및 병렬성을 위한 기반 플랫폼
- **Vector Database**: 장기 메모리 및 검색 증강 생성을 위한 임베딩 저장소

## 사용 사례

이 아키텍처는 다음과 같은 사용 사례에 적합합니다:

- 도구를 활용하는 복잡한 AI 비서 시스템
- 다중 에이전트 협업이 필요한 워크플로우
- 대규모 동시 사용자를 처리해야 하는 AI 서비스
- 엔터프라이즈급 확장성과 내결함성이 필요한 AI 애플리케이션
- 보안 및 접근 제어가 중요한 도구 기반 AI 시스템

## 구현 고려사항

이 문서는 개념적 설계와 통합 가능성 분석을 제공합니다. 실제 구현 시 다음을 고려해야 합니다:

1. 적절한 에이전트 프레임워크 선택 (작업 특성에 따라)
2. MCP 서버의 컨테이너화 및 배포 전략
3. Elixir 환경에서의 MCP 클라이언트 구현 방식
4. 확장성을 고려한 LLM API 호출 전략
5. 벡터 데이터베이스 선택 및 임베딩 저장 정책

## 향후 연구 방향

- Elixir용 MCP SDK 개발
- 특정 도메인용 MCP 서버 구현 (예: 특화된 도구)
- 분산 에이전트 간 협업 패턴 최적화
- 실시간 스트리밍 응답을 위한 아키텍처 확장
