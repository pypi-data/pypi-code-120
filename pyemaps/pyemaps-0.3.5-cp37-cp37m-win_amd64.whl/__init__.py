
"""
This file is part of pyemaps
___________________________

pyemaps is free software for non-comercial use: you can 
redistribute it and/or modify it under the terms of the GNU General 
Public License as published by the Free Software Foundation, either 
version 3 of the License, or (at your option) any later version.

pyemaps is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyemaps.  If not, see <https://www.gnu.org/licenses/>.

Contact supprort@emlabsoftware.com for any questions and comments.
___________________________

__pyemaps__ package is a collection of python modules and libraries that simulate
 transmission electron diffraction with selected crystals, designed for crystal 
 electron microscope diffraction simulations and related crystallographic calculations. 
 
 Main features include:

>**Crystal** : crystal data module, classes and methods loading crystal data from various sources, including diffraction patterns generation based on the crystal data and microscope and sample control parameters

>**DP** :  kinematic diffraction python class. It encapsulates diffraction pattern data generated by the Crystal class instance and diffraction pattern visualization methods such as plotting Kikuchi and HOLZ lines, and diffraction spots or disks and their indices. 



__pyemaps__ is based on the proprietary Fortran applications released as backend of [cloudEMAPS2.0](https://emaps.emlabsolutions.com). 

Future releases planned include:

>*Bloch* : dynamic Bloch wave simulation.

Check [EMlab Solution, Inc.](https://www.emlabsolutions.com) for updates and releases. We welcome comments and suggestions from our user community. For reporting any issues and requesting pyemaps improvements, or sharing scripts using __pyemaps__, please go to [our support page](https://www.emlabsolutions.com/contact/). 

We ask for your support and donation to continue to provide free software packages like this to make impact in research and education in microscopy and crystallography.  

## Installation

```
python -m pip pyemaps
```
or
```
 pip install pyemaps
```

## Basic Usage

```
from pyemaps import Crystal
from pyemaps import DP
```

Author:     EMLab Solutions, Inc.
Date:       May 07, 2022    
"""


from pyemaps import __config__

#from diffraction extension
from .diffract import dif

#Wrappers class around diffraction extensions

from .crystals import Crystal

#Microscope control data classes handling data properties
from .emcontrols import EMControl as EMC

#diffraction classes handling diffraction patter data
from .kdiffs import diffPattern as DP
from .kdiffs import Diffraction as DPList

#Extension control defaults
#       DEF_CONTROLS --- default controls in dictionary object
#       DEF_CONTROLS = dict(zone = (0,0,1),
#                     tilt = (0.0,0.0),
#                     defl = (0.0,0.0),
#                     cl = 1000,
#                     vt = 200
#                     )
#       DEF_CBED_DSIZE --- default DP spot cricle size in CBED mode
#       XMAX YMAX --- DP generation bound (-XMAX, XMAX, -YMAX, YMAX)
#
#       THESE CONSTANTS ARE SET IN PYEMAPS DIF MODULE
from .emcontrols import DEF_CONTROLS, DEF_CBED_DSIZE
from .kdiffs import XMAX, YMAX, DEF_MODE