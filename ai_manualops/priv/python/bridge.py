from typing import Any, Dict, List, Optional, Union
from erlastic import Atom, decode, encode

class Bridge:
    """Elixir-Python 통신을 위한 브릿지 클래스"""
    
    def __init__(self):
        self.handlers = {}
        
    def register_handler(self, name: str, handler_func: callable):
        """메시지 핸들러 등록"""
        self.handlers[name] = handler_func
        
    def handle_message(self, message: bytes) -> bytes:
        """Elixir로부터 받은 메시지 처리"""
        try:
            decoded = decode(message)
            if not isinstance(decoded, tuple) or len(decoded) < 2:
                return encode((Atom(b"error"), "Invalid message format"))
                
            action = decoded[0]
            if not isinstance(action, Atom):
                return encode((Atom(b"error"), "Invalid action type"))
                
            handler = self.handlers.get(action.text.decode())
            if not handler:
                return encode((Atom(b"error"), f"No handler for action: {action.text.decode()}"))
                
            result = handler(*decoded[1:])
            return encode((Atom(b"ok"), result))
            
        except Exception as e:
            return encode((Atom(b"error"), str(e)))
            
    def start(self):
        """브릿지 시작"""
        while True:
            try:
                # 4바이트 길이 헤더 읽기
                length_bytes = self._read_exact(4)
                if not length_bytes:
                    break
                    
                message_length = int.from_bytes(length_bytes, byteorder='big')
                
                # 메시지 본문 읽기
                message = self._read_exact(message_length)
                if not message:
                    break
                    
                # 메시지 처리 및 응답
                response = self.handle_message(message)
                
                # 응답 전송
                response_length = len(response)
                self._write_exact(response_length.to_bytes(4, byteorder='big'))
                self._write_exact(response)
                
            except Exception as e:
                print(f"Error in bridge: {e}", flush=True)
                break
                
    def _read_exact(self, length: int) -> Optional[bytes]:
        """정확한 길이만큼 데이터 읽기"""
        buffer = bytearray()
        while len(buffer) < length:
            chunk = self._read(length - len(buffer))
            if not chunk:
                return None
            buffer.extend(chunk)
        return bytes(buffer)
        
    def _write_exact(self, data: bytes):
        """데이터 전체 쓰기"""
        self._write(data)
        
    def _read(self, length: int) -> bytes:
        """표준 입력에서 데이터 읽기"""
        import sys
        return sys.stdin.buffer.read(length)
        
    def _write(self, data: bytes):
        """표준 출력으로 데이터 쓰기"""
        import sys
        sys.stdout.buffer.write(data)
        sys.stdout.buffer.flush() 