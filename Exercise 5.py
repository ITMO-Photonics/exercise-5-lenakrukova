
# coding: utf-8

# In[74]:


import numpy as np
# define a custom-build root-finding function (e.g. the one discussed in Lecture 1)
def f(x):
    return (x-3.)*(x*x+1.)
a=0.
b=7.
tolerance=1.e-3

if( f(a)*f(b)>0. ):
    print('Error: f(a) and f(b) should have opposite signs! Stopping.')
else:
    while(0.5*(b-a) > tolerance):
        c = 0.5*(a+b)
        if( f(a)*f(c)<0. ):
            b=c
        else:
            a=c    
    print('result: ',0.5*(b+a))


# In[39]:


x=np.linspace(0.,5.,100)
get_ipython().run_line_magic('timeit', 'f(x) # performance of my function')




# In[61]:


import scipy
from scipy import optimize
scipy.optimize.bisect (f,a,b)








# In[63]:


get_ipython().run_line_magic('timeit', 'scipy.optimize.bisect (f,a,b) # performance of the built-in function "bisect"')


# In[64]:


scipy.optimize.brentq (f,a,b)


# In[65]:


get_ipython().run_line_magic('timeit', 'scipy.optimize.brentq (f,a,b) # performance of the built-in function "brentq"')


# In[67]:


scipy.optimize.newton (f,b)


# In[69]:


get_ipython().run_line_magic('timeit', 'scipy.optimize.newton (f,b) # performance of the built-in function "newton"')

