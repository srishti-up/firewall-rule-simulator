from typing import Dict

class Rule:
    def __init__(self, rule_id: str, action: str, protocol: str, src_ip: str, dest_ip: str, port: int):
        self.rule_id = rule_id
        self.action = action.lower()
        self.protocol = protocol.lower()
        self.src_ip = src_ip
        self.dest_ip = dest_ip
        self.port = port

    def matches(self, packet: Dict) -> bool:
        return (
            self.protocol == packet['protocol'].lower()
            and self.src_ip == packet['src_ip']
            and self.dest_ip == packet['dest_ip']
            and self.port == packet['port']
        )

    def __eq__(self, other):
        return (
            self.protocol == other.protocol and
            self.src_ip == other.src_ip and
            self.dest_ip == other.dest_ip and
            self.port == other.port
        )

    def __str__(self):
        return f"{self.rule_id}: {self.action.upper()} {self.protocol.upper()} {self.src_ip} -> {self.dest_ip}:{self.port}"
