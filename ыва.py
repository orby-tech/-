import numpy as np
def sigmoid(x):
    return 1/(1+np.exp(-x))

training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs =np.array([[0,1,1,0]]).T

np.random.seed()

synaptic_weights1 =2* np.random. random((4,3))-1
synaptic_weights2 =2* np.random. random((3,1))-1


for i in range(20000):
    input_layer =training_inputs
    outputs1 = sigmoid( input_layer* synaptic_weights1)
    layer1=outputs1
    
    outputs2 = sigmoid( np.dot(layer1, synaptic_weights2))
    err2=training_outputs - outputs2
    adjustments2= np.dot( layer1.T, err2*(outputs2*(1-outputs2)))

    
    err1=outputs2*err2
    adjustments1=err1*outputs1*(1-outputs1)
    synaptic_weights1+= adjustments1
    
    synaptic_weights2+= adjustments2

   
print(outputs2)
new_inputs = np.array([1,1,0])
outputs1 = sigmoid( new_inputs* synaptic_weights1)
layer1=outputs1
out = sigmoid( np.dot(layer1, synaptic_weights2))

print("NEW SIT:")
print(out)
input()
