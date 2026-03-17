import matplotlib.pyplot as plt
import numpy as np
'''
x=[1,2,3,4,5]
y=[60,80,80,90,70]
x=plt.plot(x,y)
plt.title("marks corresonding to no of hours study")
plt.xlabel("no of hours studied")
plt.ylabel("marks obtain")
plt.show()  '''

'''x=[1,2,3,4,5]
dsa_marks=[90,90,80,69,80]
ml_marks=[93,79,59,89,80]

plt.plot(x,dsa_marks,label="dsa marks",color= 'm',linewidth=2,marker='*',linestyle='--',markersize=10)
plt.plot(x,ml_marks,'r*--',label="ml marks ")# by using short hand notation

plt.title("marks corresonding to no of hours study",
        fontdict={'fontname':'comic as same','fontweight':10,'color':'blue'})
plt.xlabel("no of hours studied",fontdict={'fontname':'comic as same','fontweight':10,'fontsize':10,'color':'red'})
plt.ylabel("marks obtain",fontdict={'fontname':'comic as same','fontweight':10,'fontsize':20,'color':'green'})

plt.xticks([1,2,3,4,5])
plt.yticks([10,20,30,40,50])
plt.legend(loc='lower right')
plt.savefig("marks.png",dpi=10)# to save your graph ,figure ets use savefig and mension resolution br dpi
plt.show()  '''

'''t=np.arange(0.,5.,0.2)
print(t)
plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')#(x,y,color,x,y,colour,x,y,color)
plt.show()'''

'''t=np.arange(0.,5.,0.2)
plt.figure()
plt.subplot(1,3,1)
plt.plot(t,t,'r--')
plt.subplot(1,3,2)
plt.plot(t,t**2,'g^')
plt.subplot(1,3,3)
plt.plot(t,t**3,'bs')
plt.show()'''

t=np.arange(0.,5.,0.2)
plt.figure()

plt.subplot(3,1,1)
plt.plot(t,t,'r--')
plt.title('linear')

plt.subplot(3,1,2)
plt.plot(t,t**2,'g^')
plt.title('quadratic')

plt.subplot(3,1,3)
plt.plot(t,t**3,'bs')
plt.title('qubic')

plt.suptitle('different function of t')
plt.tight_layout()# erridicats spacing issues 

plt.show()









