"""Context definition."""
# Standard Library
import copy
from argparse import Namespace
from threading import Lock
from typing import Any


class Singleton(type):
  """Pythonic implementation of singleton.
  """
  _instances: dict[Any, Any] = {}
  _lock: Lock = Lock()

  def __call__(cls, *args: Any, **kwargs: Any):
    with cls._lock:
      if cls not in cls._instances:
        instance = super().__call__(*args, **kwargs)
        cls._instances[cls] = instance

    return cls._instances[cls]

class Context(metaclass=Singleton):
  """Contextual data and information to inject in every class.

  Use this utility to store cli options and other env info.
  """

  def __init__(self, options: Namespace = Namespace()):
    """Creates a new Context object.

    Use this method only one time each execution.
    This class will be updated to a singleton before first major release.

    Args:
      options (Namespace, optional):
        Options from command line.
        Defaults to Namespace().
    """
    self._options = options

  def set_option(self, name: str, value):
    """Set the value of an options.

    You can set the value of an options only if it already exists.

    Args:
      name (str): name of the options to change.
      value ([type]): value of the option to set.

    Raises:
      ValueError: when trying to set an options which doesn't exists.
    """
    if name not in self._options:
      raise ValueError(f'You are trying to set {name} which doesn\'t exists \
        in options values')

    self._options[name] = value

  def options(self) -> Namespace:
    """Gets a deepcopy of options.

    To update an options, use the set_option method. It will be implemented
    before next major release.

    Returns:
      Namespace: Options from command line.
    """
    return copy.deepcopy(self._options)
