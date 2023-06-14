import numpy.linalg as l
import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt


def laplace(ua,ub,uc,ud,n,m,h,error):
  u = np.array([[ 0 for i in range (n+2)] for j in range (m+2)])
  for i in range(n+2):
    u[i][0]=uc
    u[i][m+1]=ud
  for j in range(m+2):
    u[0][j]=ua
    u[n+1][j]=ub


  p=(ua+ub+uc+ud)/4
  for i in range(1,n+1):
    for j in range(1,m+1):
      u[i][j]=p


  k = 0
  conv = 0


  while k<h and conv==0:
    k=k+1
    t=u.copy()
    for i in range(1,n+1):
      for j in range(1,m+1):
        u[i][j] =0.25*(u[i+1][j]+u[i-1][j]+u[i][j+1]+u[i][j-1])
   
    pp = np.subtract(u, t)
    if (l.norm(pp, np.inf)/l.norm(u,np.inf))<error:
      conv=1
  if conv==1:
    x = np.array([ i+1 for i in range (m+2)])
    y = np.array([ i+1 for i in range (n+2)])
    xx,yy = np.meshgrid(x,y)
    print("u: \n ",u,"\n x: \n ",xx,"\n y: \n ",yy)
   
    fig = plt.figure(figsize =(14, 9))
    ax = plt.axes(projection='3d')
   
    my_cmap = plt.get_cmap('hot')


    hm = ax.plot_surface(xx, yy, u, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    fig.colorbar(hm, ax = ax,
             shrink = 0.5, aspect = 5)
 
    ax.set_title('Ecuación de Laplace')


  else:
    print("no display")
  return
laplace(0,4,0,4,10,10,100,1)
plt.show()
