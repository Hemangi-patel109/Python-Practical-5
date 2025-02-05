# The following company details are given for analysis: customer acc no,customer name, purchased product no, product category, unit price.Marketing is interested in understanding customer purchase patterns. Find
# the answers of following questions:
#  How many customers have purchased bread?
#  How many customers have purchased butter?
#  How many customers have purchased bread and butter?
#  Who has purchased bread but not butter?
#  Which customers have purchased bread, butter and milk?
#  Print the name of the most valuable customers who have
# purchased all three items.

def analyzed_data(c_data):
    c_bread = set()
    c_butter = set()
    c_milk = set()
    c_purchase = {} 

    for record in c_data:
        c_acc_no = record['c_acc_no']
        c_name = record['c_name']
        p_category = record['p_category']

        if c_acc_no not in c_purchase:
            c_purchase[c_acc_no] = {'name': c_name, 'products': set(), 'total_spent': 0}

        c_purchase[c_acc_no]['products'].add(p_category)
        c_purchase[c_acc_no]['total_spent'] += record['unit_price']

        if p_category == 'bread':
            c_bread.add(c_acc_no)
        elif p_category == 'butter':
            c_butter.add(c_acc_no)
        elif p_category == 'milk':
            c_milk.add(c_acc_no)

    c_both = c_bread.intersection(c_butter)
    c_bread_only = [
        c_purchase[acc_no]['name'] for acc_no in c_bread - c_butter
    ]
    c_all = [
        c_purchase[acc_no]['name'] for acc_no in c_bread.intersection(c_butter).intersection(c_milk)
    ]

    most_valuable_customers = []
    max_spent = 0

    for acc_no, data in c_purchase.items():
        if 'bread' in data['products'] and 'butter' in data['products'] and 'milk' in data['products']:
            if data['total_spent'] > max_spent:
                max_spent = data['total_spent']
                most_valuable_customers = [data['name']]
            elif data['total_spent'] == max_spent:
                most_valuable_customers.append(data['name'])

    return {
        'c_bread': len(c_bread),
        'c_butter': len(c_butter),
        'c_both': len(c_both),
        'c_bread_only': c_bread_only,
        'c_all': c_all,
        'most_valuable_customers': most_valuable_customers,
    }

c_data = [
    {'c_acc_no': 1, 'c_name': 'Hemangi', 'p_no': 101, 'p_category': 'bread', 'unit_price': 2.50},
    {'c_acc_no': 1, 'c_name': 'Hemangi', 'p_no': 102, 'p_category': 'butter', 'unit_price': 5.00},
    {'c_acc_no': 1, 'c_name': 'Hemangi', 'p_no': 103, 'p_category': 'milk', 'unit_price': 3.00},
    {'c_acc_no': 2, 'c_name': 'Adrien', 'p_no': 101, 'p_category': 'bread', 'unit_price': 2.50},
    {'c_acc_no': 2, 'c_name': 'Adrien', 'p_no': 102, 'p_category': 'butter', 'unit_price': 5.00},
]

results = analyzed_data(c_data)
print(results)