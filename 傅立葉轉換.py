#fft

import numpy
f=open('input.txt','r')
signal = numpy.array([float(x) for x in f.read().split()], dtype=float)
i=0
for float(x) in signal:
  data=[]
  data.append(float(val))
  i=i+1
  if i==8:	
   xf=numpy.fft.fft(data)

print xf
fftResult = numpy.abs(numpy.fft.fft(data)) ** 2
print fftResult
f.close()
g= open('output.txt', 'w')
i = 0
n = len(data)
freq = numpy.fft.fftfreq(n, d=1)
for val in fftResult:
  a=str(val)+'\n'
  g.write(a)
  i = i + 1
  if i==8:
    break

g.close()
