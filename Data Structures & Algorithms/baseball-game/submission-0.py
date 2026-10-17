class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # Create our stack
        records = []

        # Begin traversing through the operations
        for operation in operations:
            # Try to convert to an integer, if it succeeds,
            # then we know it's a number, otherwise, its' one
            # of the other operations
            try:
                digit = int(operation)
                records.append(digit)
            except ValueError:
                # Now check for the other operations
                if operation == "+":
                    records.append(records[-1] + records[-2])
                elif operation == "C":
                    records.pop()
                else:
                    records.append(records[-1] * 2)

        # Return the final sum of all records
        return sum(records)