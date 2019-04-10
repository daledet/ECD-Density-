import math

#Equivalent Circulating Density

n_dimsionless = 3.32 * math.log10(float(60)/float(36)) # !!! 64 and 36 are derived from either viscometer readings or by adding plastic viscocity and yeild point together.
k_dimensionless = 36 / (511 ** n_dimsionless)

annular_velocity_ft_min = (24.5 * 400) / ((8.5 ** 2) - (5 ** 2))
equation_1 = (2.4 / (8.5 - 5)) * (((2 * n_dimsionless + 1 ) / (3 * n_dimsionless))) #WTF?
exponent_2 = ((n_dimsionless) / (2 - n_dimsionless)) #WTF? Why can't I exponent these?
critical_annular_velocity_ft_min = (((3.878 * (10 ** 4) * k_dimensionless) / (12.5)) ** (1/(2 - n_dimsionless))) * equation_1 ** exponent_2

test = (((3.878 * (10 ** 4) * k_dimensionless) / (12.5)) ** (1/(2 - n_dimsionless)))
test_2 = (2.4 / (8.5 - 5)) * (((2 * n_dimsionless + 1 ) / (3 * n_dimsionless)))
test_3 = ((n_dimsionless) / (2 - n_dimsionless))
test_4 = test_2 ** test_3
