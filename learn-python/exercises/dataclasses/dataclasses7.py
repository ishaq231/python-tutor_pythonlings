# Exercise: Dataclasses 7
# I AM NOT DONE
#
# A FROZEN dataclass can't be changed after it's created: trying to change a
# field raises an error. This is useful for settings you don't want changed by
# accident. Put `frozen=True` in the brackets of the decorator:
#
#     @dataclass(frozen=True)
#
# Fix `Config` so changing `cfg.port` raises an error. The `try`/`except` at
# the bottom checks that for you.

from dataclasses import dataclass


@dataclass  # Bug: missing frozen=True
class Config:
    host: str
    port: int


cfg = Config("localhost", 8080)

try:
    cfg.port = 9090  # should raise because the dataclass is frozen
    mutation_raised = False
except Exception:
    mutation_raised = True
