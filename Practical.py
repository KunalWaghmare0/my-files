'''# PR6, Q1. mean of one sample using z test.
import numpy as np
from scipy.stats import norm

data = list(map(float, input("Enter sample values separated by spaces(e.g 990 920 931 945...: ").split()))
mu0 = float(input("Enter claimed population mean (H0)(eg.1000): "))
sigma = float(input("Enter known population standard deviation(eg, 8): "))
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test - left / right / two: ").strip().lower()






















n = len(data)
x_bar = np.mean(data)
z_cal = (x_bar - mu0) / (sigma / np.sqrt(n))

if tail == "left":
    print("\nH0: mu = %g   H1: mu < %g" % (mu0, mu0))
    z_crit = norm.ppf(alpha)
    p_value = norm.cdf(z_cal)
    reject = z_cal < z_crit
elif tail == "right":
    print("\nH0: mu = %g   H1: mu > %g" % (mu0, mu0))
    z_crit = norm.ppf(1 - alpha)
    p_value = 1 - norm.cdf(z_cal)
    reject = z_cal > z_crit
else:
    print("\nH0: mu = %g   H1: mu != %g" % (mu0, mu0))
    z_crit = norm.ppf(1 - alpha / 2)
    p_value = 2 * (1 - norm.cdf(abs(z_cal)))
    reject = abs(z_cal) > z_crit

print(f"n = {n}, sample mean = {x_bar:.2f}")
print(f"z calculated = {z_cal:.4f}")
print(f"z critical   = {z_crit:.4f}" if tail != "two" else f"z critical   = +/-{z_crit:.4f}")
print(f"p-value      = {p_value:.3e}")
print("Decision: Reject H0" if reject else "Decision: Fail to reject H0")
'''
#Universal cmd command: python -m pip install numpy scipy pandas statsmodels
#c: pip install numpy scipy
#only numpy and scipy are third-party, so you can check the install with python -c "import numpy, scipy; print('ok')".












'''# PR6, Q2. mean of one sample using t-test
import numpy as np
from scipy.stats import t

data = list(map(float, input("Enter sample values separated by spaces: ").split()))
mu0 = float(input("Enter claimed population mean (H0): "))
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test - left / right / two: ").strip().lower()

n = len(data)
x_bar = np.mean(data)
s = np.std(data, ddof=1)         
df = n - 1
t_cal = (x_bar - mu0) / (s / np.sqrt(n))

if tail == "left":
    print("\nH0: mu = %g   H1: mu < %g" % (mu0, mu0))
    t_crit = t.ppf(alpha, df)
    p_value = t.cdf(t_cal, df)
    reject = t_cal < t_crit
elif tail == "right":
    print("\nH0: mu = %g   H1: mu > %g" % (mu0, mu0))
    t_crit = t.ppf(1 - alpha, df)
    p_value = 1 - t.cdf(t_cal, df)
    reject = t_cal > t_crit
else:
    print("\nH0: mu = %g   H1: mu != %g" % (mu0, mu0))
    t_crit = t.ppf(1 - alpha / 2, df)
    p_value = 2 * (1 - t.cdf(abs(t_cal), df))
    reject = abs(t_cal) > t_crit

print(f"n = {n}, df = {df}")
print(f"sample mean = {x_bar:.2f}, sample SD = {s:.4f}")
print(f"t calculated = {t_cal:.4f}")
print(f"t critical   = {t_crit:.4f}" if tail != "two" else f"t critical   = +/-{t_crit:.4f}")
print(f"p-value      = {p_value:.4f}")
print("Decision: Reject H0" if reject else "Decision: Fail to reject H0")
'''










'''# Q3.  two samples using z-test
import numpy as np
from scipy.stats import norm

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

n1 = int(input("Enter size of sample 1: "))
n2 = int(input("Enter size of sample 2: "))
sigma1 = float(input("Enter known population SD of sample 1 (sigma1): "))
sigma2 = float(input("Enter known population SD of sample 2 (sigma2): "))
x1 = np.array(read_list("Sample 1", n1))
x2 = np.array(read_list("Sample 2", n2))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test on mean1 - mean2 - left / right / two: ").strip().lower()

m1, m2 = np.mean(x1), np.mean(x2)
se = np.sqrt(sigma1 ** 2 / n1 + sigma2 ** 2 / n2)     
z_cal = (m1 - m2) / se

if tail == "left":
    print("\nH0: mu1 = mu2   H1: mu1 < mu2")
    z_crit = norm.ppf(alpha)
    p_value = norm.cdf(z_cal)
    reject = z_cal < z_crit
elif tail == "right":
    print("\nH0: mu1 = mu2   H1: mu1 > mu2")
    z_crit = norm.ppf(1 - alpha)
    p_value = 1 - norm.cdf(z_cal)
    reject = z_cal > z_crit
else:
    print("\nH0: mu1 = mu2   H1: mu1 != mu2")
    z_crit = norm.ppf(1 - alpha / 2)
    p_value = 2 * (1 - norm.cdf(abs(z_cal)))
    reject = abs(z_cal) > z_crit

print(f"n1 = {n1}, n2 = {n2}")
print(f"mean1 = {m1:.4f}, mean2 = {m2:.4f}")
print(f"standard error = {se:.4f}")
print(f"z calculated = {z_cal:.4f}")
print(f"z critical   = {z_crit:.4f}" if tail != "two" else f"z critical   = +/-{z_crit:.4f}")
print(f"p-value      = {p_value:.4f}")
print("Decision: Reject H0" if reject else "Decision: Fail to reject H0")
'''












'''#Q4. two samples using t-test (independent)
import numpy as np
from scipy.stats import t

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

n1 = int(input("Enter size of sample 1: "))
n2 = int(input("Enter size of sample 2: "))
x1 = np.array(read_list("Sample 1", n1))
x2 = np.array(read_list("Sample 2", n2))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test on mean1 - mean2 - left / right / two: ").strip().lower()

m1, m2 = np.mean(x1), np.mean(x2)
ss1 = np.sum((x1 - m1) ** 2)
ss2 = np.sum((x2 - m2) ** 2)
df = n1 + n2 - 2
sp = np.sqrt((ss1 + ss2) / df)                 
t_cal = (m1 - m2) / (sp * np.sqrt(1 / n1 + 1 / n2))

if tail == "left":
    print("\nH0: mu1 = mu2   H1: mu1 < mu2")
    t_crit = t.ppf(alpha, df)
    p_value = t.cdf(t_cal, df)
    reject = t_cal < t_crit
elif tail == "right":
    print("\nH0: mu1 = mu2   H1: mu1 > mu2")
    t_crit = t.ppf(1 - alpha, df)
    p_value = 1 - t.cdf(t_cal, df)
    reject = t_cal > t_crit
else:
    print("\nH0: mu1 = mu2   H1: mu1 != mu2")
    t_crit = t.ppf(1 - alpha / 2, df)
    p_value = 2 * (1 - t.cdf(abs(t_cal), df))
    reject = abs(t_cal) > t_crit

print(f"n1 = {n1}, n2 = {n2}, df = {df}")
print(f"mean1 = {m1:.4f}, mean2 = {m2:.4f}")
print(f"pooled SD = {sp:.4f}")
print(f"t calculated = {t_cal:.4f}")
print(f"t critical   = {t_crit:.4f}" if tail != "two" else f"t critical   = +/-{t_crit:.4f}")
print(f"p-value      = {p_value:.4f}")
print("Decision: Reject H0" if reject else "Decision: Fail to reject H0")
'''











'''
# Q5. two sample using z-test(dependent)
import numpy as np
from scipy.stats import t

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

n_input = int(input("Enter number of pairs: "))
before = np.array(read_list("Sample 1 (Before)", n_input))
after = np.array(read_list("Sample 2 (After)", n_input))
print()
alpha = float(input("Enter level of significance (e.g. 0.10): "))
tail = input("Type of test on d = After - Before - left / right / two: ").strip().lower()

d = after - before                
n = len(d)
d_bar = np.mean(d)
s_d = np.std(d, ddof=1)      
df = n - 1
t_cal = d_bar / (s_d / np.sqrt(n))

if tail == "left":
    print("\nH0: mu_d = 0   H1: mu_d < 0")
    t_crit = t.ppf(alpha, df)
    p_value = t.cdf(t_cal, df)
    reject = t_cal < t_crit
elif tail == "right":
    print("\nH0: mu_d = 0   H1: mu_d > 0")
    t_crit = t.ppf(1 - alpha, df)
    p_value = 1 - t.cdf(t_cal, df)
    reject = t_cal > t_crit
else:
    print("\nH0: mu_d = 0   H1: mu_d != 0")
    t_crit = t.ppf(1 - alpha / 2, df)
    p_value = 2 * (1 - t.cdf(abs(t_cal), df))
    reject = abs(t_cal) > t_crit

print("d = After - Before =", d)
print(f"n = {n}, df = {df}")
print(f"mean of d = {d_bar:.2f}, SD of d = {s_d:.4f}")
print(f"t calculated = {t_cal:.4f}")
print(f"t critical   = {t_crit:.4f}" if tail != "two" else f"t critical   = +/-{t_crit:.4f}")
print(f"p-value      = {p_value:.4f}")
print("Decision: Reject H0" if reject else "Decision: Fail to reject H0")
'''












'''
#PR 7, Q1.testing for hypothesis for variance of one sample
import numpy as np
from scipy.stats import chi2

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

n = int(input("Enter size of sample: "))
x = np.array(read_list("Sample", n))
print()
var0 = float(input("Enter hypothesised population variance (H0): "))
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test - left / right / two: ").strip().lower()

x_bar = np.mean(x)
ss = np.sum((x - x_bar) ** 2)          
s2 = ss / (n - 1)                     
df = n - 1
chi_cal = ss / var0                    

if tail == "left":
    print("\nH0: sigma^2 = %g   H1: sigma^2 < %g" % (var0, var0))
    crit = chi2.ppf(alpha, df)
    p_value = chi2.cdf(chi_cal, df)
    reject = chi_cal < crit
    crit_txt = f"{crit:.4f}"
elif tail == "right":
    print("\nH0: sigma^2 = %g   H1: sigma^2 > %g" % (var0, var0))
    crit = chi2.ppf(1 - alpha, df)
    p_value = 1 - chi2.cdf(chi_cal, df)
    reject = chi_cal > crit
    crit_txt = f"{crit:.4f}"
else:
    print("\nH0: sigma^2 = %g   H1: sigma^2 != %g" % (var0, var0))
    lo = chi2.ppf(alpha / 2, df)
    hi = chi2.ppf(1 - alpha / 2, df)
    p_value = 2 * min(chi2.cdf(chi_cal, df), 1 - chi2.cdf(chi_cal, df))
    reject = chi_cal < lo or chi_cal > hi
    crit_txt = f"{lo:.4f} and {hi:.4f}"

print(f"n = {n}, df = {df}")
print(f"sample mean = {x_bar:.4f}, sum of squares = {ss:.4f}")
print(f"sample variance s^2 = {s2:.4f}")
print(f"chi-square calculated = {chi_cal:.4f}")
print(f"chi-square critical   = {crit_txt}")
print(f"p-value               = {p_value:.4f}")
print("Decision: Reject H0" if reject else "Decision: Fail to reject H0")
'''










'''
#Q2. testing of hypothesis for variance of two sample
import numpy as np
from scipy.stats import f

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

n1 = int(input("Enter size of sample 1: "))
n2 = int(input("Enter size of sample 2: "))
x1 = np.array(read_list("Sample 1", n1))
x2 = np.array(read_list("Sample 2", n2))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test on sigma1^2 vs sigma2^2 - left / right / two: ").strip().lower()

s1 = np.var(x1, ddof=1)               
s2 = np.var(x2, ddof=1)               
df1, df2 = n1 - 1, n2 - 1
F_cal = s1 / s2

if tail == "left":
    print("\nH0: sigma1^2 = sigma2^2   H1: sigma1^2 < sigma2^2")
    crit = f.ppf(alpha, df1, df2)
    p_value = f.cdf(F_cal, df1, df2)
    reject = F_cal < crit
    crit_txt = f"{crit:.4f}"
elif tail == "right":
    print("\nH0: sigma1^2 = sigma2^2   H1: sigma1^2 > sigma2^2")
    crit = f.ppf(1 - alpha, df1, df2)
    p_value = 1 - f.cdf(F_cal, df1, df2)
    reject = F_cal > crit
    crit_txt = f"{crit:.4f}"
else:
    print("\nH0: sigma1^2 = sigma2^2   H1: sigma1^2 != sigma2^2")
    lo = f.ppf(alpha / 2, df1, df2)
    hi = f.ppf(1 - alpha / 2, df1, df2)
    p_value = 2 * min(f.cdf(F_cal, df1, df2), 1 - f.cdf(F_cal, df1, df2))
    reject = F_cal < lo or F_cal > hi
    crit_txt = f"{lo:.4f} and {hi:.4f}"

print(f"n1 = {n1}, n2 = {n2}, df = ({df1}, {df2})")
print(f"s1^2 = {s1:.4f}, s2^2 = {s2:.4f}")
print(f"F calculated = {F_cal:.4f}")
print(f"F critical   = {crit_txt}")
print(f"p-value      = {p_value:.4f}")
print("Decision: Reject H0" if reject else "Decision: Fail to reject H0")
'''












'''#PR 8, Q1. One Way ANOVA
import numpy as np
from scipy.stats import f

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

k = int(input("Enter number of groups: "))
groups = []
for i in range(k):
    n_i = int(input(f"Enter size of group {i + 1}: "))
    groups.append(np.array(read_list(f"Group {i + 1}", n_i)))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))

N = sum(len(g) for g in groups)
grand_mean = np.concatenate(groups).mean()

SSB = sum(len(g) * (g.mean() - grand_mean) ** 2 for g in groups)   
SSW = sum(np.sum((g - g.mean()) ** 2) for g in groups)             
SST = SSB + SSW

df_b, df_w = k - 1, N - k
MSB = SSB / df_b
MSW = SSW / df_w
F_cal = MSB / MSW

F_crit = f.ppf(1 - alpha, df_b, df_w)
p_value = 1 - f.cdf(F_cal, df_b, df_w)

print("\nH0: all group means are equal   H1: at least one mean is different")
print("\nGroup means:", [round(float(g.mean()), 4) for g in groups])
print(f"Grand mean = {grand_mean:.4f}, N = {N}")
print("\nANOVA table")
print(f"{'Source':<10}{'SS':>12}{'df':>6}{'MS':>12}{'F':>10}")
print(f"{'Between':<10}{SSB:>12.4f}{df_b:>6}{MSB:>12.4f}{F_cal:>10.4f}")
print(f"{'Within':<10}{SSW:>12.4f}{df_w:>6}{MSW:>12.4f}")
print(f"{'Total':<10}{SST:>12.4f}{N - 1:>6}")
print(f"\nF critical = {F_crit:.4f}")
print(f"p-value    = {p_value:.6f}")
print("Decision: Reject H0" if F_cal > F_crit else "Decision: Fail to reject H0")
'''

















'''# Q2. Two- way ANOVA(WOR).
import numpy as np
from scipy.stats import f

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
row_names = []
data = []
for i in range(r):
    row_names.append(input(f"\nEnter name of row {i + 1}: "))
    row = []
    for j in range(c):
        row.append(float(input(f"Enter element for column {j + 1}: ")))
    data.append(row)
data = np.array(data)
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))

N = r * c
T = data.sum()
CF = T ** 2 / N                                 

SST = np.sum(data ** 2) - CF                  
SSR = np.sum(data.sum(axis=1) ** 2) / c - CF      
SSC = np.sum(data.sum(axis=0) ** 2) / r - CF      
SSE = SST - SSR - SSC                      

df_r, df_c, df_e = r - 1, c - 1, (r - 1) * (c - 1)
MSR, MSC, MSE = SSR / df_r, SSC / df_c, SSE / df_e
F_r, F_c = MSR / MSE, MSC / MSE

Fcrit_r = f.ppf(1 - alpha, df_r, df_e)
Fcrit_c = f.ppf(1 - alpha, df_c, df_e)
p_r = 1 - f.cdf(F_r, df_r, df_e)
p_c = 1 - f.cdf(F_c, df_c, df_e)

print("\nHypotheses")
print("Rows   : H0: all row means are equal    H1: at least one row mean is different")
print("Columns: H0: all column means are equal  H1: at least one column mean is different")
print(f"\nRow totals    = {data.sum(axis=1)}")
print(f"Column totals = {data.sum(axis=0)}")
print(f"Grand total = {T:.0f}, correction factor = {CF:.4f}")

print("\nANOVA table")
print(f"{'Source':<10}{'SS':>12}{'df':>5}{'MS':>12}{'F':>10}{'F crit':>10}{'p-value':>10}")
print(f"{'Rows':<10}{SSR:>12.4f}{df_r:>5}{MSR:>12.4f}{F_r:>10.4f}{Fcrit_r:>10.4f}{p_r:>10.4f}")
print(f"{'Columns':<10}{SSC:>12.4f}{df_c:>5}{MSC:>12.4f}{F_c:>10.4f}{Fcrit_c:>10.4f}{p_c:>10.4f}")
print(f"{'Error':<10}{SSE:>12.4f}{df_e:>5}{MSE:>12.4f}")
print(f"{'Total':<10}{SST:>12.4f}{N - 1:>5}")

print("\nDecision (rows)   :", "Reject H0" if F_r > Fcrit_r else "Fail to reject H0")
print("Decision (columns):", "Reject H0" if F_c > Fcrit_c else "Fail to reject H0")
'''














'''#Q3. Two-way ANOVA(WR).
import numpy as np
from scipy.stats import f

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
m = int(input("Enter number of observations in each cell (replications): "))

data = np.zeros((r, c, m))
for i in range(r):
    for j in range(c):
        print(f"\nRow {i + 1}, Column {j + 1}:")
        for k in range(m):
            data[i, j, k] = float(input("Enter element: "))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))

N = r * c * m
T = data.sum()
CF = T ** 2 / N                                       

row_tot = data.sum(axis=(1, 2))
col_tot = data.sum(axis=(0, 2))
cell_tot = data.sum(axis=2)

SST = np.sum(data ** 2) - CF                          
SSR = np.sum(row_tot ** 2) / (c * m) - CF       
SSC = np.sum(col_tot ** 2) / (r * m) - CF        
SS_cells = np.sum(cell_tot ** 2) / m - CF
SSI = SS_cells - SSR - SSC                          
SSE = SST - SS_cells                                 

df_r, df_c = r - 1, c - 1
df_i = df_r * df_c
df_e = r * c * (m - 1)

MSR, MSC, MSI, MSE = SSR / df_r, SSC / df_c, SSI / df_i, SSE / df_e

if MSE < 1e-12:
    print("Error mean square is 0, so F cannot be calculated. Please enter different data.")
    raise SystemExit

F_r, F_c, F_i = MSR / MSE, MSC / MSE, MSI / MSE
Fc_r = f.ppf(1 - alpha, df_r, df_e)
Fc_c = f.ppf(1 - alpha, df_c, df_e)
Fc_i = f.ppf(1 - alpha, df_i, df_e)
p_r = 1 - f.cdf(F_r, df_r, df_e)
p_c = 1 - f.cdf(F_c, df_c, df_e)
p_i = 1 - f.cdf(F_i, df_i, df_e)

print("\nHypotheses")
print("Rows        : H0: all row means are equal")
print("Columns     : H0: all column means are equal")
print("Interaction : H0: there is no interaction between rows and columns")
print(f"\nRow totals    = {row_tot}")
print(f"Column totals = {col_tot}")
print(f"Grand total = {T:.0f}, N = {N}, correction factor = {CF:.4f}")

print("\nANOVA table")
print(f"{'Source':<13}{'SS':>12}{'df':>5}{'MS':>12}{'F':>9}{'F crit':>9}{'p-value':>9}")
print(f"{'Rows':<13}{SSR:>12.4f}{df_r:>5}{MSR:>12.4f}{F_r:>9.4f}{Fc_r:>9.4f}{p_r:>9.4f}")
print(f"{'Columns':<13}{SSC:>12.4f}{df_c:>5}{MSC:>12.4f}{F_c:>9.4f}{Fc_c:>9.4f}{p_c:>9.4f}")
print(f"{'Interaction':<13}{SSI:>12.4f}{df_i:>5}{MSI:>12.4f}{F_i:>9.4f}{Fc_i:>9.4f}{p_i:>9.4f}")
print(f"{'Error':<13}{SSE:>12.4f}{df_e:>5}{MSE:>12.4f}")
print(f"{'Total':<13}{SST:>12.4f}{N - 1:>5}")

print("\nDecision (rows)       :", "Reject H0" if F_r > Fc_r else "Fail to reject H0")
print("Decision (columns)    :", "Reject H0" if F_c > Fc_c else "Fail to reject H0")
print("Decision (interaction):", "Reject H0" if F_i > Fc_i else "Fail to reject H0")
'''








'''
#PRr 9. Q1. testing of hypothesis using sign text
import numpy as np
from scipy.stats import binom

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

kind = input("Type of data - 1 = one sample (given median), 2 = paired samples: ").strip()
n_in = int(input("Enter number of observations (pairs): "))

if kind == "1":
    x = np.array(read_list("Sample", n_in))
    med0 = float(input("\nEnter hypothesised median (H0): "))
    d = x - med0                     
    label = "median"
else:
    s1 = np.array(read_list("Sample 1 (Before)", n_in))
    s2 = np.array(read_list("Sample 2 (After)", n_in))
    d = s2 - s1                       
    label = "median of differences (After - Before)"
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test - left / right / two: ").strip().lower()

n_plus = int(np.sum(d > 0))
n_minus = int(np.sum(d < 0))
n_ties = int(np.sum(d == 0))
n = n_plus + n_minus                 

if tail == "left":
    print(f"\nH0: {label} = 0 (or the hypothesised value)   H1: {label} is less")
    p_value = binom.cdf(n_plus, n, 0.5)
    test_stat = n_plus
elif tail == "right":
    print(f"\nH0: {label} = 0 (or the hypothesised value)   H1: {label} is greater")
    p_value = 1 - binom.cdf(n_plus - 1, n, 0.5)
    test_stat = n_plus
else:
    print(f"\nH0: {label} = 0 (or the hypothesised value)   H1: {label} is different")
    test_stat = min(n_plus, n_minus)
    p_value = min(1.0, 2 * binom.cdf(test_stat, n, 0.5))

print("Signs:", "".join("+" if v > 0 else "-" if v < 0 else "0" for v in d))
print(f"Plus signs = {n_plus}, Minus signs = {n_minus}, Ties dropped = {n_ties}")
print(f"Effective n = {n}")
print(f"Test statistic = {test_stat}")
print(f"p-value = {p_value:.4f}")
print("Decision: Reject H0" if p_value < alpha else "Decision: Fail to reject H0")
'''











'''# Q2. Wilcoxon Signed Rank Test
import numpy as np
from scipy.stats import rankdata, norm

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

kind = input("Type of data - 1 = one sample (given median), 2 = paired samples: ").strip()
n_in = int(input("Enter number of observations (pairs): "))

if kind == "1":
    x = np.array(read_list("Sample", n_in))
    med0 = float(input("\nEnter hypothesised median (H0): "))
    d = x - med0                        
    label = "median"
else:
    s1 = np.array(read_list("Sample 1 (Before)", n_in))
    s2 = np.array(read_list("Sample 2 (After)", n_in))
    d = s2 - s1                          
    label = "median of differences (After - Before)"
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test - left / right / two: ").strip().lower()

n_zero = int(np.sum(d == 0))
d_nz = d[d != 0]                      
n = len(d_nz)
ranks = rankdata(np.abs(d_nz))          
R_plus = ranks[d_nz > 0].sum()
R_minus = ranks[d_nz < 0].sum()

if n <= 25:
    r2 = np.rint(ranks * 2).astype(int)  
    dist = np.zeros(r2.sum() + 1)
    dist[0] = 1
    for v in r2:
        new = dist.copy()
        new[v:] += dist[:len(dist) - v]
        dist = new
    dist /= 2 ** n
    obs = int(round(R_plus * 2))
    p_left = dist[:obs + 1].sum()       
    p_right = dist[obs:].sum()             
    method = "exact"
else:
    mean = n * (n + 1) / 4
    _, cnt = np.unique(np.abs(d_nz), return_counts=True)
    var = n * (n + 1) * (2 * n + 1) / 24 - np.sum(cnt ** 3 - cnt) / 48
    z = (R_plus - mean) / np.sqrt(var)
    p_left, p_right = norm.cdf(z), 1 - norm.cdf(z)
    method = "normal approximation"

if tail == "left":
    print(f"\nH0: {label} = 0 (or hypothesised value)   H1: {label} is less")
    p_value = p_left
    stat = R_plus
elif tail == "right":
    print(f"\nH0: {label} = 0 (or hypothesised value)   H1: {label} is greater")
    p_value = p_right
    stat = R_minus
else:
    print(f"\nH0: {label} = 0 (or hypothesised value)   H1: {label} is different")
    p_value = min(1.0, 2 * min(p_left, p_right))
    stat = min(R_plus, R_minus)

print("\nd (After - Before or obs - median):", d)
print(f"Zero differences dropped = {n_zero}, effective n = {n}")
print(f"R+ (sum of positive ranks) = {R_plus}")
print(f"R- (sum of negative ranks) = {R_minus}")
print(f"Check: R+ + R- = {R_plus + R_minus}, n(n+1)/2 = {n * (n + 1) / 2}")
print(f"Test statistic W = {stat}")
print(f"p-value ({method}) = {p_value:.4f}")
print("Decision: Reject H0" if p_value < alpha else "Decision: Fail to reject H0")
'''









'''Q3. Wilcoxon Signed Rank Test.
import numpy as np
from scipy.stats import rankdata, norm

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

n1 = int(input("Enter size of sample 1: "))
n2 = int(input("Enter size of sample 2: "))
x1 = np.array(read_list("Sample 1", n1))
x2 = np.array(read_list("Sample 2", n2))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))
tail = input("Type of test (sample 1 vs sample 2) - left / right / two: ").strip().lower()

N = n1 + n2
ranks = rankdata(np.concatenate([x1, x2]))
R1 = ranks[:n1].sum()
R2 = ranks[n1:].sum()

U1 = n1 * n2 + n1 * (n1 + 1) / 2 - R1
U2 = n1 * n2 - U1
U = min(U1, U2)

if N <= 40:
    # exact: distribution of R1 over all ways of choosing n1 of the N ranks
    r2 = np.rint(ranks * 2).astype(int)             
    S = r2.sum()
    dp = np.zeros((n1 + 1, S + 1))
    dp[0, 0] = 1
    for v in r2:
        for j in range(n1, 0, -1):
            dp[j, v:] += dp[j - 1, :S + 1 - v]
    dist = dp[n1] / dp[n1].sum()
    obs = int(round(R1 * 2))
    p_left = dist[:obs + 1].sum()                   
    p_right = dist[obs:].sum()                   
    method = "exact"
else:
    mean_R1 = n1 * (N + 1) / 2
    _, cnt = np.unique(np.concatenate([x1, x2]), return_counts=True)
    var = n1 * n2 / 12 * ((N + 1) - np.sum(cnt ** 3 - cnt) / (N * (N - 1)))
    z = (R1 - mean_R1) / np.sqrt(var)
    p_left = norm.cdf(z)                               
    p_right = 1 - norm.cdf(z)                         
    method = "normal approximation"

if tail == "left":
    print("\nH0: the two populations are identical   H1: sample 1 tends to be smaller")
    p_value = p_left
elif tail == "right":
    print("\nH0: the two populations are identical   H1: sample 1 tends to be larger")
    p_value = p_right
else:
    print("\nH0: the two populations are identical   H1: the populations differ")
    p_value = min(1.0, 2 * min(p_left, p_right))

print(f"\nn1 = {n1}, n2 = {n2}, N = {N}")
print(f"Rank sum of sample 1 (R1) = {R1}")
print(f"Rank sum of sample 2 (R2) = {R2}")
print(f"Check: R1 + R2 = {R1 + R2}, N(N+1)/2 = {N * (N + 1) / 2}")
print(f"U1 = {U1}, U2 = {U2}, U = min(U1, U2) = {U}")
print(f"p-value ({method}) = {p_value:.4f}")
print("Decision: Reject H0" if p_value < alpha else "Decision: Fail to reject H0")
'''









'''
#Pr 10, Q1. Kruskal wallis test 
import numpy as np
from scipy.stats import rankdata, chi2

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

k = int(input("Enter number of groups: "))
groups = []
for i in range(k):
    n_i = int(input(f"Enter size of group {i + 1}: "))
    groups.append(np.array(read_list(f"Group {i + 1}", n_i)))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))

sizes = [len(g) for g in groups]
N = sum(sizes)
all_ranks = rankdata(np.concatenate(groups))
rank_sums, start = [], 0
for n_i in sizes:
    rank_sums.append(all_ranks[start:start + n_i].sum())
    start += n_i

H = 12 / (N * (N + 1)) * sum(R ** 2 / n_i for R, n_i in zip(rank_sums, sizes)) - 3 * (N + 1)

_, counts = np.unique(np.concatenate(groups), return_counts=True)
C = 1 - np.sum(counts ** 3 - counts) / (N ** 3 - N)
H_corr = H / C

df = k - 1
crit = chi2.ppf(1 - alpha, df)
p_value = 1 - chi2.cdf(H_corr, df)

print("\nH0: the medians (distributions) of all groups are the same")
print("H1: at least one group has a different median")
print("\nGroup   n    Rank sum   Mean rank")
for i, (n_i, R) in enumerate(zip(sizes, rank_sums), start=1):
    print(f"{i:<7}{n_i:<5}{R:<11.1f}{R / n_i:.2f}")
print(f"\nN = {N}, df = {df}")
print(f"H (without tie correction) = {H:.4f}")
print(f"Tie correction factor      = {C:.4f}")
print(f"H (corrected for ties)     = {H_corr:.4f}")
print(f"Chi-square critical value  = {crit:.4f}")
print(f"p-value                    = {p_value:.4f}")
print("Decision: Reject H0" if H_corr > crit else "Decision: Fail to reject H0")
'''








'''
#Q2. Friedman Test
import numpy as np
from scipy.stats import rankdata, chi2

b = int(input("Enter number of subjects (blocks): "))
k = int(input("Enter number of treatments (columns): "))
names = [input(f"Enter name of treatment {j + 1}: ") for j in range(k)]

data = np.zeros((b, k))
for i in range(b):
    print(f"\nSubject {i + 1}:")
    for j in range(k):
        data[i, j] = float(input(f"Enter score for {names[j]}: "))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))

ranks = np.array([rankdata(row) for row in data])
R = ranks.sum(axis=0)                          

chi_r = 12 / (b * k * (k + 1)) * np.sum(R ** 2) - 3 * b * (k + 1)

tie_sum = 0
for row in data:
    _, counts = np.unique(row, return_counts=True)
    tie_sum += np.sum(counts ** 3 - counts)
C = 1 - tie_sum / (b * k * (k ** 2 - 1))
chi_corr = chi_r / C

df = k - 1
crit = chi2.ppf(1 - alpha, df)
p_value = 1 - chi2.cdf(chi_corr, df)

print("\nH0: the treatments have the same effect (same median score)")
print("H1: at least one treatment has a different effect")
print("\nRanks within each subject:")
print("Subject  " + "  ".join(f"{n:>6}" for n in names))
for i, row in enumerate(ranks, start=1):
    print(f"{i:<9}" + "  ".join(f"{v:>6.1f}" for v in row))
print("Rank sum " + "  ".join(f"{v:>6.1f}" for v in R))
print(f"\nb = {b}, k = {k}, df = {df}")
print(f"Friedman statistic (no tie correction) = {chi_r:.4f}")
print(f"Tie correction factor                  = {C:.4f}")
print(f"Friedman statistic (corrected)         = {chi_corr:.4f}")
print(f"Chi-square critical value              = {crit:.4f}")
print(f"p-value                                = {p_value:.4f}")
print("Decision: Reject H0" if chi_corr > crit else "Decision: Fail to reject H0")
'''









'''#Q3. Mood's Median Test
import numpy as np
from scipy.stats import chi2

def read_list(title, n):
    print(f"\n{title}:")
    values = []
    for _ in range(n):
        values.append(float(input("Enter element: ")))
    return values

k = int(input("Enter number of groups: "))
groups = []
for i in range(k):
    n_i = int(input(f"Enter size of group {i + 1}: "))
    groups.append(np.array(read_list(f"Group {i + 1}", n_i)))
print()
alpha = float(input("Enter level of significance (e.g. 0.05): "))

everything = np.concatenate(groups)
N = len(everything)
grand_median = np.median(everything)

above = np.array([np.sum(g > grand_median) for g in groups])   
below = np.array([np.sum(g <= grand_median) for g in groups])  
obs = np.vstack([above, below])
row_tot = obs.sum(axis=1, keepdims=True)
col_tot = obs.sum(axis=0, keepdims=True)
exp = row_tot * col_tot / N
chi_cal = np.sum((obs - exp) ** 2 / exp)
df = k - 1
crit = chi2.ppf(1 - alpha, df)
p_value = 1 - chi2.cdf(chi_cal, df)

print("\nH0: the medians of all groups are the same")
print("H1: at least one group has a different median")
print(f"\nGrand median of all {N} values = {grand_median}")
print("\nObserved frequencies")
print(f"{'':<14}" + "".join(f"{'Group ' + str(i + 1):>9}" for i in range(k)) + f"{'Total':>9}")
print(f"{'> median':<14}" + "".join(f"{v:>9}" for v in above) + f"{above.sum():>9}")
print(f"{'<= median':<14}" + "".join(f"{v:>9}" for v in below) + f"{below.sum():>9}")
print("\nExpected frequencies")
print(f"{'> median':<14}" + "".join(f"{v:>9.3f}" for v in exp[0]))
print(f"{'<= median':<14}" + "".join(f"{v:>9.3f}" for v in exp[1]))
if exp.min() < 5:
    print("\nNote: some expected frequencies are below 5, so treat the result with caution.")
print(f"\ndf = {df}")
print(f"Chi-square calculated = {chi_cal:.4f}")
print(f"Chi-square critical   = {crit:.4f}")
print(f"p-value               = {p_value:.4f}")
print("Decision: Reject H0" if chi_cal > crit else "Decision: Fail to reject H0")
'''
