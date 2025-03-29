def back_chain(goal, rules, facts):
    if goal in facts:
        return True
    for rule in rules:
        if rule[0] == goal:
            conditions_satisfied = all(back_chain(condition, rules, facts) for condition in rule[1])
            if conditions_satisfied:
                facts.add(goal)  # Use set instead of list
                return True
    return False  # Ensure function returns False if goal is not reached

if __name__ == "__main__":
    rules = [
        ("clean_room", ["pick_up_toys", "vacuum_floor"]),
        ("pick_up_toys", ["find_toys"]),
        ("find_toys", ["know_location_of_toys"]),
        ("know_location_of_toys", ["ask_parents"]),
        ("vacuum_floor", ["move_furniture"])
    ]
    
    initial_facts = {"move_furniture"}  # Use a set
    goal = "vacuum_floor"

    result = back_chain(goal, rules, initial_facts)
    
    print(f"Goal '{goal}' achieved:", result)
    print("Final facts:", initial_facts)
