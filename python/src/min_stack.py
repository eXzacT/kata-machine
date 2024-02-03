class MinStack:
    def __init__(self) -> None:
        self.stack = []
        self.min_stack = []

    def __repr__(self) -> str:
        return f"<MinStack stack: {self.stack}, min_stack: {self.min_stack}>"

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:  # If minstack is empty then just append the value
            self.min_stack.append(val)
        else:  # Otherwise append the min between curr and last in minstack
            self.min_stack.append(min(self.min_stack[-1], val))

    def pop(self) -> int:
        self.min_stack.pop()
        return self.stack.pop()

    def get_min(self) -> int:
        return self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]
