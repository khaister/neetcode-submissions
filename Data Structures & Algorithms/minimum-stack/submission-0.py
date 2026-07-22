class MinStack:
    def __init__(self):
        self._stack = []
        self._current_min = None
        self._min_history = []

    def push(self, val: int) -> None:
        self._stack.append(val)
        if self._current_min is None:
            self._current_min = val
        elif self._current_min > val:
            self._current_min = val
        self._min_history.append(self._current_min)

    def pop(self) -> None:
        popped_value = self._stack.pop()
        popped_min = self._min_history.pop()
        self._current_min = self._min_history[-1] if self._min_history else None

    def top(self) -> int:
        if not self._stack:
            raise ValueError("Stack is empty")
        return self._stack[-1]

    def getMin(self) -> int:
        if self._current_min is None:
            raise ValueError("Min value not found")
        return self._current_min
