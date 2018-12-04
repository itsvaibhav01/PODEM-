
# coding: utf-8

# In[1]:


# defining all multi-input logic gates 

def And (l):                            # And([1,1,1]) = 1
    if len(l)!=0:
        r=l[0]
    for x in range(1,len(l)):
        r=l[x] and r
    return r
def Or (l):                            # Or([1,0]) = 1
    if len(l) !=0:
        r=l[0]
    for x in range(1,len(l)):
        r=l[x] or r
    return r 
def Not(a):                           # Not(1) = 0
    return int(not a) 
def Nand (l):                         # Nand([1,1,1]) = 0
    return int(not And(l))
def Nor (l):                          # Nor([1,0,0]) = 0
    return int(not Or(l))
def xor (a,b):                        # xor(1,1) = 0, 2-level gate xor with x small
    if a == b :
        return 0
    else :
        return 1 
def Xor (l):                         # Xor ([1,1,1]) = 1 , multi-level gate with capital X in Xor 
    if len(l) != 0:
        r=xor(l[0],l[1])
    for x in range(2,len(l)):
        r=xor(r,l[x])
    return r
def Xnor (l):                       # Xnor([1,1,1]) = 0 
    return int(not Xor(l))
# print(And([1,1,1]),Or ([1,0]),Not(0),Nand([1,0]),Nor([1,0,0]),Xor([1,1,0]),Xnor([1,1,1]))


# In[2]:


# instructions for writing a equation 
# first make a list of all input pins as 
#  input = ["A","B"]
#  similerly the output pin 
#  output = ["O"]
#  then we need to give the circuit diagram and a stuck at fault site by :
#  o =  write the equation in reverse order from output, like for simple and gate 
#  o = And([l[0],l[1]])
#  place the l[i], in place of variable you want to give at that position 
#  similerly give ot = just the same equation with stuck at fault value assigned in place of its output.
#  here are 2 examples given for understanding 


# In[3]:


# circuit 1
inputs = ["A","B","C","D","E"]
output = ["O"]
# --------------------------
l=[]
for x in range(len(inputs)):
    l.append(0)


# In[4]:


# circuit diagram 
# l[0]=>a
# l[1]=>b
# l[2]=>c
# l[3]=>d
def o(l):  
    o =  And([Xor([And([l[0],l[1]]),Or([l[2],l[3]])]),l[4]])
    return o
def ot(l):
    ot =  And([Xor([And([l[0],l[1]]),Or([l[2],l[3]])]),0])
    return ot


# In[5]:


# circuit 2
inputs = ["I0","I1","I3","I4","S0","S1"]
output = ["O"]
# --------------------------
l=[]
for x in range(len(inputs)):
    l.append(0)


# In[6]:


# Mux 4-2-1
# l[0]=>I0
# l[1]=>I1
# l[2]=>I3
# l[3]=>I4
# l[4]=>S0
# l[5]=>S1
def o(l):
    o = Or([And([l[0],Not(l[4]),Not(l[5])]),And([l[1],l[4],Not(l[5])]),And([l[2],Not(l[4]),l[5]]),And([l[3],l[4],l[5]])])
    return o
def ot(l):
    ot = Or([And([l[0],Not(l[4]),1]),And([l[1],l[4],Not(l[5])]),And([l[2],Not(l[4]),l[5]]),And([l[3],l[4],l[5]])])

    return ot


# In[7]:


t=[]
for x in range(2**len(inputs)):
    s=list(bin(x))
    s.pop(0)
    s.pop(0)
    s=list(map(int,s))
    if len (s)<len(l):
        for x in range(len(l)-len(s)):
            s.insert(0,0)
    t.append(s)
    
# print(t)


# In[8]:


s=[]
for x in t:
#     print(o(x),",",ot(x))
    if o(x) != ot(x):
        s.append(x)
print(s)


# In[9]:


f=open("test.txt","w+")
f.write("Following input vectors can be used to detect stuck at fault in circuit. \n")
f.write("\n")
for x in s:
    for y in range(len(x)):
        f.write(str(inputs[y]+": "+str(x[y])+" "))
    f.write("\n")
f.close()


# finally all the test cases will be saved in a text file where the code is saved
