def test1():
    try:
        from cassius.cassius import Analysis
    except:
        return False
    return True

def test2():
    try:
        from cassius.cassius import Analysis
        a = Analysis("Hello. My name is Andrew, and I am a big fan of saying no to drugs!")
    except:
        return False
    return True
