from __future__ import annotations

import random
import typing as t
from pathlib import Path

import pandas as pd

tuples: t.Set[t.Tuple[int, int]] = set()

min_x = 1
max_x = 48

while len(tuples) < 50:
    tuples.add((random.randint(min_x, max_x), random.randint(min_x, max_x)))


df = pd.DataFrame(tuples, columns=["StartX", "StartY"])
df["MaxTripDistance"] = 5.0
df["AgentExploreRadius"] = 1.0


df.to_csv(
    Path("GridBlueprint/Resources/complex_agent.csv"),
    index=False,
    sep=";",
)

# print(df)
