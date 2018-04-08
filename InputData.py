
# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1       # years

# transition matrix
TRANS_MATRIX = [
    [0.75,  0.15, 0.0, 0.1],   # Well
    [0.0,0.0,1.0,0.0],#stroke
    [0.0,0.25,0.55,0.2],   # Post-stroke
     [0,0,0,1]  # death
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    2756.0,   # CD4_200to500
    5000.0,   # CD4_200

    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0.75,   # CD4_200to500
    0.50,   # CD4_200
    0.25    # AIDS
    ]

# annual drug costs
Zidovudine_COST = 2278.0
Lamivudine_COST = 2086.0

# treatment relative risk
TREATMENT_RR = 0.65
DEATH_RR = 1.05
