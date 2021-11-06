def solution(ings, menu, sell):
    answer = 0

    ings_dict = dict()
    for ing in ings:
        ing_name, ing_price = ing.split()
        ings_dict[ing_name] = int(ing_price)

    menu_dict = dict()
    for m in menu:
        name, ing, price = m.split()
        cost = 0
        for x in ing:
            cost += ings_dict[x]
        menu_dict[name] = int(price) - cost

    for s in sell:
        name, count = s.split()
        answer += (menu_dict[name] * int(count))

    return answer


print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"],
               ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))
print(solution(["a 10"], ["AA aaa 10"], ["AA 5"]))