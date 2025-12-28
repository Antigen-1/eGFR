import core
import os.path

CysCandScr2eGFR = None
with open(os.path.join(os.path.dirname(__file__), "json", "CysCandScr.json"), "rt") as f:
    CysCandScr2eGFR = core.run(f.read())

Scr2eGFR = None
with open(os.path.join(os.path.dirname(__file__), "json", "Scr.json"), "rt") as f:
    Scr2eGFR = core.run(f.read())
