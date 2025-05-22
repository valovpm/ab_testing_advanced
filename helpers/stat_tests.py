
import scipy as sp
import statsmodels.api as sm
import warnings
from statsmodels.stats import descriptivestats as ds


# used in:
# bartlett_test (equality of variances)
# ind t-test (compare independent group means)
# welch t-test (compare independent group means)
def normality_test(sample, name, alpha):

    print(f'NORMALITY TESTING: {name}')
    print(f'SHAPIRO-WILK TEST')
    if len(sample) > 5000:
        print(f'warning: sample size is greater than 5000, unreliable results')
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=UserWarning)
        stat, p_value = sp.stats.shapiro(sample)
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("sample looks Gaussian (fail to reject H0)")
    else:
        print("sample does not look Gaussian (reject H0)")

    print(f'D’AGOSTINO AND PEARSON’S TEST')
    stat, p_value = sp.stats.normaltest(sample)
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("sample looks Gaussian (fail to reject H0)")
    else:
        print("sample does not look Gaussian (reject H0)")

    print(f'KOLMOGOROV-SMIRNOV')
    d_statistic, p_value = sp.stats.kstest(
        sample, 'norm', args=(sample.mean(), sample.std()))
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("sample looks Gaussian (fail to reject H0)")
    else:
        print("sample does not look Gaussian (reject H0)")
    print()


def bartlett_test(a_sample, b_sample, a_name, b_name, alpha):
    # checks if variances of two samples are equal
    # ASSUMES that data is normally distributed (use normality_test)
    print(f'BARTLETT: {a_name}, {b_name}')
    stat, p_value = sp.stats.bartlett(a_sample, b_sample)
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("variances are equal (fail to reject H0)")
    else:
        print("variances are significantly different (reject H0)")
    print()


def levenes_test(a_sample, b_sample, a_name, b_name, alpha):
    # checks if variances of two samples are equal
    # less sensitive to deviations from normality compared to Bartlett's
    # used in:
    # - mannwhitney_utest
    print(f'LEVENE`S: {a_name}, {b_name}')
    stat, p_value = sp.stats.levene(a_sample, b_sample)
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("variances are equal (fail to reject H0)")
    else:
        print("variances are significantly different (reject H0)")
    print()


def dagostino_skew_test(sample, name, alpha):
    # doesn't rely on other tests
    # used in:
    # - wilcoxon signed rank test (wilcoxon_test)
    print(f'DAGOSTINO_SKEW_TEST: {name}')
    # calculate and assess skewness
    skewness = sp.stats.skew(sample)
    print(f'skewness: {skewness}')
    if -0.5 <= skewness <= 0.5:
        print(f'skewness is relatively small')
    else:
        print(f'skewness is relatively small')
    stat, p_value = sp.stats.skewtest(sample)
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("skewness is not significantly different from zero (fail to reject H0)")
    else:
        print("skewness is significantly different from zero (reject H0)")
    print()


def pearson_kurtosis_test(sample, name, alpha):
    # doesn't rely on other tests
    print(f'PEARSON_KURTOSIS_TEST: {name}')
    stat, p_value = sp.stats.kurtosistest(sample)
    kurtosis = sp.stats.kurtosis(sample)
    print(f'kurtosis: {kurtosis}')
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("kurtosis is not significantly different from zero (fail to reject H0)")
    else:
        print("kurtosis is significantly different from zero (reject H0)")
    print()


def ttest_ind(a_sample, b_sample, name, alpha):
    # compares means of two independent samples to see if they differ significantly
    # ASSUMES normality of samples (use normality_test)
    # ASSUMES equal variances (use bartlett_test)
    print(f'TTEST_IND: {name}')
    stat, p_value = sp.stats.ttest_ind(a_sample, b_sample, equal_var=True, alternative='two-sided')
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("samples are equal (fail to reject H0)")
    else:
        print("samples are significantly different (reject H0)")
    print()

    return p_value


def mannwhitney_utest(a_sample, b_sample, name, alpha):
    # Alternative to the independent samples t-test (ttest_ind)
    # It compares the distributions of two independent groups
    #
    # ASSUMES that the two samples have similarly shaped distributions:
    # - variances can be compared using Levene`s test (levenes_test)
    # - 2-sample kolmogorov-smirnov test?
    # - bootstrap difference between skewness and kurtosis?
    #
    # doesn't assume:
    # - normality
    print(f'MANNWHITNEY_UTEST: {name}')
    stat, p_value = sp.stats.mannwhitneyu(a_sample, b_sample, alternative='two-sided')
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("samples are equal (fail to reject H0)")
    else:
        print("samples are significantly different (reject H0)")
    print()


def welch_ttest(a_sample, b_sample, name, alpha):
    # Welch’s t-test compares means between two independent groups
    # ASSUMES:
    # - normality of samples (normality_test)
    # Doesn't assume:
    # - equality of variances
    print(f'WELCH_TTEST: {name}')
    stat, p_value = sp.stats.ttest_ind(a_sample, b_sample, equal_var=False, alternative='two-sided')
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("samples are equal (fail to reject H0)")
    else:
        print("samples are significantly different (reject H0)")
    print()


def brunner_munzel_test(a_sample, b_sample, name, alpha):
    # compares means between two independent groups
    # acts as a non-parametric alternative to Welch’s t-test
    # Tests null hypothesis that randomly selected observation from one group
    # is equally likely to be larger than a randomly selected observation from the other group
    # Doesn't assume:
    # - equality of variances
    # - equality of distributional shapes
    print(f'BRUNNER_MUNZEL_TEST: {name}')
    stat, p_value = sp.stats.brunnermunzel(a_sample, b_sample, alternative='two-sided')
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("samples are equal (fail to reject H0)")
    else:
        print("samples are significantly different (reject H0)")
    print()


def ttest_rel(a_sample, b_sample, name, alpha):
    # paired t-test
    print(f'TTEST_REL: {name}')
    stat, p_value = sp.stats.ttest_rel(a_sample, b_sample, alternative='two-sided')
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("samples are equal (fail to reject H0)")
    else:
        print("samples are significantly different (reject H0)")
    print()


def wilcoxon_test(a_sample, b_sample, name, alpha):
    # Wilcoxon Signed-Rank Test
    # Instead of comparing means (like the paired t-test),
    # it evaluates whether the median differences between paired observations are significantly different from zero
    # Assume:
    # - differences are symmetrically distributed around the median (dagostino_skew_test)
    # Doesn't assume:
    # - normality
    print(f'WILCOXON SIGNED-RANK TEST: {name}')
    stat, p_value = sp.stats.wilcoxon(a_sample, b_sample, alternative='two-sided')
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("samples are equal (fail to reject H0)")
    else:
        print("samples are significantly different (reject H0)")
    print()


def sign_test(diffs, name, alpha):
    #
    print(f'SIGN_TEST: {name}')
    # stat, p_value = sm.stats.descriptivestats.sign_test(diff, mu0=0)
    stat, p_value = ds.sign_test(diffs, mu0=0)
    print(f'p-value: {p_value}')
    if p_value > alpha:
        print("not enough evidence to conclude a significant median difference between the paired observations (fail to reject H0)")
    else:
        print("significant difference in the median of the paired differences (reject H0)")
    print()


