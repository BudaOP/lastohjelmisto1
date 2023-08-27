# 1. tehtävä
kuhanPituus = float(input('Kirjoita Kuhan pituuden senttimetreinä: '))

if kuhanPituus < 37:
    print('Laske kuha takaisin järveen, sillä alimmasta sallitusta pyyntimitasta puuttuu ', 37 - kuhanPituus, 'cm')
elif kuhanPituus >= 37:
    print('Kuhan pituus on sopiva, ei tarvi olla nälkäinen tänään 😎')