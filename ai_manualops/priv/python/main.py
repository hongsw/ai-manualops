from bridge import Bridge
from example_handlers import (
    echo_handler,
    sum_handler,
    process_data_handler,
    list_manipulation_handler
)

def main():
    # 브릿지 인스턴스 생성
    bridge = Bridge()
    
    # 핸들러 등록
    bridge.register_handler("echo", echo_handler)
    bridge.register_handler("sum", sum_handler)
    bridge.register_handler("process_data", process_data_handler)
    bridge.register_handler("list_manipulation", list_manipulation_handler)
    
    # 브릿지 시작
    print("Starting Python-Elixir bridge...", flush=True)
    bridge.start()

if __name__ == "__main__":
    main() 