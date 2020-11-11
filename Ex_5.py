cash_proceeds = int(input('Hello! Can i see your current main digits? Like proceeds...'))
cash_costs = int(input(' and costs of your Company? '))
if cash_proceeds > cash_costs:
    profit = cash_proceeds - cash_costs
    print('I have great news for you!')
    print(f'In this month you have nice profit {profit}!')
    print(f'Your profitability is {profit/cash_proceeds:.2f}')
    workers = int(input(f'I wonder! How many people are working in your company? '))
    print(f'Hmmm.. your profit per worker is {profit/workers:.2f}')
elif cash_proceeds == cash_costs:
    print('Not bad! Not good!')
    print('zero..')
elif cash_proceeds < cash_costs:
    print('Unfourtenately black line in life..')
    print("You have some loss. I'm sorry")
print('Good bye!!!')
