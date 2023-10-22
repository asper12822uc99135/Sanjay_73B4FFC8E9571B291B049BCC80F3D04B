#Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements. In python
def is_leap_year(year: int) -> bool:
  """Determines whether a given year is a leap year.

  Args:
    year: The year to check.

  Returns:
    True if the year is a leap year, False otherwise.
  """

  if year % 4 != 0:
    return False
  elif year % 100 == 0 and year % 400 != 0:
    return False
  else:
    return True


def main():
  year = int(input("Enter a year: "))

  if is_leap_year(year):
    print(f"{year} is a leap year.")
  else:
    print(f"{year} is not a leap year.")


if __name__ == "__main__":
  main()

'''
Enter a year: 2024
2024 is a leap year.
Enter a year: 2100
2100 is not a leap year.
'''