# Dependency Map (optional extension)

**Reference date:** 2026-11-27 · Kept separate from the WBS on purpose: the WBS says **what** exists, this map says
**what relies on what**. No dates, no durations.

```mermaid
flowchart LR
    E1["1.1.1 Interview plan + consent"] --> E2["1.1.2 Interview records"] --> E3["1.1.3 Creator findings"]
    L1["1.2.1 Licence + terms assessment"] --> L2["1.2.2 Recent-data sources"]
    L1 --> L3["1.2.3 Data basis decision"]
    L2 --> L3
    E3 --> Q3["1.3.3 Minimum acceptable performance"]
    Q3 --> Q2["1.3.2 Recency check"]
    L3 --> Q2
    Q1["1.3.1 Option comparison"] --> B1["1.4.1 Pattern sheet"] --> B2["1.4.2 Plain-language review"]
    B1 --> C1["1.5.1 Comprehension kit"]
    Q3 --> C1
    M1["1.8.1 Teammate consent"] --> C1
    C1 --> C2["1.5.2 Comprehension report"]
    E1 --> C2
    L3 --> R2["1.6.2 Ownership outline"]
    R1["1.6.1 Cost per visit"] --> G1["1.7.1 Updated matrix"]
    E3 --> G1
    Q2 --> G1
    C2 --> G1
    G1 --> G2{"1.7.2 Gate decision"}
    M1 --> G2
    G2 --> M4["1.8.4 Closure record"]
```

## What this shows

| Question | Answer |
|---|---|
| External dependencies | A legal reviewer (1.2.1), creators (1.1, 1.5), the two teammates (1.8.1), any recent-data provider (1.2.2) |
| Decision gates | 1.3.3 thresholds must be approved **before** 1.3.2 runs; 1.7.2 is the project's single exit gate |
| Can start at once, in parallel | 1.1.1 interview plan, 1.2.1 legal reading, 1.3.1 comparison (partly done), 1.6.1 cost measurement, 1.8.1 consent |
| Longest chain | 1.1.1 → 1.1.2 → 1.1.3 → 1.3.3 → 1.3.2 → 1.7.1 → 1.7.2 |
| Assumptions most likely to change the sequence | A01 (if no creator wants odds, 1.3.2 and 1.6 lose their purpose); U05 (if no lawful recent data exists, 1.3.2 ends early as "not possible"); A07 (a "no" removes the C mock from 1.5.1) |
