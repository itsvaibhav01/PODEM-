# PODEM-py 
PODEM - Path Oriented DEcision Making 
here we have a python code to detect the stuck at faults in the ciruit, read the code its self-explainatory 


### instructions for writing a equation 
### first make a list of all input pins as 
###  input = ["A","B"]
###  similerly the output pin 
###  output = ["O"]
###  then we need to give the circuit diagram and a stuck at fault site by :
###  o =  write the equation in reverse order from output, like for simple and gate 
###  o = And([l[0],l[1]])
###  place the l[i], in place of variable you want to give at that position 
###  similerly give ot = just the same equation with stuck at fault value assigned in place of its output.
###  here are 2 examples given for understanding 


# circuit 1

inputs = ["A","B","C","D","E"]
output = ["O"]

# --------------------------
l=[]
for x in range(len(inputs)):
    l.append(0)

### circuit diagram 
### l[0]=>a
### l[1]=>b
### l[2]=>c
### l[3]=>d

def o(l):  
    o =  And([Xor([And([l[0],l[1]]),Or([l[2],l[3]])]),l[4]])
    return o
def ot(l):
    ot =  And([Xor([And([l[0],l[1]]),Or([l[2],l[3]])]),0])
    return ot



# circuit 2

inputs = ["I0","I1","I3","I4","S0","S1"]
output = ["O"]

# --------------------------
l=[]
for x in range(len(inputs)):
    l.append(0)


### Mux 4-2-1
### l[0]=>I0
### l[1]=>I1
### l[2]=>I3
### l[3]=>I4
### l[4]=>S0
### l[5]=>S1

def o(l):
    o = Or([And([l[0],Not(l[4]),Not(l[5])]),And([l[1],l[4],Not(l[5])]),And([l[2],Not(l[4]),l[5]]),And([l[3],l[4],l[5]])])
    return o
def ot(l):
    ot = Or([And([l[0],Not(l[4]),1]),And([l[1],l[4],Not(l[5])]),And([l[2],Not(l[4]),l[5]]),And([l[3],l[4],l[5]])])

    return ot


### finally all the test cases will be saved in a text file where the code is saved
