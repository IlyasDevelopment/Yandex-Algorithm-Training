def f_bin_search(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        # print(f'm: {m}, l: {l}, r: {r}')
        if check(m, checkparams):
            r = m
        else:
            l = m
    return l


def check_monthly_perc(m_perc, y_perc):
    m_sum = 1 + m_perc / 100
    y_sum = 1 + y_perc / 100
    return m_sum ** 12 >= y_sum


def check_credit(m_pay, params):
    periods, credit_sum, m_perc = params
    for i in range(periods):
        perc_pay = credit_sum * (m_perc / 100)
        credit_sum -= m_pay - perc_pay
    return credit_sum <= 0


x = 12  # year percent
eps = 0.01
m = 10000000  # sum
n = 300  # months
m_perc = f_bin_search(0, x, eps, check_monthly_perc, x)
month_pay = f_bin_search(0, m, eps, check_credit, (n, m, m_perc))
print(m_perc, month_pay)
