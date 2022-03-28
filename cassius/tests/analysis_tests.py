def test1():
    try:
        from cassius.analysis import Analysis
    except:
        return False
    return True

def test2():
    try:
        from cassius.analysis import Analysis
        a = Analysis("Hello. My name is Andrew, and I am a big fan of saying no to drugs!")
    except:
        return False
    return True

def test3():
    try:
        from cassius.analysis import Analysis
        pass
    except:
        return False
    return True
