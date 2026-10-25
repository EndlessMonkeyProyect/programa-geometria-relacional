#!/bin/sh
S=/home/claude/mf96/scripts/pnp_two_languages.py
R=/home/claude/mf96/results/pnp
python3 -I $S sat2 $R/pnp_sat2.json > $R/run_sat2.log 2>&1
python3 -I $S sat3 $R/pnp_sat3.json > $R/run_sat3.log 2>&1
python3 -I $S tseitin $R/pnp_tseitin.json > $R/run_tseitin.log 2>&1
