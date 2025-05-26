# Firewall Rule Simulator

A CLI tool to simulate and validate firewall rules and detect conflicts.

## Features

- JSON-based rule input
- Conflict detection between overlapping rules
- Packet simulation engine
- CLI-based interface

## Usage

### 1. Run conflict check:

```
python main.py --rules rules.json --check-conflicts
```


### 2. Simulate a packet:

```
python main.py --rules rules.json --simulate packet.json
```

### 3. Run tests:

```
pytest tests/
```
