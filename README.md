# SongStats X-Enigma Header Generator

A utility for generating X-Enigma headers required for SongStats frontend API requests. This tool helps developers interact with SongStats' frontend endpoints by providing the necessary authentication headers.

## Overview

This utility provides functionality to generate the X-Enigma header used in SongStats frontend API requests. The X-Enigma header is a security measure implemented by SongStats to validate API requests.

## Features

- Generate X-Enigma headers for SongStats frontend API requests
- Available in TypeScript and Python
- Simple and easy to use
- No external dependencies

## Usage Examples

### TypeScript

```typescript
function generateXEnigma(): string {
  const f = (e: string): number[] => e.split("").map((e) => e.charCodeAt(0));
  const baitString = "<img src='/getbaited.jpg' />";
  const baitBytes = f(baitString);

  let o = {
    W3: (e: string): number[] => e.split("").map((e) => e.charCodeAt(0)),
    n5: (e: number[]): number =>
      baitBytes.reduce((acc: number, curr: number) => acc ^ curr, e[0] || 0),
    _t: (e: number): string => ("0" + Number(e).toString(16)).substr(-2),
  };

  return String(420 * Date.now() + 69)
    .split("")
    .map(o.W3)
    .map(o.n5)
    .map(o._t)
    .join("");
}
```

### Python

```python
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
```

## Examples Directory

The project includes example implementations in the `examples` directory:

- TypeScript examples in `examples/typescript/`
- Python examples in `examples/python/`

## License

This project is free to use for anyone. Feel free to copy and modify the code as needed.
