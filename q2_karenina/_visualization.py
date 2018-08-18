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

import karenina.visualization as k_visualization
import pkg_resources
import qiime2
import q2templates
from q2_types.ordination import PCoAResults

def visualization(output_dir: str, pcoa : PCoAResults, metadata : qiime2.Metadata,
				 individual_col: str, timepoint_col: str, treatment_col: str):
    #Parse in pcoa and metadata as dataframes and inject to k_visualization
	pass