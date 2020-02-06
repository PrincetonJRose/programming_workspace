class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern
      
    def __iter__(self):
        yield from self.pattern
      
    def __str__(self):
        output = []
        for blip in self:
            if blip == '.':
                output.append('dot')
            else:
                output.append('dash')
        return '-'.join(output)
    
    @classmethod
    def from_string(cls, string):
        morse_code = []
        code = string.split("-")
        for char in code:
            if char == 'dash':
                morse_code.append('_')
            else:
                morse_code.append('.')
        return cls(morse_code)

class S(Letter):
    def __init__(self):
         pattern = ['.', '.', '.']
         super().__init__(pattern)