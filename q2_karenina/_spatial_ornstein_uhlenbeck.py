#/usr/bin/env python
from __future__ import division

__author__ = "Jesse Zaneveld"
__copyright__ = "Copyright 2016, The Karenina Project"
__credits__ = ["Jesse Zaneveld"]
__license__ = "GPL"
__version__ = "0.0.1-dev"
__maintainer__ = "Jesse Zaneveld"
__email__ = "zaneveld@gmail.com"
__status__ = "Development"

import karenina.spatial_ornstein_uhlenbeck as k_OU
import pkg_resources
import qiime2
import q2templates
from q2_types.ordination import PCoAResults
from q2_types.ordination import PCoAResults
from q2_types.distance_matrix import DistanceMatrix
		
def spatial_ornstein_uhlenbeck(perturbation_fp:str, treatment_names:str, n_individuals:str, 
							n_timepoints:int, perturbation_timepoint:int,
							perturbation_duration:int,interindividual_variation:float,
							delta:float,lam:float,fixed_start_pos:str) -> PCoAResults, DistanceMatrix:
	#pass items to k_OU, 
	#ensure that metadata is saved with both PcOAResults, and DistanceMatrix!
	pass