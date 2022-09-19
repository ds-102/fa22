import pymc3 as pm


alphas = ...
betas = ...
pi = ...

with pm.Model() as model:
    z = pm.Bernoulli(
        # Define the Bernoulli Model Here
    )
    
    # Hint: you should use the shape= parameter here so that
    # q is a PyMC3 array with both q0 and q1.
    q = ...
    
    # Hint: it may be useful to use "fancy indexing" like we did in class. 
    # See below for an example
    X = pm.Geometric(
        # DEFINE THE GEOMETRIC MODEL HERE
    )
    
    trace = ....
    
# FANCY INDEXING

my_binary_array = np.array([0, 0, 1, 1, 0, 1])
my_real_array = np.array([0.27, 0.34])
print(my_real_array[my_binary_array])