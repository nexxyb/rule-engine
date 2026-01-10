RULE_REGISTRY = {}


def register_rule(rule_class):
    RULE_REGISTRY[rule_class.key] = rule_class
    return rule_class
