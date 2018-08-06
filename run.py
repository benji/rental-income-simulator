# https://www.coachcarson.com/rental-property-cash-flow/

property_price = 400000

loan_years = 30
yearly_rate = 0.05
down_payment_ratio = 0.2

monthly_rent = 3000
expected_vacancy_ratio = .07
hoa = 400
property_tax_rate = 0.011723

# net operating income

gross_rental_income = monthly_rent*12
vacancy_loss_reserve = gross_rental_income * expected_vacancy_ratio
management_fee = hoa
property_tax = property_price * property_tax_rate
property_insurance = 700
maintenance_repairs = 100
utilities = 0
rental_license = 45

net_operating_income = gross_rental_income - vacancy_loss_reserve - \
    management_fee - property_tax - property_insurance - \
    maintenance_repairs-utilities-rental_license
print 'Net operating income: ${:,.2f}'.format(net_operating_income)

# cash flow from operations

capital_expense_reserve = 75*12

cash_flow_from_reserves = net_operating_income - capital_expense_reserve
print 'Cash flow from reserves: ${:,.2f}'.format(cash_flow_from_reserves)

# cash flow after financing

loan_amout = property_price*(1-down_payment_ratio)
loan_months = loan_years*12
monthly_rate = yearly_rate/12
a = (1+monthly_rate)**loan_months
monthly_mortgage = loan_amout*((monthly_rate*a)/(a-1))

cumul_year_interests = []
left_to_pay = loan_amout
for y in range(1, loan_years+1):
    year_interest = 0
    for m in range(1, 12+1):
        monthly_interest = left_to_pay*monthly_rate
        year_interest += monthly_interest
        left_to_pay -= monthly_mortgage-monthly_interest
    cumul_year_interests.append(year_interest)

print 'Mortage: ${:,.2f}/mo'.format(monthly_mortgage)

cash_flow_after_financing = cash_flow_from_reserves - monthly_mortgage*12
print 'Cash flow after financing: ${:,.2f}'.format(cash_flow_after_financing)

# taxable income

building_value = property_price/2.
depreciation_per_year = building_value/27.5
interests_expense = cumul_year_interests[0]

taxable_income = net_operating_income - interests_expense-depreciation_per_year
if taxable_income <= 0:
    print 'Negative income, no taxes.'
    final_cash_flow = cash_flow_after_financing
else:
    print 'Taxable income: ${:,.2f}'.format(taxable_income)

    tax_bracket = .33
    taxes = taxable_income*tax_bracket

    cash_flow_after_taxes = cash_flow_after_financing - taxes
    print 'Cash flow after taxes: ${:,.2f}'.format(cash_flow_after_taxes)
    final_cash_flow = cash_flow_after_taxes

print 'Final cash flow: ${:.2f} per year.'.format(final_cash_flow)
