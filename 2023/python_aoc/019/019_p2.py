from itertools import combinations
from math import prod


def parser(file_name="input.txt"):
    with open(file_name, 'r') as file:
        rules, parts = file.read().split('\n\n')
    return rules, parts


def p1(data):
    unparsed_rules, unparsed_parts = data
    rules = {}


    for rule in unparsed_rules.split('\n'):
        name, rule = rule.strip('}').split('{')
        rule = rule.split(',')
        rule = [tuple(r.split(':')) for r in rule]
        rules[name] = rule
    max_size = 4000
    start_part = {
        'x': range(1, max_size + 1),
        'm': range(1, max_size + 1),
        'a': range(1, max_size + 1),
        's': range(1, max_size + 1),
    }
    parts = [start_part]
    accepted_parts = []
    for part in parts:

        # print(part, len(parts))

        current_workflow = rules['in']
        ended = False
        while not ended:
            # print(current_workflow)
            for rule in current_workflow:
                if any((c := char) in "<>" for char in rule[0]):
                    l = rule[0][0]
                    num = int(rule[0][2:])
                    values: range = part[l]
                    if c == '<':
                        if values.start >= num:
                            continue
                        if values.stop <= num:
                            pass
                        elif values.stop > num:
                            new_part = part.copy()
                            new_part[l] = range(num, values.stop)
                            if new_part[l]:
                                parts.append(new_part)
                            part[l] = range(values.start,  num)
                            if not part[l]:
                                ended = True
                                break
                        else:
                            raise BlockingIOError
                    else:
                        if (values.stop - 1) <= num:
                            continue
                        if values.start > num:
                            pass
                        else:
                            new_part = part.copy()
                            new_part[l] = range(values.start, num + 1)
                            if new_part[l]:
                                parts.append(new_part)
                            part[l] = range(num + 1,  values.stop)
                            if not part[l]:
                                ended = True
                                break
                    rule = rule[1]
                else:

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
    print("jo we got all accepted parts")
    print(accepted_parts)
    for part in accepted_parts:
        print(part)
        current = prod(len(r) for r in part.values())
        lengths = [len(r) for r in part.values()]
        print(lengths)
        print(current)
        total += current
    print(total)
    return total


test_data = parser("019_test.txt")
assert p1(test_data) == 167409079868000
actual_data = parser()
print(p1(actual_data))