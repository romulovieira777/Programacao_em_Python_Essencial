value = float(input('Enter the value: '))
discount_10 = value - (value * 10/100)
installment_3 = value / 3
commission_vew = discount_10 * 0.05
commission_parceled = value * 0.05
print('Total payable with 10% discount R$ {:.2f}'.format(discount_10))
print('Amount of the installment per month R$ {:.2f} totaling R$ {:.2f}'.format(installment_3, value))
print('Commision amount for cash payment R$ {:.2f}'.format(commission_vew))
print('Commission amount for payment in installments R$ {:.2f}'.format(commission_parceled))
