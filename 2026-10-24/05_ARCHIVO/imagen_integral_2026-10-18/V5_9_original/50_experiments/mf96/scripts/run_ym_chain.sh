#!/bin/sh
S=/home/claude/mf96/scripts/ym_lattice_su2_u1.py
R=/home/claude/mf96/results/ym
python3 -I $S scan $R/ym_scan.json > $R/run_scan.log 2>&1
python3 -I $S wilson $R/ym_wilson_L10.json 10 > $R/run_wilson.log 2>&1
