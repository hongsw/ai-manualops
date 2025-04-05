from typing import Any, Dict, List

def echo_handler(message: str) -> str:
    """에코 핸들러 - 받은 메시지를 그대로 반환"""
    return message

def sum_handler(*numbers: float) -> float:
    """숫자들의 합을 계산"""
    return sum(numbers)

def process_data_handler(data: Dict[str, Any]) -> Dict[str, Any]:
    """데이터 처리 핸들러 - 딕셔너리 데이터를 처리"""
    processed = {
        "received": data,
        "length": len(data),
        "keys": list(data.keys())
    }
    return processed

def list_manipulation_handler(items: List[Any], operation: str) -> List[Any]:
    """리스트 조작 핸들러"""
    if operation == "reverse":
        return list(reversed(items))
    elif operation == "sort":
        return sorted(items)
    elif operation == "unique":
        return list(set(items))
    else:
        raise ValueError(f"Unknown operation: {operation}") 