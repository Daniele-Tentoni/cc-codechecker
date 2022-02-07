"""Abstract class for yaml objects.
"""
# Standard Library
from typing import Any

# Codechecker
from cc_codechecker.context import Context


class Configurable:
  """Abstract class for yaml objects.
  """
  def __init__(self, **kwargs) -> None:
    """Create a new configurable yaml object.
    """
    self._locals = Context().options()

    # Check if verbose override is needed.
    verbose = kwargs.get('verbose', None)
    if verbose:
      self._locals.verbose = verbose

  def dump(self) -> dict[str, Any]:
    """Dump the configurable object to a dictionary.
    """
    result = {}
    for key, value in self.valued_items():
      result[key] = value

    return result

  def valued_items(self) -> list[tuple[str, Any]]:
    def _excluded(key, value) -> bool:
      return key and value

    items = self.__dict__.items()
    return [(k,v) for k, v in items if _excluded(k, v)]

  def __repr__(self) -> str:
    args: list[str] = []

    for key, value in self.valued_items():
      args.append(f'{key}={value}')

    args_string = ','.join(args)

    return f'{self.__class__.__name__}({args_string})'
