#!/usr/bin/env python
from pathlib import Path
from pandas import read_excel
from matplotlib.pyplot import show,boxplot

def dostats(fn):
    fn = Path(fn).expanduser()
    dat = read_excel(fn)

    return dat

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='ride cost statistics')
    p.add_argument('fn',help='XLS to analyze')
    p.add_argument('-d','--dist',help='select by distance',type=float)
    p = p.parse_args()

    base = 2. + 1.15   # dollars

    dat = dostats(p.fn)
    filt = dat.copy()

    if p.dist is not None:
        filt = dat.loc[dat['approx miles']==p.dist,:]

    costpermile = (filt['cost'] - base) / filt['approx miles']
    boxplot(costpermile,showfliers=True)
    #ax = costpermile.plot.box(grid=True,showfliers=True)
    show()