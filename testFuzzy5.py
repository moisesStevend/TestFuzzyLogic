import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

pasos=0.1

#semantica de error de posicion
e=np.arange(-20,20,pasos)#va desde -20 hasta 20, pero de 0.1 en 0.1
#print e.shape[0]
#crearemos los terminos linguisticos
ENG=fuzz.trapmf(e,[-20,-20,-10,-5])
ENP=fuzz.trimf(e,[-10,-5,-0])
EC=fuzz.trimf(e,[-5,0,5])
EPP=fuzz.trimf(e,[0,5,10])
EPG=fuzz.trapmf(e,[5,10,20,20])

plt.figure('Terminos linguisticos para el error') #creamos una figura
plt.plot(e,ENG,linewidth=4, label='ENG')
plt.plot(e,ENP,linewidth=4, label='ENP')
plt.plot(e,EC,linewidth=4, label='EC')
plt.plot(e,EPP,linewidth=4, label='EPP')
plt.plot(e,EPG,linewidth=4, label='EPG')
plt.grid('on')
plt.hold(True)
plt.legend()
#plt.show()

#semantica de accion de control
v=np.arange(-12,12,pasos)
#terminos linguisticos para las variables linguisticas
VNG=fuzz.trapmf(v,[-12,-12,-6,-3])
VNP=fuzz.trimf(v,[-6,-3,0])
VC=fuzz.trimf(v,[-3,0,3])
VPP=fuzz.trimf(v,[0,3,6])
VPG=fuzz.trapmf(v,[3,6,12,12])

plt.figure('Terminos linguisticos para el voltaje') #creamos una figura
plt.plot(v,VNG,linewidth=4, label='VNG')
plt.plot(v,VNP,linewidth=4, label='VNP')
plt.plot(v,VC,linewidth=4, label='VC')
plt.plot(v,VPP,linewidth=4, label='VPP')
plt.plot(v,VPG,linewidth=4, label='VPG')
plt.grid(b=True)
plt.hold(True)
plt.xlim(-12,12)
plt.legend()

plt.show()
#############################################
#error como lista para encontrar su index (posicion en la lista)
#algoritmo de redondeo
tamn=e.shape[0]
ee=e.tolist()
#e=e.tolist() #es opcional

for i in range(tamn):
    ee[i]=round(e[i],6)
    
#print ee #tipo lista
######################################
    #se fuzzificara e inferira
e0=9
n=ee.index(e0)
B1=np.fmin(VNG,ENG[n])
B2=np.fmin(VNP,ENP[n])
B3=np.fmin(VC,EC[n])
B4=np.fmin(VPP,EPP[n])
B5=np.fmin(VPG,EPG[n])

B=np.fmax(B1,(np.fmax(B2,np.fmax(B3,np.fmax(B4,B5))))) #inferencia con el #universo de discurso

#desfuzzificamos
v0=fuzz.defuzz(v,B,'centroid')
print v0



