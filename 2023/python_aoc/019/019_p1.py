from itertools import combinations


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        rules, parts = file.read().split('\n\n')
    return rules, parts


def p1(data):
    unparsed_rules, unparsed_parts = data
    rules = {}
    parts = []
    accepted_parts = []
    for rule in unparsed_rules.split('\n'):
        name, rule = rule.strip('}').split('{')
        rule = rule.split(',')
        rule = [tuple(r.split(':')) for r in rule]
        rules[name] = rule
    for part in unparsed_parts.split('\n'):
        if part == '':
            continue
        part = part.strip('{}').split(',')
        try:
            part = {p.split('=')[0]: int(p.split('=')[1]) for p in part}
        except:
            print(part)
            raise BlockingIOError
        parts.append(part)
    for part in parts:
        print(part)
        current_workflow = rules['in']
        ended = False
        while not ended:
            print(current_workflow)
            for rule in current_workflow:
                if any((c:=char) in "<>" for char in rule[0]):
                    l = rule[0][0]
                    num = int(rule[0][2:])
                    if c == '<':
                        if part[l] < num:
                            rule = rule[1]
                        else:
                            continue
                    else:
                        if part[l] > num:
                            rule = rule[1]
                        else:
                            continue
                else:
                    print("wowee")
                    rule = rule[0]
                if rule in ('A', 'R'):
                    print("we got A R")
                    if rule == 'A':
                        accepted_parts.append(part)
                    ended = True
                    break
                else:
                    current_workflow = rules[rule]
                    break
    total = 0
    for part in accepted_parts:
        total += sum(part.values())
    print(total)
    return total


test_data = parser("019_test.txt")
assert p1(test_data) == 19114
actual_data = parser()
print(p1(actual_data))