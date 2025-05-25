from typing import Self

class IntGEZ(int):
    # Tipo dato specializzato intero >= 0
    def __new__(cls, value: float | int | str | bool | Self) -> Self:
        ret: Self = int.__new__(cls, value)
        if ret < 0:
            raise ValueError(f"Il valore {value} deve essere >= 0")
        return ret
    
print(IntGEZ(0))          # 0
print(IntGEZ(42))         # 42
print(IntGEZ("10"))       # 10

print(IntGEZ(-1))         # ValueError
print(IntGEZ("-5"))       # ValueError