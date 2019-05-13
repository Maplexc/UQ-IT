#
# program to calculate a person's tax
#
#use meaningful name for variables
#
deduction_clothes=input('enter deduction for clothes:')
deduction_clothes=int(deduction_clothes)
deduction_car=input('enter deduction for car:')
deduction_car=int(deduction_car)
deduction_dependents=input('enter deduction for dependents:')
deduction_dependents=int(deduction_dependents)

deductions=deduction_clothes+deduction_car+deduction_dependents
#deduction_clothes, deduction_car, deduction_dependents are called variables
#they can vary
#
gross_income=50000
tax_free_threshold=18000
tax_rate=0.25
#
taxable_income=gross_income-tax_free_threshold-deductions
tax_payable=taxable_income*tax_rate
#calculate tax payable
print('Taxable income=',taxable_income,', Tax payable:',tax_payable, sep='')
