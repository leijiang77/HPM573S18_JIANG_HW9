from enum import Enum
import numpy as np
import scipy.stats as stat
import math as math
import InputData as Data
import scr.MarkovClasses as MarkovCls
import scr.RandomVariantGenerators as Random
import scr.ProbDistParEst as Est


class HealthStats(Enum):
    """ health states of patients with HIV """
    Well = 0
    Stroke = 1
    PostStroke = 2
    Death = 3


class Therapies(Enum):
    """ mono vs. combination therapy """
    MONO = 0
    ANTI = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.Well

        # annual treatment cost
        if self._therapy == Therapies.MONO:
            self._annualTreatmentCost = Data.Zidovudine_COST
        else:
            self._annualTreatmentCost = Data.Zidovudine_COST + Data.Lamivudine_COST

        # transition probability matrix of the selected therapy
        self._prob_matrix = Data.TRANS_MATRIX
        # treatment relative risk
        self._treatmentRR = 0
        self._deathRR = 0
        # calculate transition probabilities between hiv states
        #self._prob_matrix = calculate_prob_matrix()

        # update the transition probability matrix if combination therapy is being used
        if self._therapy == Therapies.ANTI:
            # treatment relative risk
            self._treatmentRR = Data.TREATMENT_RR
            self._deathRR = Data.DEATH_RR
            # calculate transition probability matrix for the combination therapy
            self._prob_matrix = calculate_prob_matrix_combo(
                matrix_mono=self._prob_matrix, combo_rr=Data.TREATMENT_RR, death_rr=Data.DEATH_RR)

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]


def calculate_prob_matrix():
    """ :returns transition probability matrix for hiv states under mono therapy"""

    # create an empty matrix populated with zeroes
    prob_matrix = []
    for s in HealthStats:
        prob_matrix.append([0] * len(HealthStats))

    # for all health states
    for s in HealthStats:
        # if the current state is death
        if s == HealthStats.Death:
            # the probability of staying in this state is 1
            prob_matrix[s.value][s.value] = 1
        else:
            # calculate total counts of individuals
            sum_counts = sum(Data.TRANS_MATRIX[s.value])
            # calculate the transition probabilities out of this state
            for j in range(s.value, HealthStats.Death.value+1):
                prob_matrix[s.value][j] = Data.TRANS_MATRIX[s.value][j] / sum_counts

    return prob_matrix


def calculate_prob_matrix_combo(matrix_mono, combo_rr, death_rr):
    """

    :param matrix_mono:
    :param combo_rr:
    :param death_rr:
    :return:
    """
    matrix_combo = matrix_mono


    # populate the combo matrix
    # first non-diagonal elements
    for s in HealthStats:
        #if s==HealthStats.Well:
            #matrix_combo[s.value][1] = combo_rr*matrix_mono[s.value][1]
            #matrix_combo[s.value][3] = death_rr*matrix_mono[s.value][3]
            #matrix_combo[s.value][s.value] =1 - sum(matrix_combo[s.value][s.value + 1:])
        if s == HealthStats.PostStroke:
            matrix_combo[s.value][1] = combo_rr * matrix_mono[s.value][1]
            matrix_combo[s.value][3] = death_rr * matrix_mono[s.value][3]*combo_rr
            matrix_combo[s.value][s.value] = 1 - (matrix_combo[s.value][1]+matrix_combo[s.value][3])


    return matrix_combo
