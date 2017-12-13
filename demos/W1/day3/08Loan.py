'''
·输入的贷款金额、贷款年限、贷款利率
·求月供
·求还款总额
'''

amount = eval(input("骚年你想贷多少钱:"))
years = eval(input("您想贷多少年:"))
monthRate = eval(input("银行月化利息为："))

monthPay = (amount * monthRate)/(1-(1/(1+monthRate)**(years*12)))
totalPay = monthPay * years * 12

print("月供是",monthPay)
print("还款总额是",totalPay)