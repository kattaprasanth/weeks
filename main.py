from datetime import date, timedelta
import unittest

def get_previous_week_range(weeks):
    if weeks <= 0:
        raise Exception("weeks should not be less than or equal to 0")
    current_week = 1
    total_weeks = current_week + weeks
    previous_date = date.today() - timedelta(days=7*total_weeks)
    result = previous_date.isocalendar()
    output = []
    for i in range(weeks):
        output.append(f"{result.year}-{result.week + i}")
    print(output)
    return f"{result.year}-{result.week}"


class TestPreviousWeeksRange(unittest.TestCase):
    def test_get_previous_one_week_info(self):
        expected = "2024-52"
        got = get_previous_week_range(1)
        self.assertEqual(expected, got)

    def test_get_previous_two_week_info(self):
        expected = "2024-51"
        got = get_previous_week_range(2)
        self.assertEqual(expected, got)
    
    def test_get_previous_three_week_info(self):
        expected = "2024-50"
        got = get_previous_week_range(3)
        self.assertEqual(expected, got)
    
    def test_get_previous_ten_week_info(self):
        expected = "2024-43"
        got = get_previous_week_range(10)
        self.assertEqual(expected, got)
    
    def test_get_previous_one_year_week_info(self):
        expected = "2024-1"
        got = get_previous_week_range(52)
        self.assertEqual(expected, got)

if __name__ == '__main__':
    # unittest.main()
    get_previous_week_range(1)
    get_previous_week_range(2)
    get_previous_week_range(3)
    get_previous_week_range(10)
    get_previous_week_range(52)
    # get_previous_week_range(100)