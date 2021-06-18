#!/bin/bash

osmo-nitb -c ./openbsc.cfg -l ./hlr.sqlite3 -P -C --debug=DRLL:DCC:DMM:DRR:DRSL:DNM -M /tmp/bsc_mncc
