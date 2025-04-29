class CryptarithmeticSolver:
    def __init__(self, puzzle):
        """
        Initialize the solver with a puzzle string like "SEND + MORE = MONEY"
        """
        # Parse the puzzle
        parts = puzzle.replace(" ", "").split("=")
        self.result = parts[1].strip()
        addends = parts[0].split("+")
        self.addends = [addend.strip() for addend in addends]
        
        # Get all unique letters
        self.letters = set()
        for word in self.addends + [self.result]:
            for letter in word:
                self.letters.add(letter)
        
        # Identify first letters (can't be zero)
        self.first_letters = set()
        for word in self.addends + [self.result]:
            self.first_letters.add(word[0])
            
        self.letters = list(self.letters)
        self.solution = None
    
    def solve(self):
        """Solve the cryptarithmetic puzzle"""
        self.solution = {}
        available_digits = list(range(10))
        return self._backtrack(0, available_digits)
    
    def _backtrack(self, index, available_digits):
        """Backtracking algorithm to assign digits to letters"""
        # Base case: all letters assigned
        if index == len(self.letters):
            if self._is_valid_solution():
                return True
            return False
        
        letter = self.letters[index]
        
        for i, digit in enumerate(available_digits):
            # Skip zero for first letters
            if digit == 0 and letter in self.first_letters:
                continue
                
            # Assign digit to letter
            self.solution[letter] = digit
            
            # Remove digit from available digits
            remaining_digits = available_digits[:i] + available_digits[i+1:]
            
            # Continue with next letter
            if self._backtrack(index + 1, remaining_digits):
                return True
                
        # Backtrack if no valid assignment found
        if letter in self.solution:
            del self.solution[letter]
        return False
    
    def _is_valid_solution(self):
        """Check if current assignment satisfies the equation"""
        # Convert words to numbers based on current assignment
        addend_values = []
        for addend in self.addends:
            value = 0
            for letter in addend:
                value = value * 10 + self.solution[letter]
            addend_values.append(value)
        
        result_value = 0
        for letter in self.result:
            result_value = result_value * 10 + self.solution[letter]
        
        # Check if sum of addends equals result
        return sum(addend_values) == result_value
    
    def display_solution(self):
        """Display the solution"""
        if not self.solution:
            return "No solution found"
        
        # Print the assignment
        assignment = {letter: self.solution[letter] for letter in self.letters}
        
        # Convert words to numbers based on solution
        word_values = {}
        for word in self.addends + [self.result]:
            value = 0
            for letter in word:
                value = value * 10 + self.solution[letter]
            word_values[word] = value
        
        # Format the output
        output = "Solution:\n"
        output += "Letter mapping: " + str(assignment) + "\n"
        output += " + ".join([f"{word} = {word_values[word]}" for word in self.addends])
        output += f" = {self.result} = {word_values[self.result]}"
        
        return output

# Example usage
if __name__ == "__main__":
    puzzle = "SEND + MORE = MONEY"
    solver = CryptarithmeticSolver(puzzle)
    if solver.solve():
        print(solver.display_solution())
    else:
        print("No solution found")