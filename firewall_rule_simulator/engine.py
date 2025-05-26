import json
from firewall_rule_simulator.rule import Rule

def load_rules(path: str):
    with open(path, 'r') as f:
        data = json.load(f)
        return [Rule(**r) for r in data]

def detect_conflicts(rules):
    seen = {}
    conflicts = []
    for rule in rules:
        key = (rule.protocol, rule.src_ip, rule.dest_ip, rule.port)
        if key in seen:
            if seen[key].action != rule.action:
                conflicts.append((seen[key], rule))
        else:
            seen[key] = rule
    return conflicts

def simulate_packet(packet: dict, rules: list):
    for rule in rules:
        if rule.matches(packet):
            return rule.action
    return "deny"  # default policy
