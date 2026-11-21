def findPattern(self, pattern):
      positions = []
      pattern = pattern.upper()
      if pattern == "":
          return positions
      for i in range(len(self.sequence) - len(pattern) + 1):
          if self.sequence[i:i + len(pattern)] == pattern:
              positions.append(i)
      return positions
