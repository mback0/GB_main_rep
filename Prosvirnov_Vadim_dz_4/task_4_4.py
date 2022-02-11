from utils import currency_rates

print(currency_rates('BYN'))
print(currency_rates('x'))
print(currency_rates('UAH'))
print(currency_rates('Y'))

"""
Z:\#python.projects\git_python\lesson4>python task_4_4.py
29.3502
None
2.67511
None

# Сначала выполнил задание образом, представленным ниже. Перечитав условие понял, что сделал немного не то, но решил оставить :)

Z:\#python.projects\git_python\lesson4>python -c "from utils import currency_rates; print(currency_rates('BYN'))"
29.3502

Z:\#python.projects\git_python\lesson4>python -c "from utils import currency_rates; print(currency_rates('EUR'))"
85.3574

Z:\#python.projects\git_python\lesson4>python -c "from utils import currency_rates; print(currency_rates('noinfo'))"
None

Z:\#python.projects\git_python\lesson4>python -c "from utils import currency_rates; print(currency_rates('XYZ'))"
None

Z:\#python.projects\git_python\lesson4>python -c "from utils import currency_rates; print(currency_rates('UAH'))"
2.67511

Z:\#python.projects\git_python\lesson4>python -c "from utils import currency_rates; print(currency_rates('JPY'))"
0.646326

"""