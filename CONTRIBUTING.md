# 기여 가이드라인

AI-ManualOps 프로젝트에 기여하고 싶으시다면 다음 가이드라인을 따라주세요.

## 개발 환경 설정

### 요구사항

- Elixir 1.14 이상
- Python 3.9 이상
- Qdrant 1.1 이상
- Docker (선택 사항)

### 설치

```bash
# 저장소 클론
git clone https://github.com/yourusername/ai-manualops.git
cd ai-manualops

# 의존성 설치
mix deps.get
pip install -r requirements.txt

# 환경 변수 설정
cp .env.example .env
# .env 파일을 편집하여 필요한 설정 추가
```

## 개발 워크플로우

1. **이슈 생성**: 작업을 시작하기 전에 관련 이슈를 생성하세요.
2. **브랜치 생성**: 이슈 번호를 포함한 기능 브랜치를 생성하세요.
   ```bash
   git checkout -b feature/123-feature-name
   ```
3. **개발**: 코드를 작성하고 테스트하세요.
4. **커밋**: 커밋 메시지 규칙을 따라 커밋하세요.
5. **푸시**: 변경사항을 원격 저장소에 푸시하세요.
   ```bash
   git push origin feature/123-feature-name
   ```
6. **PR 생성**: Pull Request를 생성하고 리뷰어를 지정하세요.

## 코드 스타일

### Elixir

- [Credo](https://github.com/rrrene/credo)를 사용하여 코드 스타일을 검사합니다.
- [Dialyxir](https://github.com/jeremyjh/dialyxir)를 사용하여 타입 검사를 수행합니다.

```bash
# 코드 스타일 검사
mix credo

# 타입 검사
mix dialyzer
```

### Python

- [Black](https://github.com/psf/black)을 사용하여 코드 포맷팅을 수행합니다.
- [Flake8](https://flake8.pycqa.org/)을 사용하여 린팅을 수행합니다.
- [MyPy](https://mypy.readthedocs.io/)를 사용하여 타입 검사를 수행합니다.

```bash
# 코드 포맷팅
black .

# 린팅
flake8

# 타입 검사
mypy .
```

## 테스트

### Elixir

```bash
# 단위 테스트 실행
mix test

# 특정 테스트 파일 실행
mix test test/ai_manualops/dimension_engine_test.exs
```

### Python

```bash
# 단위 테스트 실행
pytest

# 특정 테스트 파일 실행
pytest tests/test_dimension_engine.py
```

## 문서화

- 모든 공개 함수와 모듈에 문서화 주석을 추가하세요.
- 복잡한 알고리즘에는 설명 주석을 추가하세요.
- README.md 및 기타 문서를 필요에 따라 업데이트하세요.

### Elixir

```elixir
@moduledoc """
모듈에 대한 설명
"""

@doc """
함수에 대한 설명

## 예시

    iex> AI.ManualOps.DimensionEngine.convert("path/to/manual.pdf")
    {:ok, %DSL{}}

"""
def convert(path) do
  # 구현
end
```

### Python

```python
def convert(path: str) -> Dict[str, Any]:
    """
    매뉴얼 파일을 DSL로 변환합니다.

    Args:
        path (str): 매뉴얼 파일 경로

    Returns:
        Dict[str, Any]: 변환된 DSL

    Example:
        >>> convert("path/to/manual.pdf")
        {"type": "manual", "content": {...}}
    """
    # 구현
```

## 커밋 메시지 규칙

커밋 메시지는 다음 형식을 따릅니다:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 타입

- **feat**: 새로운 기능
- **fix**: 버그 수정
- **docs**: 문서 변경
- **style**: 코드 포맷팅
- **refactor**: 코드 리팩토링
- **test**: 테스트 코드
- **chore**: 빌드 프로세스 또는 보조 도구 변경

### 예시

```
feat(dimension-engine): 매뉴얼 변환 기능 추가

- PDF 파일 파싱 기능 구현
- 텍스트 추출 및 구조화 로직 추가
- DSL 생성 기능 구현

Closes #123
```

## Pull Request 프로세스

1. PR 설명에 관련 이슈 번호를 포함하세요.
2. PR 설명에 변경 내용에 대한 자세한 설명을 추가하세요.
3. 모든 테스트가 통과했는지 확인하세요.
4. 코드 리뷰어의 피드백을 반영하세요.
5. 충돌이 있는 경우 해결하세요.

## 이슈 보고

버그를 발견하거나 기능 요청을 하려면 다음 정보를 포함하여 이슈를 생성하세요:

- 문제 또는 요청에 대한 자세한 설명
- 재현 단계 (버그인 경우)
- 예상 결과와 실제 결과 (버그인 경우)
- 환경 정보 (OS, Elixir 버전, Python 버전 등)
- 스크린샷 또는 로그 (가능한 경우)

## 라이선스

기여하는 모든 코드는 MIT 라이선스 하에 배포됩니다. 기여함으로써 귀하는 귀하의 기여가 MIT 라이선스 하에 배포될 수 있음에 동의합니다. 