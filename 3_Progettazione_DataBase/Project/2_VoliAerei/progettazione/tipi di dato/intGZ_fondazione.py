from typing import Self

class IntGT1900(int):
    def __new__(cls, value: float | int | str | bool | Self) -> Self:
        ret = int(value)
        if ret <= 1900:
            raise ValueError(f"Il valore {value} deve essere > 1900")
        return super().__new__(cls, ret)
    
print(IntGT1900(2000))     
print(IntGT1900("2024"))   

print(IntGT1900(1899))    
print(IntGT1900("pippo"))  

