###
# Python wrapper for Pyfmtools. Simplifies the usage of Pyfmtools by handling all Numpy and CFFI calls
###
import numpy as np
import types
import math
import re
from  _pyfmtools import ffi, lib as fm

###
# Helper functions
###

# global variable to support trace-info while testing
isTest = False

# Trace function
def trace( str):
    if isTest == True: print( "-- ", str, " --")


# convert Python float to CFFI double * 
def convert_float_to_CFFI_double( x):
    if x.dtype != "float64": x = x.astype(float)
    px = ffi.cast( "double *", x.ctypes.data)
    return px

# use numpy to create an intc array with n zeros and cast to CFFI 
def create_intc_zeros_as_CFFI_int( n):
    x = np.zeros( n, np.intc)
    px = ffi.cast( "int *", x.ctypes.data)
    return x, px

# use numpy to create an intc array with n zeros and cast to CFFI 
def create_float_zeros_as_CFFI_double( n):
    x = np.zeros( n, float)
    px = ffi.cast( "double *", x.ctypes.data)
    return x, px

def convert_py_float_to_cffi( x):
    px = np.array( x)
    if px.dtype != "float64": px = px.astype( float)
    pxcffi = ffi.cast( "double *", px.ctypes.data)
    return px, pxcffi


def convert_py_int_to_cffi( x):
    x = x.astype( np.intc)
    px = np.array( x)
    pxcffi = ffi.cast( "int *", px.ctypes.data)
    return px, pxcffi


###
# The python minimum wrapper for py_ functions from wrapper.cpp
###

# void py_fm_init(int n, struct fm_env* env)
def fm_init( n):
    try:
        trace( "py_fm_init")
        env = ffi.new( "struct fm_env *")
        fm.py_fm_init( n, env)
        return env
    except ValueError:
        raise

# void py_fm_free( struct fm_env* env)
def fm_free( env):
    try:
        trace( "py_fm_free")
        if( env == None): raise ValueError( "Env not initialised") 
        fm.py_fm_free( env)
    except ValueError:
        raise

# void py_ShowCoalitions(int* coalition, struct fm_env* env)
def ShowCoalitions( env):
    trace( "py_ShowCoalitions")
    A, pA = create_intc_zeros_as_CFFI_int( env.m) 
    fm.py_ShowCoalitions( pA, env)
    return A

# int py_generate_fm_2additive_concave(int num, int n, double * vv)
def generate_fm_2additive_concave( ti, n, env):
    trace( "py_generate_fm_2additive_concave")
    v, pv = create_float_zeros_as_CFFI_double( env.m)
    size = fm.py_generate_fm_2additive_concave( ti, n, pv)
    return size, v

# void py_ShowCoalitionsCard(int* coalition, struct fm_env* env)
def ShowCoalitionsCard( env):
    trace( "py_ShowCoalitionsCard")
    A, pA = create_intc_zeros_as_CFFI_int( env.m) 
    A = fm.py_ShowCoalitionsCard( pA, env)
    return A

# py_generate_fmconvex_tsort(ti,n, n-1 , 1000, 8, 1, pv,env)
def generate_fmconvex_tsort( num, n, kint, markov, option, K, env):
    trace( "py_generate_fmconvex_tsort")
    v, pv = create_float_zeros_as_CFFI_double( env.m)
    size = fm.py_generate_fmconvex_tsort( num ,n, kint, markov, option, K, pv, env)
    return size, v

# py_generate_fm_tsort(ti,n, 2 , 10, 0, 0.1, pv,env)
def generate_fm_tsort( num, n, kint, markov, option, K, env):
    trace( "py_generate_fm_tsort")
    v, pv = create_float_zeros_as_CFFI_double( env.m)
    size = fm.py_generate_fm_tsort( num ,n, kint, markov, option, K, env)
    return size, v

# py_ConvertCard2Bit(pvb,pv,env)
def ConvertCard2Bit( v, env):
    trace( "py_ConvertCard2Bit")
    
    pv = convert_float_to_CFFI_double( v)
    vb, pvb = create_float_zeros_as_CFFI_double( env.m)
    fm.py_ConvertCard2Bit( pvb, pv, env)
    return vb 

# py_IsMeasureSupermodular(pvb,env)
def IsMeasureSupermodular( vb, env):
    trace( "py_IsMeasureSupermodular")
    pvb = convert_float_to_CFFI_double( vb)
    return fm.py_IsMeasureSupermodular( pvb, env)

# py_IsMeasureAdditive(pvb,env)
def IsMeasureAdditive( vb, env):
    trace( "y_IsMeasureAdditive")
    pvb = convert_float_to_CFFI_double( vb)
    return fm.py_IsMeasureAdditive( pvb, env)

# py_export_maximal_chains(n,pvb,pmc,env)
def export_maximal_chains( n, vb, env):
    trace( "py_export_maximal_chains")
    pvb = convert_float_to_CFFI_double( vb)
    mc, pmc = create_float_zeros_as_CFFI_double( math.factorial(n) * n)
    fm.py_export_maximal_chains( n, pvb, pmc, env)
    return mc

# py_Choquet(px,pvb,env)
def Choquet( x, vb, env):
    trace( "y_Choquet")
    npx = np.array( x)
    pnpx = ffi.cast( "double *", npx.ctypes.data)
    pvb = convert_float_to_CFFI_double( vb)
    return fm.py_Choquet( pnpx, pvb, env)

# double py_Sugeno(double* x, double* v, struct fm_env* env)
def Sugeno( x, vb, env):
    trace( "py_Sugeno")
    npx = np.array( x)
    pnpx = ffi.cast( "double *", npx.ctypes.data)
    pvb = convert_float_to_CFFI_double( vb)
    return fm.py_Sugeno( pnpx, pvb, env)



###
# The python wrapper for all other py_ functions from wrapper.cpp
###

# Generated python wrapper for:
#    double py_min_subset(double* x, int n, int_64 S)
def min_subset(x, n, S):
    trace( "double py_min_subset(double* x, int n, int_64 S)")
    pxnp, px = convert_py_float_to_cffi( x)
    yy = fm.py_min_subset( px, n, S)
    return yy


# Generated python wrapper for:
#    double py_max_subset(double* x, int n, int_64 S)
def max_subset(x, n, S):
    trace( "double py_max_subset(double* x, int n, int_64 S)")
    pxnp, px = convert_py_float_to_cffi( x)
    yy = fm.py_max_subset( px, n, S)
    return yy


# Generated python wrapper for:
#    double py_min_subsetC(double* x, int n, int_64 S, struct fm_env* env)
def min_subsetC(x, n, S, env):
    trace( "double py_min_subsetC(double* x, int n, int_64 S, struct fm_env* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    yy = fm.py_min_subsetC( px, n, S, env)
    return yy


# Generated python wrapper for:
#    double py_max_subsetNegC(double* x, int n, int_64 S, struct fm_env* env)
def max_subsetNegC(x, n, S, env):
    trace( "double py_max_subsetNegC(double* x, int n, int_64 S, struct fm_env* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    yy = fm.py_max_subsetNegC( px, n, S, env)
    return yy


# Generated python wrapper for:
#    int py_SizeArraykinteractive(int n, int k, struct fm_env* env)
def SizeArraykinteractive(n, k, env):
    trace( "int py_SizeArraykinteractive(int n, int k, struct fm_env* env)")
    yy = fm.py_SizeArraykinteractive( n, k, env)
    return yy


# Generated python wrapper for:
#    int py_IsSubsetC(int i, int j, struct fm_env* env)
def IsSubsetC(i, j, env):
    trace( "int py_IsSubsetC(int i, int j, struct fm_env* env)")
    yy = fm.py_IsSubsetC( i, j, env)
    return yy


# Generated python wrapper for:
#    int py_IsElementC(int i, int j, struct fm_env* env)
def IsElementC(i, j, env):
    trace( "int py_IsElementC(int i, int j, struct fm_env* env)")
    yy = fm.py_IsElementC( i, j, env)
    return yy


# Generated python wrapper for:
#    void py_ExpandKinteractive2Bit(double* out_dest, double* src, struct fm_env* env, int kint, int arraysize)
def ExpandKinteractive2Bit(src, env, kint, arraysize):
    trace( "void py_ExpandKinteractive2Bit(double* out_dest, double* src, struct fm_env* env, int kint, int arraysize)")
    pout_destnp, pout_dest = create_float_zeros_as_CFFI_double( env.m)
    psrcnp, psrc = convert_py_float_to_cffi( src)
    fm.py_ExpandKinteractive2Bit( pout_destpsrc, env, kint, arraysize)
    return pout_destnp


# Generated python wrapper for:
#    void py_ExpandKinteractive2Bit_m(double* out_dest, double* src, struct fm_env* env, int kint, int arraysize, double* VVC)
def ExpandKinteractive2Bit_m(src, env, kint, arraysize, VVC):
    trace( "void py_ExpandKinteractive2Bit_m(double* out_dest, double* src, struct fm_env* env, int kint, int arraysize, double* VVC)")
    pout_destnp, pout_dest = create_float_zeros_as_CFFI_double( env.m)
    psrcnp, psrc = convert_py_float_to_cffi( src)
    pVVCnp, pVVC = convert_py_float_to_cffi( VVC)
    fm.py_ExpandKinteractive2Bit_m( pout_destpsrc, env, kint, arraysize, pVVC)
    return pout_destnp


# Generated python wrapper for:
#    void py_Shapley(double* v, double* out_x, struct fm_env* env)
def Shapley(v, env):
    trace( "void py_Shapley(double* v, double* out_x, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_xnp, pout_x = create_float_zeros_as_CFFI_double( env.n)
    fm.py_Shapley( pv, pout_x, env)
    return pout_xnp


# Generated python wrapper for:
#    void py_Banzhaf(double* v, double* out_B, struct fm_env* env)
def Banzhaf(v, env):
    trace( "void py_Banzhaf(double* v, double* out_B, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_Bnp, pout_B = create_float_zeros_as_CFFI_double( env.n)
    fm.py_Banzhaf( pv, pout_B, env)
    return pout_Bnp


# Generated python wrapper for:
#    void py_ShapleyMob(double* Mob, double* out_x, struct fm_env* env)
def ShapleyMob(Mob, env):
    trace( "void py_ShapleyMob(double* Mob, double* out_x, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    pout_xnp, pout_x = create_float_zeros_as_CFFI_double( env.n)
    fm.py_ShapleyMob( pMob, pout_x, env)
    return pout_xnp


# Generated python wrapper for:
#    void py_BanzhafMob(double* Mob, double* out_B, struct fm_env* env)
def BanzhafMob(Mob, env):
    trace( "void py_BanzhafMob(double* Mob, double* out_B, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    pout_Bnp, pout_B = create_float_zeros_as_CFFI_double( env.n)
    fm.py_BanzhafMob( pMob, pout_B, env)
    return pout_Bnp


# Generated python wrapper for:
#    double py_ChoquetKinter(double* x, double* v, int kint, struct fm_env* env)
def ChoquetKinter(x, v, kint, env):
    trace( "double py_ChoquetKinter(double* x, double* v, int kint, struct fm_env* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_ChoquetKinter( px, pv, kint, env)
    return yy


# Generated python wrapper for:
#    double py_ChoquetMob(double* x, double* Mob, struct fm_env* env)
def ChoquetMob(x, Mob, env):
    trace( "double py_ChoquetMob(double* x, double* Mob, struct fm_env* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_ChoquetMob( px, pMob, env)
    return yy


# Generated python wrapper for:
#    void py_ConstructLambdaMeasure(double* singletons, double* out_lambdax, double* out_v, struct fm_env* env)
def ConstructLambdaMeasure(singletons, env):
    trace( "void py_ConstructLambdaMeasure(double* singletons, double* out_lambdax, double* out_v, struct fm_env* env)")
    psingletonsnp, psingletons = convert_py_float_to_cffi( singletons)
    pout_lambdaxnp, pout_lambdax = create_float_zeros_as_CFFI_double( env.m)
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    fm.py_ConstructLambdaMeasure( psingletons, pout_lambdax, pout_v, env)
    return pout_lambdaxnp, pout_vnp


# Generated python wrapper for:
#    void py_ConstructLambdaMeasureMob(double* singletons, double* out_lambdax, double* out_Mob, struct fm_env* env)
def ConstructLambdaMeasureMob(singletons, env):
    trace( "void py_ConstructLambdaMeasureMob(double* singletons, double* out_lambdax, double* out_Mob, struct fm_env* env)")
    psingletonsnp, psingletons = convert_py_float_to_cffi( singletons)
    pout_lambdaxnp, pout_lambdax = create_float_zeros_as_CFFI_double( env.m)
    pout_Mobnp, pout_Mob = create_float_zeros_as_CFFI_double( env.m)
    fm.py_ConstructLambdaMeasureMob( psingletons, pout_lambdax, pout_Mob, env)
    return pout_lambdaxnp, pout_Mobnp


# Generated python wrapper for:
#    void py_dualm(double* v, double* out_w, struct fm_env* env)
def dualm(v, env):
    trace( "void py_dualm(double* v, double* out_w, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_dualm( pv, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_dualmMob(double* v, double* out_w, struct fm_env* env)
def dualmMob(v, env):
    trace( "void py_dualmMob(double* v, double* out_w, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_dualmMob( pv, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    double py_Entropy(double* v, struct fm_env* env)
def Entropy(v, env):
    trace( "double py_Entropy(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_Entropy( pv, env)
    return yy


# Generated python wrapper for:
#    void py_FuzzyMeasureFit(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)
def FuzzyMeasureFit(datanum, additive, env, dataset):
    trace( "void py_FuzzyMeasureFit(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    fm.py_FuzzyMeasureFit( datanum, additive, env, pout_v, pdataset)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitMob(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)
def FuzzyMeasureFitMob(datanum, additive, env, dataset):
    trace( "void py_FuzzyMeasureFitMob(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    fm.py_FuzzyMeasureFitMob( datanum, additive, env, pout_v, pdataset)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitKtolerant(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)
def FuzzyMeasureFitKtolerant(datanum, additive, env, dataset):
    trace( "void py_FuzzyMeasureFitKtolerant(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    fm.py_FuzzyMeasureFitKtolerant( datanum, additive, env, pout_v, pdataset)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLPKmaxitive(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)
def FuzzyMeasureFitLPKmaxitive(datanum, additive, env, dataset):
    trace( "void py_FuzzyMeasureFitLPKmaxitive(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    fm.py_FuzzyMeasureFitLPKmaxitive( datanum, additive, env, pout_v, pdataset)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLPKinteractive(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K)
def FuzzyMeasureFitLPKinteractive(datanum, additive, env, dataset, K):
    trace( "void py_FuzzyMeasureFitLPKinteractive(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    pKnp, pK = convert_py_float_to_cffi( K)
    fm.py_FuzzyMeasureFitLPKinteractive( datanum, additive, env, pout_v, pdataset, pK)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLPKinteractiveMaxChains(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K)
def FuzzyMeasureFitLPKinteractiveMaxChains(datanum, additive, env, dataset, K):
    trace( "void py_FuzzyMeasureFitLPKinteractiveMaxChains(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    pKnp, pK = convert_py_float_to_cffi( K)
    fm.py_FuzzyMeasureFitLPKinteractiveMaxChains( datanum, additive, env, pout_v, pdataset, pK)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLPKinteractiveAutoK(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K, int* maxiters)
def FuzzyMeasureFitLPKinteractiveAutoK(datanum, additive, env, dataset, K, maxiters):
    trace( "void py_FuzzyMeasureFitLPKinteractiveAutoK(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K, int* maxiters)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    pKnp, pK = convert_py_float_to_cffi( K)
    pmaxitersnp, pmaxiters = convert_py_int_to_cffi( maxiters)
    fm.py_FuzzyMeasureFitLPKinteractiveAutoK( datanum, additive, env, pout_v, pdataset, pK, pmaxiters)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLPKinteractiveMarginal(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K, int submod)
def FuzzyMeasureFitLPKinteractiveMarginal(datanum, additive, env, dataset, K, submod):
    trace( "void py_FuzzyMeasureFitLPKinteractiveMarginal(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K, int submod)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    pKnp, pK = convert_py_float_to_cffi( K)
    fm.py_FuzzyMeasureFitLPKinteractiveMarginal( datanum, additive, env, pout_v, pdataset, pK, submod)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLPKinteractiveMarginalMaxChain(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K, int* maxiters, int submod)
def FuzzyMeasureFitLPKinteractiveMarginalMaxChain(datanum, additive, env, dataset, K, maxiters, submod):
    trace( "void py_FuzzyMeasureFitLPKinteractiveMarginalMaxChain(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, double* K, int* maxiters, int submod)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    pKnp, pK = convert_py_float_to_cffi( K)
    pmaxitersnp, pmaxiters = convert_py_int_to_cffi( maxiters)
    fm.py_FuzzyMeasureFitLPKinteractiveMarginalMaxChain( datanum, additive, env, pout_v, pdataset, pK, pmaxiters, submod)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLP(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, int* options, double* indexlow, double* indexhihg, int* option1, double* orness)
def FuzzyMeasureFitLP(datanum, additive, env, dataset, options, indexlow, indexhihg, option1, orness):
    trace( "void py_FuzzyMeasureFitLP(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, int* options, double* indexlow, double* indexhihg, int* option1, double* orness)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    poptionsnp, poptions = convert_py_int_to_cffi( options)
    pindexlownp, pindexlow = convert_py_float_to_cffi( indexlow)
    pindexhihgnp, pindexhihg = convert_py_float_to_cffi( indexhihg)
    poption1np, poption1 = convert_py_int_to_cffi( option1)
    pornessnp, porness = convert_py_float_to_cffi( orness)
    fm.py_FuzzyMeasureFitLP( datanum, additive, env, pout_v, pdataset, poptions, pindexlow, pindexhihg, poption1, porness)
    return pout_vnp


# Generated python wrapper for:
#    void py_FuzzyMeasureFitLPMob(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, int* options, double* indexlow, double* indexhihg, int* option1, double* orness)
def FuzzyMeasureFitLPMob(datanum, additive, env, dataset, options, indexlow, indexhihg, option1, orness):
    trace( "void py_FuzzyMeasureFitLPMob(int datanum, int additive, struct fm_env* env, double* out_v, double* dataset, int* options, double* indexlow, double* indexhihg, int* option1, double* orness)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    poptionsnp, poptions = convert_py_int_to_cffi( options)
    pindexlownp, pindexlow = convert_py_float_to_cffi( indexlow)
    pindexhihgnp, pindexhihg = convert_py_float_to_cffi( indexhihg)
    poption1np, poption1 = convert_py_int_to_cffi( option1)
    pornessnp, porness = convert_py_float_to_cffi( orness)
    fm.py_FuzzyMeasureFitLPMob( datanum, additive, env, pout_v, pdataset, poptions, pindexlow, pindexhihg, poption1, porness)
    return pout_vnp


# Generated python wrapper for:
#    void py_fittingOWA(int datanum, struct fm_env* env, double* out_v, double* dataset)
def fittingOWA(datanum, env, dataset):
    trace( "void py_fittingOWA(int datanum, struct fm_env* env, double* out_v, double* dataset)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    fm.py_fittingOWA( datanum, env, pout_v, pdataset)
    return pout_vnp


# Generated python wrapper for:
#    void py_fittingWAM(int datanum, struct fm_env* env, double* out_v, double* dataset)
def fittingWAM(datanum, env, dataset):
    trace( "void py_fittingWAM(int datanum, struct fm_env* env, double* out_v, double* dataset)")
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    pdatasetnp, pdataset = convert_py_float_to_cffi( dataset)
    fm.py_fittingWAM( datanum, env, pout_v, pdataset)
    return pout_vnp


# Generated python wrapper for:
#    void py_Interaction(double* out_Mob, double* v, struct fm_env* env)
def Interaction(v, env):
    trace( "void py_Interaction(double* out_Mob, double* v, struct fm_env* env)")
    pout_Mobnp, pout_Mob = create_float_zeros_as_CFFI_double( env.m)
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_Interaction( pout_Mob, pv, env)
    return pout_Mobnp


# Generated python wrapper for:
#    void py_InteractionB(double* out_Mob, double* v, struct fm_env* env)
def InteractionB(v, env):
    trace( "void py_InteractionB(double* out_Mob, double* v, struct fm_env* env)")
    pout_Mobnp, pout_Mob = create_float_zeros_as_CFFI_double( env.m)
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_InteractionB( pout_Mob, pv, env)
    return pout_Mobnp


# Generated python wrapper for:
#    void py_InteractionMob(double* out_Mob, double* v, struct fm_env* env)
def InteractionMob(v, env):
    trace( "void py_InteractionMob(double* out_Mob, double* v, struct fm_env* env)")
    pout_Mobnp, pout_Mob = create_float_zeros_as_CFFI_double( env.m)
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_InteractionMob( pout_Mob, pv, env)
    return pout_Mobnp


# Generated python wrapper for:
#    void py_InteractionBMob(double* Mob, double* out_v, struct fm_env* env)
def InteractionBMob(Mob, env):
    trace( "void py_InteractionBMob(double* Mob, double* out_v, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    fm.py_InteractionBMob( pMob, pout_v, env)
    return pout_vnp


# Generated python wrapper for:
#    void py_BipartitionShapleyIndex(double* v, double* out_w, struct fm_env* env)
def BipartitionShapleyIndex(v, env):
    trace( "void py_BipartitionShapleyIndex(double* v, double* out_w, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_BipartitionShapleyIndex( pv, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_BipartitionBanzhafIndex(double* v, double* out_w, struct fm_env* env)
def BipartitionBanzhafIndex(v, env):
    trace( "void py_BipartitionBanzhafIndex(double* v, double* out_w, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_BipartitionBanzhafIndex( pv, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_BNonadditivityIndexMob(double* Mob, double* out_w, struct fm_env* env)
def BNonadditivityIndexMob(Mob, env):
    trace( "void py_BNonadditivityIndexMob(double* Mob, double* out_w, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_BNonadditivityIndexMob( pMob, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_NonadditivityIndex(double* v, double* out_w, struct fm_env* env)
def NonadditivityIndex(v, env):
    trace( "void py_NonadditivityIndex(double* v, double* out_w, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_NonadditivityIndex( pv, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_NonmodularityIndex(double* v, double* out_w, struct fm_env* env)
def NonmodularityIndex(v, env):
    trace( "void py_NonmodularityIndex(double* v, double* out_w, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_NonmodularityIndex( pv, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_NonmodularityIndexMob(double* Mob, double* out_w, struct fm_env* env)
def NonmodularityIndexMob(Mob, env):
    trace( "void py_NonmodularityIndexMob(double* Mob, double* out_w, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_NonmodularityIndexMob( pMob, pout_w, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_NonmodularityIndexKinteractive(double* v, double* out_w, int kint,  struct fm_env* env)
def NonmodularityIndexKinteractive(v, kint, env):
    trace( "void py_NonmodularityIndexKinteractive(double* v, double* out_w, int kint,  struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_NonmodularityIndexKinteractive( pv, pout_w, kint, env)
    return pout_wnp


# Generated python wrapper for:
#    void py_NonmodularityIndexMobkadditive(double* Mob, double* out_w, int k,  struct fm_env* env)
def NonmodularityIndexMobkadditive(Mob, k, env):
    trace( "void py_NonmodularityIndexMobkadditive(double* Mob, double* out_w, int k,  struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    pout_wnp, pout_w = create_float_zeros_as_CFFI_double( env.m)
    fm.py_NonmodularityIndexMobkadditive( pMob, pout_w, k, env)
    return pout_wnp


# Generated python wrapper for:
#    int py_IsMeasureBalanced(double* v, struct fm_env* env)
def IsMeasureBalanced(v, env):
    trace( "int py_IsMeasureBalanced(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_IsMeasureBalanced( pv, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSelfdual(double* v, struct fm_env* env)
def IsMeasureSelfdual(v, env):
    trace( "int py_IsMeasureSelfdual(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_IsMeasureSelfdual( pv, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSubadditive(double* v, struct fm_env* env)
def IsMeasureSubadditive(v, env):
    trace( "int py_IsMeasureSubadditive(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_IsMeasureSubadditive( pv, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSubmodular(double* v, struct fm_env* env)
def IsMeasureSubmodular(v, env):
    trace( "int py_IsMeasureSubmodular(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_IsMeasureSubmodular( pv, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSuperadditive(double* v, struct fm_env* env)
def IsMeasureSuperadditive(v, env):
    trace( "int py_IsMeasureSuperadditive(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_IsMeasureSuperadditive( pv, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSymmetric(double* v, struct fm_env* env)
def IsMeasureSymmetric(v, env):
    trace( "int py_IsMeasureSymmetric(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_IsMeasureSymmetric( pv, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureKMaxitive(double* v, struct fm_env* env)
def IsMeasureKMaxitive(v, env):
    trace( "int py_IsMeasureKMaxitive(double* v, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_IsMeasureKMaxitive( pv, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureAdditiveMob(double* Mob, struct fm_env* env)
def IsMeasureAdditiveMob(Mob, env):
    trace( "int py_IsMeasureAdditiveMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureAdditiveMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureBalancedMob(double* Mob, struct fm_env* env)
def IsMeasureBalancedMob(Mob, env):
    trace( "int py_IsMeasureBalancedMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureBalancedMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSelfdualMob(double* Mob, struct fm_env* env)
def IsMeasureSelfdualMob(Mob, env):
    trace( "int py_IsMeasureSelfdualMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureSelfdualMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSubadditiveMob(double* Mob, struct fm_env* env)
def IsMeasureSubadditiveMob(Mob, env):
    trace( "int py_IsMeasureSubadditiveMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureSubadditiveMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSubmodularMob(double* Mob, struct fm_env* env)
def IsMeasureSubmodularMob(Mob, env):
    trace( "int py_IsMeasureSubmodularMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureSubmodularMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSuperadditiveMob(double* Mob, struct fm_env* env)
def IsMeasureSuperadditiveMob(Mob, env):
    trace( "int py_IsMeasureSuperadditiveMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureSuperadditiveMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSupermodularMob(double* Mob, struct fm_env* env)
def IsMeasureSupermodularMob(Mob, env):
    trace( "int py_IsMeasureSupermodularMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureSupermodularMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureSymmetricMob(double* Mob, struct fm_env* env)
def IsMeasureSymmetricMob(Mob, env):
    trace( "int py_IsMeasureSymmetricMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureSymmetricMob( pMob, env)
    return yy


# Generated python wrapper for:
#    int py_IsMeasureKMaxitiveMob(double* Mob, struct fm_env* env)
def IsMeasureKMaxitiveMob(Mob, env):
    trace( "int py_IsMeasureKMaxitiveMob(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_IsMeasureKMaxitiveMob( pMob, env)
    return yy


# Generated python wrapper for:
#    void py_Mobius(double* v, double* out_MobVal, struct fm_env* env)
def Mobius(v, env):
    trace( "void py_Mobius(double* v, double* out_MobVal, struct fm_env* env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_MobValnp, pout_MobVal = create_float_zeros_as_CFFI_double( env.m)
    fm.py_Mobius( pv, pout_MobVal, env)
    return pout_MobValnp


# Generated python wrapper for:
#    double py_Orness(double* Mob, struct fm_env* env)
def Orness(Mob, env):
    trace( "double py_Orness(double* Mob, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_Orness( pMob, env)
    return yy


# Generated python wrapper for:
#    double py_OWA(double* x, double* v, struct fm_env* env)
def OWA(x, v, env):
    trace( "double py_OWA(double* x, double* v, struct fm_env* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_OWA( px, pv, env)
    return yy


# Generated python wrapper for:
#    double py_WAM(double* x, double* v, struct fm_env* env)
def WAM(x, v, env):
    trace( "double py_WAM(double* x, double* v, struct fm_env* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_WAM( px, pv, env)
    return yy


# Generated python wrapper for:
#    void py_Zeta(double* Mob, double* out_v, struct fm_env* env)
def Zeta(Mob, env):
    trace( "void py_Zeta(double* Mob, double* out_v, struct fm_env* env)")
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    pout_vnp, pout_v = create_float_zeros_as_CFFI_double( env.m)
    fm.py_Zeta( pMob, pout_v, env)
    return pout_vnp


# Generated python wrapper for:
#    void py_dualMobKadd(int m, int length, int k, double* src, double* out_dest, struct fm_env* env)
def dualMobKadd(k, src, env):
    trace( "void py_dualMobKadd(int m, int length, int k, double* src, double* out_dest, struct fm_env* env)")
    psrcnp, psrc = convert_py_float_to_cffi( src)
    pout_destnp, pout_dest = create_float_zeros_as_CFFI_double( env.m)
    length = fm.py_fm_arraysize( env.n, k, env)
    fm.py_dualMobKadd( env.m, length, k, psrc, pout_dest, env)
    return pout_destnp


# Generated python wrapper for:
#    void py_Shapley2addMob(double* v, double* out_x, int n)
def Shapley2addMob(v, n):
    trace( "void py_Shapley2addMob(double* v, double* out_x, int n)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_xnp, pout_x = create_float_zeros_as_CFFI_double( n)
    fm.py_Shapley2addMob( pv, pout_x, n)
    return pout_xnp


# Generated python wrapper for:
#    void py_Banzhaf2addMob(double* v, double* out_x, int n)
def Banzhaf2addMob(v, n):
    trace( "void py_Banzhaf2addMob(double* v, double* out_x, int n)")
    pvnp, pv = convert_py_float_to_cffi( v)
    pout_xnp, pout_x = create_float_zeros_as_CFFI_double( n)
    fm.py_Banzhaf2addMob( pv, pout_x, n)
    return pout_xnp


# Generated python wrapper for:
#    double py_Choquet2addMob(double* x, double* Mob, int n)
def Choquet2addMob(x, Mob, n):
    trace( "double py_Choquet2addMob(double* x, double* Mob, int n)")
    pxnp, px = convert_py_float_to_cffi( x)
    pMobnp, pMob = convert_py_float_to_cffi( Mob)
    yy = fm.py_Choquet2addMob( px, pMob, n)
    return yy


# Generated python wrapper for:
#    int py_fm_arraysize(int n, int kint, struct fm_env* env)
def fm_arraysize(n, kint, env):
    trace( "int py_fm_arraysize(int n, int kint, struct fm_env* env)")
    yy = fm.py_fm_arraysize( n, kint, env)
    return yy


# Generated python wrapper for:
#    int py_generate_fm_minplus(int num, int n, int kint, int markov, int option, double K, double* vv, struct fm_env* env)
def generate_fm_minplus(num, n, kint, markov, option, K, vv, env):
    trace( "int py_generate_fm_minplus(int num, int n, int kint, int markov, int option, double K, double* vv, struct fm_env* env)")
    pvvnp, pvv = convert_py_float_to_cffi( vv)
    yy = fm.py_generate_fm_minplus( num, n, kint, markov, option, K, pvv, env)
    return yy


# Generated python wrapper for:
#    int py_generate_fm_2additive_convex(int num, int n,  double* vv)
def generate_fm_2additive_convex(num, n, vv):
    trace( "int py_generate_fm_2additive_convex(int num, int n,  double* vv)")
    pvvnp, pvv = convert_py_float_to_cffi( vv)
    yy = fm.py_generate_fm_2additive_convex( num, n, pvv)
    return yy


# Generated python wrapper for:
#    int py_generate_fm_2additive_convex_withsomeindependent(int num, int n, double* vv)
def generate_fm_2additive_convex_withsomeindependent(num, n, vv):
    trace( "int py_generate_fm_2additive_convex_withsomeindependent(int num, int n, double* vv)")
    pvvnp, pvv = convert_py_float_to_cffi( vv)
    yy = fm.py_generate_fm_2additive_convex_withsomeindependent( num, n, pvv)
    return yy


# Generated python wrapper for:
#    void py_prepare_fm_sparse(int n, int tupsize, int* tuples, struct fm_env_sparse* out_env)
def prepare_fm_sparse(n, tupsize, tuples, out_env):
    trace( "void py_prepare_fm_sparse(int n, int tupsize, int* tuples, struct fm_env_sparse* out_env)")
    ptuplesnp, ptuples = convert_py_int_to_cffi( tuples)
    fm.py_prepare_fm_sparse( n, tupsize, ptuples, out_env)
    return out_env


# Generated python wrapper for:
#    int py_tuple_cardinality_sparse(int i, struct fm_env_sparse* env)
def tuple_cardinality_sparse(i, env):
    trace( "int py_tuple_cardinality_sparse(int i, struct fm_env_sparse* env)")
    yy = fm.py_tuple_cardinality_sparse( i, env)
    return yy


# Generated python wrapper for:
#    int py_get_num_tuples(struct fm_env_sparse* env)
def get_num_tuples(env):
    trace( "int py_get_num_tuples(struct fm_env_sparse* env)")
    yy = fm.py_get_num_tuples( env)
    return yy


# Generated python wrapper for:
#    int py_get_sizearray_tuples(struct fm_env_sparse* env)
def get_sizearray_tuples(env):
    trace( "int py_get_sizearray_tuples(struct fm_env_sparse* env)")
    yy = fm.py_get_sizearray_tuples( env)
    return yy


# Generated python wrapper for:
#    int py_is_inset_sparse(int A, int card, int i, struct fm_env_sparse* env)
def is_inset_sparse(A, card, i, env):
    trace( "int py_is_inset_sparse(int A, int card, int i, struct fm_env_sparse* env)")
    yy = fm.py_is_inset_sparse( A, card, i, env)
    return yy


# Generated python wrapper for:
#    int py_is_subset_sparse(int A, int cardA, int B, int cardB, struct fm_env_sparse* env)
def is_subset_sparse(A, cardA, B, cardB, env):
    trace( "int py_is_subset_sparse(int A, int cardA, int B, int cardB, struct fm_env_sparse* env)")
    yy = fm.py_is_subset_sparse( A, cardA, B, cardB, env)
    return yy


# Generated python wrapper for:
#    double py_min_subset_sparse(double* x, int n, int S, int cardS, struct fm_env_sparse* env)
def min_subset_sparse(x, n, S, cardS, env):
    trace( "double py_min_subset_sparse(double* x, int n, int S, int cardS, struct fm_env_sparse* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    yy = fm.py_min_subset_sparse( px, n, S, cardS, env)
    return yy


# Generated python wrapper for:
#    double py_max_subset_sparse(double* x, int n, int S, int cardS, struct fm_env_sparse* env)
def max_subset_sparse(x, n, S, cardS, env):
    trace( "double py_max_subset_sparse(double* x, int n, int S, int cardS, struct fm_env_sparse* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    yy = fm.py_max_subset_sparse( px, n, S, cardS, env)
    return yy


# Generated python wrapper for:
#    double py_ChoquetMob_sparse(double* x, int n, struct fm_env_sparse* env)
def ChoquetMob_sparse(x, n, env):
    trace( "double py_ChoquetMob_sparse(double* x, int n, struct fm_env_sparse* env)")
    pxnp, px = convert_py_float_to_cffi( x)
    yy = fm.py_ChoquetMob_sparse( px, n, env)
    return yy


# Generated python wrapper for:
#    void py_ShapleyMob_sparse(double* v, int n, struct fm_env_sparse* out_env)
def ShapleyMob_sparse(v, n, out_env):
    trace( "void py_ShapleyMob_sparse(double* v, int n, struct fm_env_sparse* out_env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_ShapleyMob_sparse( pv, n, out_env)
    return out_env


# Generated python wrapper for:
#    void py_BanzhafMob_sparse(double* v, int n, struct fm_env_sparse* out_env)
def BanzhafMob_sparse(v, n, out_env):
    trace( "void py_BanzhafMob_sparse(double* v, int n, struct fm_env_sparse* out_env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_BanzhafMob_sparse( pv, n, out_env)
    return out_env


# Generated python wrapper for:
#    void py_populate_fm_2add_sparse(double* singletons, int numpairs, double* pairs, int* indicesp1, int* indicesp2, struct fm_env_sparse* out_env)
def populate_fm_2add_sparse(singletons, numpairs, pairs, indicesp1, indicesp2, out_env):
    trace( "void py_populate_fm_2add_sparse(double* singletons, int numpairs, double* pairs, int* indicesp1, int* indicesp2, struct fm_env_sparse* out_env)")
    psingletonsnp, psingletons = convert_py_float_to_cffi( singletons)
    ppairsnp, ppairs = convert_py_float_to_cffi( pairs)
    pindicesp1np, pindicesp1 = convert_py_int_to_cffi( indicesp1)
    pindicesp2np, pindicesp2 = convert_py_int_to_cffi( indicesp2)
    fm.py_populate_fm_2add_sparse( psingletons, numpairs, ppairs, pindicesp1, pindicesp2, out_env)
    return out_env


# Generated python wrapper for:
#    void py_add_pair_sparse(int i, int j, double v, struct fm_env_sparse* out_env)
def add_pair_sparse(i, j, v, out_env):
    trace( "void py_add_pair_sparse(int i, int j, double v, struct fm_env_sparse* out_env)")
    fm.py_add_pair_sparse( i, j, v, out_env)
    return out_env


# Generated python wrapper for:
#    void py_add_tuple_sparse(int tupsize, int* tuple, double v, struct fm_env_sparse* out_env)
def add_tuple_sparse(tupsize, tuple, v, out_env):
    trace( "void py_add_tuple_sparse(int tupsize, int* tuple, double v, struct fm_env_sparse* out_env)")
    ptuplenp, ptuple = convert_py_int_to_cffi( tuple)
    fm.py_add_tuple_sparse( tupsize, ptuple, v, out_env)
    return out_env


# Generated python wrapper for:
#    void py_populate_fm_2add_sparse_from2add(int n, double* v, struct fm_env_sparse* out_env)
def populate_fm_2add_sparse_from2add(n, v, out_env):
    trace( "void py_populate_fm_2add_sparse_from2add(int n, double* v, struct fm_env_sparse* out_env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_populate_fm_2add_sparse_from2add( n, pv, out_env)
    return out_env


# Generated python wrapper for:
#    void py_expand_2add_full(double* v, struct fm_env_sparse* out_env)
def expand_2add_full(v, out_env):
    trace( "void py_expand_2add_full(double* v, struct fm_env_sparse* out_env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_expand_2add_full( pv, out_env)
    return out_env


# Generated python wrapper for:
#    void py_expand_sparse_full(double* v, struct fm_env_sparse* out_env)
def expand_sparse_full(v, out_env):
    trace( "void py_expand_sparse_full(double* v, struct fm_env_sparse* out_env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_expand_sparse_full( pv, out_env)
    return out_env


# Generated python wrapper for:
#    void py_sparse_get_singletons(int n, double* v, struct fm_env_sparse* out_env)
def sparse_get_singletons(n, v, out_env):
    trace( "void py_sparse_get_singletons(int n, double* v, struct fm_env_sparse* out_env)")
    pvnp, pv = convert_py_float_to_cffi( v)
    fm.py_sparse_get_singletons( n, pv, out_env)
    return out_env


# Generated python wrapper for:
#    int py_sparse_get_pairs(int* pairs, double* v, struct fm_env_sparse* env)
def sparse_get_pairs(pairs, v, env):
    trace( "int py_sparse_get_pairs(int* pairs, double* v, struct fm_env_sparse* env)")
    ppairsnp, ppairs = convert_py_int_to_cffi( pairs)
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_sparse_get_pairs( ppairs, pv, env)
    return yy


# Generated python wrapper for:
#    int py_sparse_get_tuples(int* tuples, double* v, struct fm_env_sparse* env)
def sparse_get_tuples(tuples, v, env):
    trace( "int py_sparse_get_tuples(int* tuples, double* v, struct fm_env_sparse* env)")
    ptuplesnp, ptuples = convert_py_int_to_cffi( tuples)
    pvnp, pv = convert_py_float_to_cffi( v)
    yy = fm.py_sparse_get_tuples( ptuples, pv, env)
    return yy


# Generated python wrapper for:
#    int   py_generate_fm_2additive_convex_sparse(int n, struct fm_env_sparse* env)
def generate_fm_2additive_convex_sparse(n, env):
    trace( "int   py_generate_fm_2additive_convex_sparse(int n, struct fm_env_sparse* env)")
    yy = fm.py_generate_fm_2additive_convex_sparse( n, env)
    return yy


# Generated python wrapper for:
#    int   py_generate_fm_kadditive_convex_sparse(int n, int k, int nonzero, struct fm_env_sparse* env)
def generate_fm_kadditive_convex_sparse(n, k, nonzero, env):
    trace( "int   py_generate_fm_kadditive_convex_sparse(int n, int k, int nonzero, struct fm_env_sparse* env)")
    yy = fm.py_generate_fm_kadditive_convex_sparse( n, k, nonzero, env)
    return yy


# Generated python wrapper for:
#    void py_Nonmodularityindex_sparse(double* w, int n, struct fm_env_sparse* out_env)
def Nonmodularityindex_sparse(w, n, out_env):
    trace( "void py_Nonmodularityindex_sparse(double* w, int n, struct fm_env_sparse* out_env)")
    pwnp, pw = convert_py_float_to_cffi( w)
    fm.py_Nonmodularityindex_sparse( pw, n, out_env)
    return out_env


