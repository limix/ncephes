from __future__ import absolute_import

from ._testit import test

try:
    from . import _ffi

    ffi = _ffi.ffi
except Exception as e:
    msg = "\nIt is likely caused by a broken installation of this package."
    msg += "\nPlease, make sure you have a C compiler and try to uninstall"
    msg += "\nand reinstall the package again."
    e.msg = e.msg + msg
    raise e


from ._ffi.lib import hcephes_bdtr as bdtr
from ._ffi.lib import hcephes_bdtrc as bdtrc
from ._ffi.lib import hcephes_bdtri as bdtri
from ._ffi.lib import hcephes_beta as beta
from ._ffi.lib import hcephes_btdtr as btdtr
from ._ffi.lib import hcephes_cabs as cabs
from ._ffi.lib import hcephes_cbrt as cbrt
from ._ffi.lib import hcephes_chbevl as chbevl
from ._ffi.lib import hcephes_chdtr as chdtr
from ._ffi.lib import hcephes_chdtrc as chdtrc
from ._ffi.lib import hcephes_chdtri as chdtri
from ._ffi.lib import hcephes_cosm1 as cosm1
from ._ffi.lib import hcephes_dawsn as dawsn
from ._ffi.lib import hcephes_ei as ei
from ._ffi.lib import hcephes_ellie as ellie
from ._ffi.lib import hcephes_ellik as ellik
from ._ffi.lib import hcephes_ellpe as ellpe
from ._ffi.lib import hcephes_ellpk as ellpk
from ._ffi.lib import hcephes_erf as erf
from ._ffi.lib import hcephes_erfc as erfc
from ._ffi.lib import hcephes_erfce as erfce
from ._ffi.lib import hcephes_euclid as euclid
from ._ffi.lib import hcephes_expm1 as expm1
from ._ffi.lib import hcephes_expn as expn
from ._ffi.lib import hcephes_expx2 as expx2
from ._ffi.lib import hcephes_fac as fac
from ._ffi.lib import hcephes_fdtr as fdtr
from ._ffi.lib import hcephes_fdtrc as fdtrc
from ._ffi.lib import hcephes_fdtri as fdtri
from ._ffi.lib import hcephes_gamma as gamma
from ._ffi.lib import hcephes_gdtr as gdtr
from ._ffi.lib import hcephes_gdtrc as gdtrc
from ._ffi.lib import hcephes_hyp2f0 as hyp2f0
from ._ffi.lib import hcephes_hyp2f1 as hyp2f1
from ._ffi.lib import hcephes_hyperg as hyperg
from ._ffi.lib import hcephes_hypot as hypot
from ._ffi.lib import hcephes_i0 as i0
from ._ffi.lib import hcephes_i0e as i0e
from ._ffi.lib import hcephes_i1 as i1
from ._ffi.lib import hcephes_i1e as i1e
from ._ffi.lib import hcephes_igam as igam
from ._ffi.lib import hcephes_igamc as igamc
from ._ffi.lib import hcephes_igami as igami
from ._ffi.lib import hcephes_incbet as incbet
from ._ffi.lib import hcephes_incbi as incbi
from ._ffi.lib import hcephes_iv as iv
from ._ffi.lib import hcephes_j0 as j0
from ._ffi.lib import hcephes_j1 as j1
from ._ffi.lib import hcephes_jn as jn
from ._ffi.lib import hcephes_jv as jv
from ._ffi.lib import hcephes_k0 as k0
from ._ffi.lib import hcephes_k0e as k0e
from ._ffi.lib import hcephes_k1 as k1
from ._ffi.lib import hcephes_k1e as k1e
from ._ffi.lib import hcephes_kn as kn
from ._ffi.lib import hcephes_kolmogi as kolmogi
from ._ffi.lib import hcephes_kolmogorov as kolmogorov
from ._ffi.lib import hcephes_lbeta as lbeta
from ._ffi.lib import hcephes_lgam_sgn as lgam_sgn
from ._ffi.lib import hcephes_lgam as lgam
from ._ffi.lib import hcephes_log1p as log1p
from ._ffi.lib import hcephes_nbdtr as nbdtr
from ._ffi.lib import hcephes_nbdtrc as nbdtrc
from ._ffi.lib import hcephes_nbdtri as nbdtri
from ._ffi.lib import hcephes_ndtr as ndtr
from ._ffi.lib import hcephes_ndtri as ndtri
from ._ffi.lib import hcephes_onef2 as onef2
from ._ffi.lib import hcephes_p1evl as p1evl
from ._ffi.lib import hcephes_pdtr as pdtr
from ._ffi.lib import hcephes_pdtrc as pdtrc
from ._ffi.lib import hcephes_pdtri as pdtri
from ._ffi.lib import hcephes_planckc as planckc
from ._ffi.lib import hcephes_planckd as planckd
from ._ffi.lib import hcephes_plancki as plancki
from ._ffi.lib import hcephes_planckw as planckw
from ._ffi.lib import hcephes_polevl as polevl
from ._ffi.lib import hcephes_polylog as polylog
from ._ffi.lib import hcephes_powi as powi
from ._ffi.lib import hcephes_psi as psi
from ._ffi.lib import hcephes_simpsn as simpsn
from ._ffi.lib import hcephes_smirnov as smirnov
from ._ffi.lib import hcephes_smirnovi as smirnovi
from ._ffi.lib import hcephes_spence as spence
from ._ffi.lib import hcephes_stdtr as stdtr
from ._ffi.lib import hcephes_stdtri as stdtri
from ._ffi.lib import hcephes_struve as struve
from ._ffi.lib import hcephes_threef0 as threef0
from ._ffi.lib import hcephes_y0 as y0
from ._ffi.lib import hcephes_y1 as y1
from ._ffi.lib import hcephes_yn as yn
from ._ffi.lib import hcephes_yv as yv
from ._ffi.lib import hcephes_zetac as zetac
from ._ffi.lib import hcephes_airy as airy
from ._ffi.lib import hcephes_drand as drand
from ._ffi.lib import hcephes_fresnl as fresnl
from ._ffi.lib import hcephes_mtherr as mtherr
from ._ffi.lib import hcephes_poldiv as poldiv
from ._ffi.lib import hcephes_polrt as polrt
from ._ffi.lib import hcephes_shichi as shichi
from ._ffi.lib import hcephes_sici as sici
from ._ffi.lib import hcephes_cadd as cadd
from ._ffi.lib import hcephes_cdiv as cdiv
from ._ffi.lib import hcephes_cmov as cmov
from ._ffi.lib import hcephes_cmul as cmul
from ._ffi.lib import hcephes_cneg as cneg
from ._ffi.lib import hcephes_csqrt as csqrt
from ._ffi.lib import hcephes_csub as csub
from ._ffi.lib import hcephes_poladd as poladd
from ._ffi.lib import hcephes_polclr as polclr
from ._ffi.lib import hcephes_polmov as polmov
from ._ffi.lib import hcephes_polmul as polmul
from ._ffi.lib import hcephes_polsbt as polsbt
from ._ffi.lib import hcephes_polsub as polsub
from ._ffi.lib import hcephes_radd as radd
from ._ffi.lib import hcephes_rdiv as rdiv
from ._ffi.lib import hcephes_revers as revers
from ._ffi.lib import hcephes_rmul as rmul
from ._ffi.lib import hcephes_rsub as rsub

try:
    from numba.cffi_support import register_module as _register_module

    _register_module(_ffi)
except ImportError:
    pass


__version__ = "1.1.0"

__all__ = [
    "__version__",
    "test",
    "bdtr",
    "bdtrc",
    "bdtri",
    "beta",
    "btdtr",
    "cabs",
    "cbrt",
    "chbevl",
    "chdtr",
    "chdtrc",
    "chdtri",
    "cosm1",
    "dawsn",
    "ei",
    "ellie",
    "ellik",
    "ellpe",
    "ellpk",
    "erf",
    "erfc",
    "erfce",
    "euclid",
    "expm1",
    "expn",
    "expx2",
    "fac",
    "fdtr",
    "fdtrc",
    "fdtri",
    "gamma",
    "gdtr",
    "gdtrc",
    "hyp2f0",
    "hyp2f1",
    "hyperg",
    "hypot",
    "i0",
    "i0e",
    "i1",
    "i1e",
    "igam",
    "igamc",
    "igami",
    "incbet",
    "incbi",
    "iv",
    "j0",
    "j1",
    "jn",
    "jv",
    "k0",
    "k0e",
    "k1",
    "k1e",
    "kn",
    "kolmogi",
    "kolmogorov",
    "lbeta",
    "lgam_sgn",
    "lgam",
    "log1p",
    "nbdtr",
    "nbdtrc",
    "nbdtri",
    "ndtr",
    "ndtri",
    "onef2",
    "p1evl",
    "pdtr",
    "pdtrc",
    "pdtri",
    "planckc",
    "planckd",
    "plancki",
    "planckw",
    "polevl",
    "polylog",
    "powi",
    "psi",
    "simpsn",
    "smirnov",
    "smirnovi",
    "spence",
    "stdtr",
    "stdtri",
    "struve",
    "threef0",
    "y0",
    "y1",
    "yn",
    "yv",
    "zetac",
    "airy",
    "drand",
    "fresnl",
    "mtherr",
    "poldiv",
    "polrt",
    "shichi",
    "sici",
    "cadd",
    "cdiv",
    "cmov",
    "cmul",
    "cneg",
    "csqrt",
    "csub",
    "poladd",
    "polclr",
    "polmov",
    "polmul",
    "polsbt",
    "polsub",
    "radd",
    "rdiv",
    "revers",
    "rmul",
    "rsub",
]
