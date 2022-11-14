import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import more_itertools as mit

#text_file = open('seqSC2.txt','r')
#data = text_file.read()
#text_file.close()

def codonHistogram(data):
    l = ["".join(w) for w in mit.windowed(data,3)]
    codonDict = {x:l.count(x) for x in l}
    nCodons = len(l)-3
    normCodons = {key:value/nCodons for key, value in codonDict.items()}
    return (normCodons)

#codonDicts = codonHistogram(data)
#print(codonDicts)

def plot_wrapper(codonD,fileStr, title):
  plt.bar(range(len(codonD)), codonD.values())
  plt.xlabel('Codon')
  plt.ylabel('Frequency')
  xlabels = list(codonD.keys())#gets keys as labels
  #np.arrange(len(codonD))
  plt.xticks(np.arange(len(codonD)),xlabels, rotation=90)
  plt.tick_params(labelsize=5)
  plt.title(title)
  plt.savefig(fileStr)
  plt.show()

def baseDensity(geneStr, nWind=200):
  a = np.zeros(len(geneStr)-nWind)
  g = np.zeros(len(geneStr)-nWind)
  c = np.zeros(len(geneStr)-nWind)
  t = np.zeros(len(geneStr)-nWind)
  for n in range(0, len(geneStr)-nWind):
    t[n] = (geneStr[n:n+nWind].count('T'))/nWind
    a[n] = (geneStr[n:n+nWind].count('A'))/nWind
    c[n] = (geneStr[n:n+nWind].count('C'))/nWind
    g[n] = (geneStr[n:n+nWind].count('G'))/nWind
  dingle = (t,a,c,g)
  return dingle

def plot_density(t,a,c,g, geneStr, title):
  fig,ax = plt.subplots()
  ax.plot(t, color = 'b', label='T')
  ax.plot(a, color = 'c', label='A')
  ax.plot(c, color = 'r', label='C')
  ax.plot(g, color = 'g', label='G')
  plt.title(title)
  plt.xlabel('Sequence Position')
  plt.ylabel('Fraction per Window')
  plt.grid()
  plt.legend(loc="upper right")
  plt.show()

def klDivergence(histOne,histTwo):
  for n in range(0,64):
    histOne
    





if __name__=="__main__":
    # Open genome
    with open('seqSC2.txt','r') as geneFile:
        scov2 = geneFile.readline()

    # Generate histogram for SARS-Cov-2
    histSC2 = codonHistogram(scov2)
    
    #xlabels = list(normCodons.keys())
    #print(xlabels)
    #stuff = np.arange(len(normCodons))
    #print(stuff)
    
    plot_wrapper(histSC2, 'histSC2.png','Codon frequency in SARS-CoV-2')
    dA,dT,dC,dG = baseDensity(scov2)
    #print(dA,dC,dG,dT)
    plot_density(dT,dA,dC,dG,scov2,'Density of base pairs through gene sequence')

    with open('seqA.txt','r') as geneFile:
      scA = geneFile.readline()

    histscA = codonHistogram(scA)
    plot_wrapper(histscA, 'histA.png','seqA')

    with open('seqB.txt','r') as geneFile:
      scB = geneFile.readline()

    histscB = codonHistogram(scB)
    plot_wrapper(histscB, 'histB.png','seqB')
