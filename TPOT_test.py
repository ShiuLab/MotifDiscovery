"""
Testing TPOT [Tree-based Pipeline Optimization Tool] built by Randy Olson 
(http://www.randalolson.com/2015/11/15/introducing-tpot-the-data-science-assistant/)
"""

from tpot import TPOT
import sys
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits  
from sklearn.cross_validation import train_test_split  
  

for i in range (1,len(sys.argv),2):
      if sys.argv[i] == "-df":
        DF = sys.argv[i+1]


df = np.loadtxt(DF, skiprows=1, usecols=range(1,271))

#df = pd.read_csv(DF, sep='\t',header=0, index_col=0)
#print(df.info())
y = df[:,0]
x = df[:,1:]
 
X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.75)  
  
tpot = TPOT(generations=5, verbosity=2)  
tpot.fit(X_train, y_train)  
print(tpot.score(X_train, y_train, X_test, y_test))
tpot.export('tpot_NNU_k3_pro_p05_pipeline.py')

