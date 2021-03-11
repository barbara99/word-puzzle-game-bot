from typing import Optional, Dict

class Session:
  def __init__(self, session_id: str, initialState: Optional[dict] = {}):
    self.id = session_id
    self.state = initialState

  def setState(self, newState: Dict[str, any]) -> None:
    self.state = self.state.update(newState)

  def resetState(self) -> None:
    self.state = {}