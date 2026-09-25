class Solution:
    def braceExpansionII(self, expression):
        
        def parse(s):
            parts = []
            current = {""}

            i = 0

            while i < len(s):
                
                if s[i].isalpha():
                    # Read a word
                    j = i
                    while j < len(s) and s[j].isalpha():
                        j += 1

                    word = s[i:j]

                    current = {
                        x + word for x in current
                    }

                    i = j

                elif s[i] == '{':
                    # Find matching }
                    count = 1
                    j = i + 1

                    while count:
                        if s[j] == '{':
                            count += 1
                        elif s[j] == '}':
                            count -= 1
                        j += 1

                    # Remove outer braces
                    inside = s[i + 1:j - 1]

                    # Split by top-level commas
                    options = []
                    start = 0
                    count = 0

                    for k, ch in enumerate(inside):
                        if ch == '{':
                            count += 1
                        elif ch == '}':
                            count -= 1
                        elif ch == ',' and count == 0:
                            options.append(inside[start:k])
                            start = k + 1

                    options.append(inside[start:])

                    # Union of all options
                    union = set()

                    for option in options:
                        union.update(parse(option))

                    # Concatenate with previous results
                    current = {
                        x + y
                        for x in current
                        for y in union
                    }

                    i = j

                else:
                    # comma (normally handled inside braces)
                    i += 1

            return current

        return sorted(parse(expression))