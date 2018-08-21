# q2-karenina
[![Build Status](https://travis-ci.org/zaneveld/q2-karenina.svg?branch=master)](https://travis-ci.org/zaneveld/q2-karenina)


Simulation and modeling tools for studying Anna Karenina effects in animal microbiomes 
This package aims to develop tools for modeling microbiome variability in disease.  Initial versions focus on simulating microbiome change 
over time using simple Ornstein-Uhlenbeck (OU) models.  

* [karenina](https://github.com/zaneveld/karenina)
* [Qiime2](https://qiime2.org)
* [Documentation](https://zaneveld.github.io/karenina/html/index.html)

Useful links:

* [Anna Karenina Principle](https://en.wikipedia.org/wiki/Anna_Karenina_principle)
* [Brownian Motion](https://en.wikipedia.org/wiki/Brownian_motion)
* [Weiner Process](https://en.wikipedia.org/wiki/Wiener_process)
* [Ornstein Uhlenbeck Process](https://en.wikipedia.org/wiki/Ornstein%E2%80%93Uhlenbeck_process)


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

Within the visualization.qzv, we have two output data files which contain our modeled timeseries results. With input parameters being optimized to sigma/ delta: 0.25, lambda: 0.20, theta/ mu: 0.00 (from the OU simulation), the fit_timeseries modeled individuals and cohorts, which can be found here:

* https://github.com/SLPeoples/q2-karenina/blob/master/data/simulation_ou_fit_ts/individual_fit_timeseries.csv

* https://github.com/SLPeoples/q2-karenina/blob/master/data/simulation_ou_fit_ts/cohort_fit_timeseries.csv

</p>
</details>
