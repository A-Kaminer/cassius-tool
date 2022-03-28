def test1():
    try:
        from cassius.analysis import Analysis
        from cassius.rot import RotCiphers

        a = Analysis("This is supposed to test everything. I want to make sure there are no oopsies. It's gonna be unfortunate if there's an oopsie.")

        assert RotCiphers.rot13(a, True) == "Guvf vf fhccbfrq gb grfg rirelguvat. V jnag gb znxr fher gurer ner ab bbcfvrf. Vg'f tbaan or hasbeghangr vs gurer'f na bbcfvr."
    except:
        return False
    return True

def test2():
    try:
        from cassius.analysis import Analysis
        from cassius.rot import RotCiphers

        a = Analysis("This is supposed to test everything. I want to make sure there are no oopsies. It's gonna be unfortunate if there's an oopsie.")
        assert RotCiphers.rot13(a, False) == "GUVF VF FHCCBFRQ GB GRFG RIRELGUVAT. V JNAG GB ZNXR FHER GURER NER AB BBCFVRF. VG'F TBAAN OR HASBEGHANGR VS GURER'F NA BBCFVR."
    except:
        return False
    return True
