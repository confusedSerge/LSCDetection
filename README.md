# LSCDetection fork for MC+PCR
Mostly a Fork from LSDetection with added functionality!

Also new additions for experiments.

## Ordner

`modules/utils_.py`
> Added MC+PCR, PCR without MC and Algo_n (not used).

`postprocessing/ppa.py`
> Python script for using MC+PCR

`postprocessing/ppa_wo_mc.py`
> Python script for using PCR without MC

`postprocessing/algo_n.py`
> Python script for using Algo_n (never tested) 

`scripts`
> Mostly unimportant. Just some scripts for quicker/automating testing

`eval`
> Different evaluation scripts used on results csv, that were generated from the resulting post-process algorithms. Example: Calculating Argmax and corresponding performance

`ploter`
> Different ploters to plot result.

`tests`
> Results from experiments. Each directory is labeled based on which experiments were performend and are self-explanatory.

`plots`
> Plots created by scripts from `ploter` using the results found in `tests`. Not all data was ploted.
