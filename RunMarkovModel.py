import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.FormatFunctions as F
import InputData as Settings
# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)

# simulate the cohort
simOutputs = cohort.simulate()

# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

# graph histogram of survival times
Figs.graph_histogram(
    data=simOutputs.get_survival_times(),
    title='Survival times of patients with HIV',
    x_label='Survival time (years)',
    y_label='Counts',
    bin_width=1
)

# print the outcomes of this simulated cohort
#SupportMarkov.print_outcomes(simOutputs)
print("  Estimate of mean survival time and {:.{prec}%} confidence interval:",F.format_estimate_interval(
        estimate=simOutputs.get_sumStat_survival_times().get_mean(),
        interval=simOutputs.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)
)

