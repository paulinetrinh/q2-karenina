# karenina
[![Build Status](https://travis-ci.org/zaneveld/karenina.svg?branch=master)](https://travis-ci.org/zaneveld/karenina)


Simulation and modeling tools for studying Anna Karenina effects in animal microbiomes 
This package aims to develop tools for modeling microbiome variability in disease.  Initial versions focus on simulating microbiome change 
over time using simple Ornstein-Uhlenbeck (OU) models.  

## Anna Karenina Effects
TODO: Explain AKE

## Bronian Motion
TODO: Explain Brownian Motion Models

## Ornstein Uhlenbeck
TODO: Explain Ornstein Uhlenbeck Models

## Usage & Installation
This package ports karenina into Qiime2, run the following commands to enable karenina and its functions within q2cli.

Install ffmpeg to accomodate for timeseries visualization generation.
```
sudo apt-get install ffmpeg -y
```

Then install both karenina, and q2-karenina
```
pip install git+https://github.com/slpeoples/karenina.git
pip install git+https://github.com/slpeoples/q2-karenina.git
```

Update the Qiime2 cache to enable the newly installed qiime2 plugin.
```
qiime dev refresh-cache
```

### qiime karenina --help
<details><summary>Expand</summary>
<p>
  
```
  Usage: qiime karenina [OPTIONS] COMMAND [ARGS]...
  
    Description: This script simulates microbiome change over time using
    Ornstein-Uhlenbeck (OU) models.  These are similar to Brownian motion
    models, with the exception that they include reversion to a mean. Output
    is a tab-delimited data table and figures.

    Plugin website: https://github.com/zaneveld/karenina

    Getting user support: Please post to the QIIME 2 forum for help with this
    plugin: https://forum.qiime2.org

  Options:
    --version    Show the version and exit.
    --citations  Show citations and exit.
    --help       Show this message and exit.

  Commands:
    fit-timeseries              Fit OU Models to PCoA Ordination output
    spatial-ornstein-uhlenbeck  Spatial Ornstein Uhlenbeck microbial community
                                simulation
    visualization               Generates 3D animations of PCoA Timeseries
  ```
  
</p>
</details>

_____

#### qiime karenina fit-timeseries --help
<details><summary>Expand</summary>
<p>
  
```
  Usage: qiime karenina fit-timeseries [OPTIONS]
  
    This visualizer generates OU model parameters for PCoA outputdata, for
    each individual and each defined treatment cohort.

  Options:
    --p-pcoa TEXT                   filepath to PCoA results  [required]
    --p-metadata TEXT               filepath to Sample metadata  [required]
    --p-method [basinhopping]       global optimization method  [required]
    --p-individual-col TEXT         individual column identifier  [required]
    --p-timepoint-col TEXT          timepoint column identifier  [required]
    --p-treatment-col TEXT          treatment column identifier  [required]
    --o-visualization VISUALIZATION PATH
                                    [required if not passing --output-dir]
    --output-dir DIRECTORY          Output unspecified results to a directory
    --cmd-config PATH               Use config file for command options
    --verbose                       Display verbose output to stdout and/or
                                    stderr during execution of this action.
                                    [default: False]
    --quiet                         Silence output if execution is successful
                                    (silence is golden).  [default: False]
    --citations                     Show citations and exit.
    --help                          Show this message and exit.
```
</p>
</details>

#### qiime karenina fit-timeseries example
<details><summary>Expand</summary>
<p>

Utilizing simulation data generated from running spatial-ornstein-uhlenbeck, the following files are used as the PCoA and Metadata files, respectively.

* https://github.com/SLPeoples/q2-karenina/blob/master/data/ordination.txt
    
* https://github.com/SLPeoples/q2-karenina/blob/master/data/metadata.tsv

We make sure that the files are saved in the appropriate place, in this instance, I have them saved to the qiime2 home directory, so we define the pcoa and metadata parameters to match these filepaths. These must be direct filepaths to PCoA and Metadata files, and not Qiime2 artifacts.
```
    --p-pcoa /home/qiime2/ordination.txt
    --p-metadata /home/qiime2/metadata.tsv
```

Currently the only supported optimization method is basinhopping, so we define our method as follows:
```
    --p-method basinhopping
```

Within the metadata file, we see that the column identifying individuals, timepoints, and treatment are:
```
        Subject, Timepoint, Treatment
```

We define the following parameters to match these column names.
```
    --p-individual-col Subject
    --p-timepoint-col Timepoint
    --p-treatment-col Treatment
```

We define our output directory as a new directory that is appropriate for the qiime2 action that is being completed.
```
    --output-dir /home/qiime2/simulation_ou_fit_ts/
```

Now that we've set up our parameters, we can run our qiime2 visualization.
```
    qiime karenina fit-timeseries --p-pcoa /home/qiime2/ordination.txt --p-metadata /home/qiime2/metadata.tsv --p-method basinhopping --p-individual-col Subject --p-timepoint-col Timepoint --p-treatment-col Treatment --output-dir /home/qiime2/simulation_ou_fit_ts/
```

If the visualization was successful, you should see the following console response:
```
    Saved Visualization to: /home/qiime2/simulation_ou_visualization/visualization.qzv
```

Within the visualization.qzv, we have two output data files which contain our modeled timeseries results. With input parameters being optimized to sigma/ delta: 0.25, lambda: 0.20, theta/ mu: 0.00, the fit_timeseries modeled individuals and cohorts, which can be found here:

* https://github.com/SLPeoples/q2-karenina/blob/master/data/simulation_ou_fit_ts/individual_fit_timeseries.csv

* https://github.com/SLPeoples/q2-karenina/blob/master/data/simulation_ou_fit_ts/cohort_fit_timeseries.csv

</p>
</details>

_____

#### qiime karenina spatial-ornstein-uhlenbeck --help
<details><summary>Expand</summary>
<p>

## UNDER CONSTRUCTION - PLEASE REFER TO karenina.spatial_ornstein_uhlenbeck
```
  Usage: qiime karenina spatial-ornstein-uhlenbeck [OPTIONS]

    This method simulates microbial behavior over time usingOrnstein Uhlenbeck
    models. This are similar to Brownian Motionwith the exception that they
    include reversion to a mean.

  Options:
    --p-perturbation-fp TEXT        filepath for perturbation parameters for
                                    simulation results  [required]
    --p-treatment-names TEXT        ['control,destabalizing_treatment'] Names
                                    for simulation treatments  [required]
    --p-n-individuals TEXT          ['35,35'] Number of individuals per
                                    treatment  [required]
    --p-n-timepoints INTEGER        ['10'] Number of simulation timepoints
                                    [required]
    --p-perturbation-timepoint INTEGER
                                    ['5'] Timepoint at which to apply treatment
                                    (<n_timepoints)  [required]
    --p-perturbation-duration INTEGER
                                    ['100'] Duration of perturbation.
                                    [required]
    --p-interindividual-variation FLOAT
                                    ['0.01']Starting variability between
                                    individuals  [required]
    --p-delta FLOAT                 ['0.25'] Starting Delta parameter for
                                    Brownian Motion/ OU models. Higher values
                                    indicate greater variability over time
                                    [required]
    --p-lam FLOAT                   ['0.20'] Starting Lambda value for OU
                                    process. Higher values indicate a greater
                                    tendancy to revert to the mean value.
                                    [required]
    --p-fixed-start-pos TEXT        Starting x,y,z position for each point. If
                                    not defined, starting positions will be
                                    randomized based on
                                    interindividual_variation; type: string, eg:
                                    ['0.0,0.1,0.2'].  [required]
    --o-ordination ARTIFACT PATH PCoAResults
                                    Sample PCoA file containing simulation data
                                    [required if not passing --output-dir]
    --o-distance-matrix ARTIFACT PATH DistanceMatrix
                                    Sample Distance Matrix containing simulation
                                    data  [required if not passing --output-dir]
    --output-dir DIRECTORY          Output unspecified results to a directory
    --cmd-config PATH               Use config file for command options
    --verbose                       Display verbose output to stdout and/or
                                    stderr during execution of this action.
                                    [default: False]
    --quiet                         Silence output if execution is successful
                                    (silence is golden).  [default: False]
    --citations                     Show citations and exit.
    --help                          Show this message and exit.
```
</p>
</details>

#### qiime karenina visualization --help
<details><summary>Expand</summary>
<p>

## UNDER CONSTRUCTION - PLEASE REFER TO karenina.visualization
```
  Usage: qiime karenina visualization [OPTIONS]

    This visualizer generates 3D animations of PCoA Timeseries.

  Options:
    --p-pcoa TEXT                   filepath to PCoA results  [required]
    --p-metadata TEXT               filepath to Sample metadata  [required]
    --p-individual-col TEXT         individual column identifier  [required]
    --p-timepoint-col TEXT          timepoint column identifier  [required]
    --p-treatment-col TEXT          treatment column identifier  [required]
    --o-visualization VISUALIZATION PATH
                                    [required if not passing --output-dir]
    --output-dir DIRECTORY          Output unspecified results to a directory
    --cmd-config PATH               Use config file for command options
    --verbose                       Display verbose output to stdout and/or
                                    stderr during execution of this action.
                                    [default: False]
    --quiet                         Silence output if execution is successful
                                    (silence is golden).  [default: False]
    --citations                     Show citations and exit.
    --help                          Show this message and exit.
```

</p>
</details>
