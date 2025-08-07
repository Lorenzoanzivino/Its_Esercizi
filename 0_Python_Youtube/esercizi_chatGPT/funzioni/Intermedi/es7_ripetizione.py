

def repeat_str(repeat, string) -> str:
    if repeat <= 0:
        repeat = abs(repeat)
    
    return string * repeat
    

print(repeat_str(-3, "ciao"))