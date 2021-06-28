import gpytorch

def gpytorch_kernel_Matern(var, ls, nu = 2.5):
    """
    Return a Matern kernel with specified kernel variance (var) and lengthscales (ls)
    """
    ker_mat = gpytorch.kernels.MaternKernel(nu=nu, ard_num_dims=len(ls))
    ker_mat.lengthscale = ls
    ker = gpytorch.kernels.ScaleKernel(ker_mat)
    ker.outputscale = var
    
    return ker

def gpytorch_mean_constant(val, fixed = True):
    """
    Return a constant mean function
    
    fixed = True -> Do not update mean function during training
    """
    mean = gpytorch.means.ConstantMean()
    mean.initialize(constant=val)
    mean.constant.requires_grad = not fixed
    
    return mean

def gpytorch_likelihood_gaussian(variance, variance_lb = 1e-6, fixed = True):
    """
    Return a Gaussian likelihood
    
    fixed = True -> Do not update during training
    variance_lb = lower bound
    """
    likelihood = gpytorch.likelihoods.GaussianLikelihood(noise_constraint=gpytorch.constraints.GreaterThan(variance_lb))
    likelihood.initialize(noise=variance)
    likelihood.requires_grad = not fixed
    
    return likelihood