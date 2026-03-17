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
