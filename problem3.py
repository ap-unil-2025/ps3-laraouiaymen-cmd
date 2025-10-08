"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""


def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        nb = input("Enter numbers one at a time. Type 'done' when finished.")
        if nb == "done":
            break
        try:
            float(nb)
            nb = float(nb)
            numbers.append(nb)
        except ValueError:
            print(f" the format {nb} is not adequate")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    count = len(numbers)
    sum_list = sum(numbers)
    average = sum_list / count
    minimum = min(numbers)
    maximum = max(numbers)
    even = 0
    odd = 0

    for i in numbers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    analysis = {
        "count": count,
        "sum": sum_list,
        "average": average,
        "minimum": minimum,
        "maximum": maximum,
        "even": even,
        "odd": odd,
    }

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.

    Args:
        analysis (dict): Dictionary containing analysis results
    """
    if not analysis:
        return None

    print("\nAnalysis Results:")
    for key, items in analysis.items():
        print(f"{key} : {items}")

    print("-" * 20)


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()
