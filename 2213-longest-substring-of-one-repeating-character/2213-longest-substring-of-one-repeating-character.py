class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Segment tree arrays
        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)

        prefix = [0] * (4 * n)
        suffix = [0] * (4 * n)
        best = [0] * (4 * n)

        # Build tree
        def build(node, l, r):
            if l == r:
                left_char[node] = s[l]
                right_char[node] = s[l]

                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            pull(node, l, r)

        # Merge two children
        def pull(node, l, r):
            left_node = node * 2
            right_node = node * 2 + 1

            left_char[node] = left_char[left_node]
            right_char[node] = right_char[right_node]

            prefix[node] = prefix[left_node]
            suffix[node] = suffix[right_node]

            best[node] = max(
                best[left_node],
                best[right_node]
            )

            # Can join across middle?
            if right_char[left_node] == left_char[right_node]:

                mid = (l + r) // 2

                left_length = mid - l + 1
                right_length = r - mid

                # Entire left side has same character
                if prefix[left_node] == left_length:
                    prefix[node] = (
                        prefix[left_node] +
                        prefix[right_node]
                    )

                # Entire right side has same character
                if suffix[right_node] == right_length:
                    suffix[node] = (
                        suffix[left_node] +
                        suffix[right_node]
                    )

                # Repeating substring crosses middle
                best[node] = max(
                    best[node],
                    suffix[left_node] + prefix[right_node]
                )

        # Update one index
        def update(node, l, r, index, char):
            if l == r:
                left_char[node] = char
                right_char[node] = char

                prefix[node] = 1
                suffix[node] = 1
                best[node] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(
                    node * 2,
                    l,
                    mid,
                    index,
                    char
                )
            else:
                update(
                    node * 2 + 1,
                    mid + 1,
                    r,
                    index,
                    char
                )

            pull(node, l, r)

        # Build initially
        build(1, 0, n - 1)

        answer = []

        # Process queries
        for char, index in zip(queryCharacters, queryIndices):

            update(
                1,
                0,
                n - 1,
                index,
                char
            )

            # Root contains answer for entire string
            answer.append(best[1])

        return answer