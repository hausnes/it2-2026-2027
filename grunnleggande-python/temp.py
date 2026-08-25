alder: int = "sytten"
print(alder)

def gammelNok(alder: int) -> bool:
    if alder > 18:
        return True
    else:
        return False

gammelNok("sytten")