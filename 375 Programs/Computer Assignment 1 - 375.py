import TestFcns as tf
import Methods as af
import pandas as pd

pd.set_option('display.precision', 10)

#roots, number of iterations
#ftable1 = af.bisec(1.75, 2.5, 1e-8, tf.F, 9.95)
#ftable1.to_csv('Bisection_F.csv', index = False)
#ftable2 = af.false(1.75, 2.5, 1e-8, tf.F, 9.95)
#ftable2.to_csv('MoFP_F.csv', index = False)
#print(ftable2)

#gtable1 = af.bisec(-1, -.125, 1e-6, tf.G, .4)
#gtable1.to_csv('Bisection_G.csv', index = False)
#gtable2 = af.false(-1, -.125, 1e-6, tf.G, .4)
#gtable2.to_csv('MoFP_G.csv', index = False)
#print(gtable2)

#htable1 = af.bisec(.4, 1, 1e-6, tf.H, 4.8)
#htable1.to_csv('Bisection_H.csv', index = False)
#htable2 = af.false(.4, 1, 1e-6, tf.H, 4.8)
#htable2.to_csv('MoFP_H.csv', index = False)
#print(htable2)
htable3 = af.newt_fpi(.4, 1e-6, tf.H, tf.dH, 4.8)
#htable3.to_csv('Newtons_H.csv', index = False)
print(htable3)
#htable4 = af.base_fpi(.4, 1e-6, tf.C)
#htable4.to_csv('FPI_H.csv', index = False)