import argparse
import json
from firewall_rule_simulator.engine import load_rules, detect_conflicts, simulate_packet

def main():
    parser = argparse.ArgumentParser(description="Firewall Rule Simulator")
    parser.add_argument('--rules', type=str, required=True, help='Path to rules.json')
    parser.add_argument('--simulate', type=str, help='Path to packet.json for simulation')
    parser.add_argument('--check-conflicts', action='store_true', help='Detect conflicting rules')

    args = parser.parse_args()
    rules = load_rules(args.rules)

    if args.check_conflicts:
        conflicts = detect_conflicts(rules)
        if not conflicts:
            print("No conflicts detected.")
        else:
            print("Conflicting Rules:")
            for r1, r2 in conflicts:
                print(f"  - {r1} <-> {r2}")

    if args.simulate:
        with open(args.simulate, 'r') as f:
            packet = json.load(f)
        action = simulate_packet(packet, rules)
        print(f"Packet {packet} -> Action: {action.upper()}")

if __name__ == "__main__":
    main()
