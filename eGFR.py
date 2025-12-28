import core

eGFR = None
with open("eGFR.json", "rt") as f:
    eGFR = core.run(f.read())