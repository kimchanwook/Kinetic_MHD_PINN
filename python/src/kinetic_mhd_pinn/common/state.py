from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class CoupledState:
    """Shared cross-module state container.

    Physics modules exchange named, unit-documented products through this object.
    The baseline intentionally uses generic mappings; concrete typed arrays should be
    introduced only when the first numerical module is selected.
    """

    fields: dict[str, Any] = field(default_factory=dict)
    metadata: dict[str, Any] = field(default_factory=dict)
    history: list[dict[str, Any]] = field(default_factory=list)

    def require(self, *names: str) -> None:
        missing = [name for name in names if name not in self.fields]
        if missing:
            raise KeyError(f"Missing required state products: {missing}")

    def publish(self, module_id: str, **products: Any) -> None:
        self.fields.update(products)
        self.history.append({"module": module_id, "products": tuple(products)})
