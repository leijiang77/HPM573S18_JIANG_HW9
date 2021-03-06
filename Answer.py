
import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs
import scr.FormatFunctions as F
import InputData as Settings
import ParameterClasses as P
import scr.StatisticalClasses as str
#Problem3
print('Problem3')

# create a cohort
cohort = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.MONO)

# simulate the cohort
simOutputs = cohort.simulate()

print("  Estimate of mean survival time and confidence interval:",F.format_estimate_interval(
        estimate=simOutputs.get_sumStat_survival_times().get_mean(),
        interval=simOutputs.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)
)

#Problem4
print('Problem4')

print(P.calculate_prob_matrix_combo(Settings.TRANS_MATRIX, Settings.TREATMENT_RR,Settings.DEATH_RR))




#Problem5
print("Problem5")
cohort2 = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.ANTI.value)
simOutputs2 = cohort2.simulate()

print("  Estimate of mean survival time and confidence interval:",F.format_estimate_interval(
        estimate=simOutputs2.get_sumStat_survival_times().get_mean(),
        interval=simOutputs2.get_sumStat_survival_times().get_t_CI(alpha=Settings.ALPHA),
        deci=2)
)

#Problem6
print("Problem6")
# graph survival curve
PathCls.graph_sample_path(
    sample_path=simOutputs.get_survival_curve(),
    title='Survival curve-No anticoagulation',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )

PathCls.graph_sample_path(
    sample_path=simOutputs2.get_survival_curve(),
    title='Survival curve-anticoagulation',
    x_label='Simulation time step',
    y_label='Number of alive patients'
    )


#Problem7
print("Problem7")

print("Estimate of mean storke times of not using anticoagulation:",simOutputs.get_stroke_range().get_mean())
print("Estimate of mean storke times of not using anticoagulation:",simOutputs2.get_stroke_range().get_mean())
Figs.graph_histogram(
    data=simOutputs.get_stroke_total(),
    title='Stroke Number of No ANTI',
    x_label='Number of Strokes',
    y_label='Counts',
    bin_width=1
)

Figs.graph_histogram(
    data=simOutputs2.get_stroke_total(),
    title='Stroke Number of WITH ANTI',
    x_label='Number of Strokes',
    y_label='Counts',
    bin_width=1
)

