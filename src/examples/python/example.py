import time
from functools import reduce

def generate_x_enigma():
    def f(e: str) -> list[int]:
        return [ord(char) for char in e]
    
    bait_string = "<img src='/getbaited.jpg' />"
    bait_bytes = f(bait_string)
    
    def w3(e: str) -> list[int]:
        return [ord(char) for char in e]
    
    def n5(e: list[int]) -> int:
        return bait_bytes[0] if not e else reduce(lambda acc, curr: acc ^ curr, bait_bytes, e[0])
    
    def _t(e: int) -> str:
        return ('0' + hex(e)[2:])[-2:]
    
    timestamp = str(420 * int(time.time() * 1000) + 69)
    return ''.join(_t(n5(w3(char))) for char in timestamp)

if __name__ == "__main__":
    x_enigma = generate_x_enigma()
    print(x_enigma)
