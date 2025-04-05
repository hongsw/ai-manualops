from bridge import Bridge
from example_handlers import (
    echo_handler,
    sum_handler,
    process_data_handler,
    list_manipulation_handler
)
import sys

def test_bridge():
    # 브릿지 인스턴스 생성
    bridge = Bridge()
    
    # 핸들러 등록
    bridge.register_handler("echo", echo_handler)
    bridge.register_handler("sum", sum_handler)
    bridge.register_handler("process_data", process_data_handler)
    bridge.register_handler("list_manipulation", list_manipulation_handler)
    
    # 간단한 테스트 데이터
    test_cases = [
        # 에코 테스트
        {
            "action": "echo", 
            "args": ["안녕하세요!"], 
            "expected": "안녕하세요!"
        },
        
        # 합계 테스트
        {
            "action": "sum", 
            "args": [1, 2, 3, 4, 5], 
            "expected": 15
        },
        
        # 데이터 처리 테스트
        {
            "action": "process_data", 
            "args": [{"name": "test", "value": 42}], 
            "expected_keys": ["received", "length", "keys"]
        },
        
        # 리스트 정렬 테스트
        {
            "action": "list_manipulation", 
            "args": [[3, 1, 4, 1, 5, 9, 2, 6], "sort"], 
            "expected": [1, 1, 2, 3, 4, 5, 6, 9]
        }
    ]
    
    print("브릿지 직접 테스트 시작...", flush=True)
    
    for i, case in enumerate(test_cases):
        action = case["action"]
        args = case["args"]
        
        try:
            handler = bridge.handlers.get(action)
            if not handler:
                print(f"테스트 {i+1} 실패: 핸들러를 찾을 수 없음 - {action}", flush=True)
                continue
                
            result = handler(*args)
            
            # 결과 검증
            if "expected" in case:
                if result == case["expected"]:
                    print(f"테스트 {i+1} 성공: {action} - 예상 결과와 일치", flush=True)
                else:
                    print(f"테스트 {i+1} 실패: {action} - 예상: {case['expected']}, 실제: {result}", flush=True)
            elif "expected_keys" in case:
                if all(key in result for key in case["expected_keys"]):
                    print(f"테스트 {i+1} 성공: {action} - 모든 예상 키가 존재", flush=True)
                else:
                    print(f"테스트 {i+1} 실패: {action} - 일부 키가 없음. 결과: {result}", flush=True)
            else:
                print(f"테스트 {i+1} 결과: {action} - {result}", flush=True)
                
        except Exception as e:
            print(f"테스트 {i+1} 에러: {action} - {str(e)}", flush=True)
    
    print("\n모든 테스트 완료!", flush=True)

if __name__ == "__main__":
    test_bridge() 