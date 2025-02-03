# Function to print a right-angled triangle star pattern
def triangle_pattern(rows):
    for i in range(1, rows + 1):
        # Print stars in each row
        print("*" * i)

# Example usage
rows = 5
triangle_pattern(rows)
