import qiime2.plugin

import q2_karenina
#from q2_karenina._spatial_ornstein_uhlenbeck import spatial_ornstien_uhlenbeck
from q2_karenina._fit_timeseries import fit_timeseries
from q2_karenina._visualization import visualization
from q2_types.ordination import PCoAResults
from qiime2.plugin import Metadata, Str, Choices


plugin = qiime2.plugin.Plugin(
    name='karenina',
    version=q2_karenina.__version__,
    website='https://github.com/zaneveld/karenina',
    package='q2_karenina',
    user_support_text=None,
	description="This script simulates microbiome " +
    "change over time using Ornstein-Uhlenbeck (OU) models.  These are " +
    "similar to Brownian motion models, with the exception that they " +
    "include reversion to a mean. Output is a tab-delimited data table " +
    "and figures.",
    citation_text=None
)

"""
plugin.methods.register_function(
	function=spatial_ornstien_uhlenbeck,
	inputs={
		#how about some input?
	},
	parameters={
		#how about some parameters?
	},
	outputs=[
		#metadata and pcoa
	],
	input_descriptions{
		#how about descriptions?
	},
	parameter_descriptions{
		#how about descriptions?
	},
	output_descriptions={
		#how about descriptions?
	},
	name='Spatial Ornstein Uhlenbeck microbial community simulation',
	description=("DESCRIPTION FROM ORIGINAL SCRIPT")
)
"""
	

plugin.visualizers.register_function(
    function=fit_timeseries,
    inputs={
        'pcoa' : PCoAResults
    },
    parameters={
        'method':Str % Choices({'basinhopping'}),
	    'metadata':Metadata,
	    'individual_col':Str,
	    'timepoint_col':Str,
	    'treatment_col':Str
    },
	parameter_descriptions = {
	    'method':'global optimization method',
	    'metadata':'Sample metadata',
	    'individual_col':'individual column identifier',
	    'timepoint_col':'timepoint column identifier',
	    'treatment_col':'treatment column identifier'
    },
    name='Fit OU Models to PCoA Ordination output',
    description='This visualizer generates OU model parameters for PCoA output'
                'data, for each individual and each defined treatment cohort.'
)

plugin.visualizers.register_function(
    function=visualization,
    inputs={
        'pcoa' : PCoAResults
    },
    parameters={
	    'metadata':Metadata,
	    'individual_col':Str,
	    'timepoint_col':Str,
	    'treatment_col':Str
    },
	parameter_descriptions = {
	    'method':'global optimization method',
	    'metadata':'Sample metadata',
	    'individual_col':'individual column identifier',
	    'timepoint_col':'timepoint column identifier',
	    'treatment_col':'treatment column identifier'
    },
    name='Fit OU Models to PCoA Ordination output',
    description='This visualizer generates 3D animations of PCoA Timeseries.'
)