from typing import Optional, Dict

class Session:

  def __init__(self, session_id: str, initialState: Optional[Dict[str, any]] = {}) -> None:
    self.id: str = session_id
    self.state: Dict[str, any] = initialState

  def setState(self, newState: Dict[str, any]) -> None:
    self.state: Dict[str, any] = self.state.update(newState)

  def resetState(self) -> None:
    self.state: Dict[str, any] = {}