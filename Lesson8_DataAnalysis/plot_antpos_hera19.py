#! /usr/bin/env python
import aipy as a, numpy as n, pylab as p
import sys, optparse
import IPython

o = optparse.OptionParser()
a.scripting.add_standard_options(o, cal=True)
o.add_option('--aspect_neq', action='store_true', help='Do not force equal aspect in x/y plot.')
o.add_option('--nonumbers', action='store_true', help='Do not plot antenna numbers next to symbols.')
opts, args = o.parse_args(sys.argv[1:])

th = n.arange(0, 2*n.pi, .01)
r = 5.

aa = a.cal.get_aa(opts.cal, .1, .1, 1)
antpos = [aa.get_baseline(0,i,src='z') for i in range(len(aa.ants))]
antpos = n.array(antpos) * a.const.len_ns / 100.
x,y,z = antpos[:,0], antpos[:,1], antpos[:,2]
x -= n.average(x)
y -= n.average(y)

for ant,(xa,ya,za) in enumerate(zip(x,y,z)):
    hx,hy = r*za*n.cos(th)+xa, r*za*n.sin(th)+ya
    if za > 0: fmt = '#eeeeee'
    else: fmt = '#a0a0a0'
    #p.fill(hx,hy, fmt)
    if za != 0:
        p.plot(xa,ya,'k.')
        if not opts.nonumbers: p.text(xa,ya, str(ant))

p.grid()
p.xlabel("East-West Antenna Position (m)")
p.ylabel("North-South Antenna Position (m)")
a = p.gca()
if not opts.aspect_neq: a.set_aspect('equal')
p.savefig('antpos_hera19.png')
