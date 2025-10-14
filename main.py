from typing import List
import math
"""
The Fibonacci sequence is a series of numbers where each number 
is the sum of the two preceding ones, starting from 0 and 1.
The sequence looks like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The function below receives an integer n, which represents the n-th term 
of the sequence, and must return a list from the first value up to the n-th term.

Example:
    n = 3
    return [0, 1, 1]
"""
def fibonacci(n: int) -> list[int]:
    if not isinstance(n, int):
        raise ValueError("n must be int")
    if n <= 0:
        return []
    seq = [0]
    if n == 1:
        return seq
    seq.append(1)
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])

    return seq


"""
The function below receives a list of numbers (nums) 
and returns a list of even numbers from nums in ascending order.

Example:
    nums = [1, 3, 2, 27, 50, 17, 8, 4, 98, 22]
    return [2, 4, 8, 22, 50, 98]
"""
def even(nums: list[int]) -> list[int]:
    ev=[ x for x in list if isinstance(x, int) and x % 2 == 0]
    return sorted(ev)


"""
The function below receives a list of numbers (nums) 
and returns a list of odd numbers from nums in descending order.

Example:
    nums = [1, 3, 2, 27, 50, 17, 8, 4, 98, 22]
    return [27, 17, 3, 1]
"""
def odd(nums: list[int]) -> list[int]:
    od = [x for x in list if isinstance(x, int) and x % 2 != 0]
    return sorted(od, reverse=True)


"""
This function receives a list of numbers (nums)
and returns a string that says:

 * 'Odd'  if the sum of odd numbers is greater than the sum of even numbers.
 * 'Even' if the sum of even numbers is greater than the sum of odd numbers.
 * 'Tie'  if both sums are equal.

Example:
    nums = [1, 2, 3]
    sum(odd) = 4, sum(even) = 2 → returns 'Odd'
"""
def even_vs_odd(nums: list[int]) -> str:
    ev_sum = sum(x for x in list if isinstance(x, int) and x % 2 == 0)
    od_sum = sum(x for x in list if isinstance(x, int) and x % 2 != 0)
    if ev_sum > od_sum:
        return "Even"
    if od_sum > ev_sum:
        return "Odd"
    return "Tie"


"""
This function checks if 'n' is a prime number.

It should:
 * Return True if n is prime, False otherwise.
 * Raise a ValueError if n is negative or not an integer.

Example:
    is_prime(7) → True
    is_prime(10) → False
    is_prime(-3) → raises ValueError
"""
def is_prime(n)->bool:
    if not isinstance(n,int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    if n < 2:
        return False
    if n ==2:
        return True
    if n % 2==0:
        return False
    i = 3
    limit=int(math.sqrt(n))+1
    while i <= limit:
        if n % i == 0:
            return False
        i += 2
    return True


"""
This function takes in a fullname, short year, 
and campus code ('jhb' or 'cpt') to generate a WeThinkCode_ email address.

Example:
    Input: ('Auston Mtabane', '2024', 'jhb')
    Output: 'aumtajhb024@student.wethinkcode.co.za'

Hint:
    - Use lowercase letters.
    - Look at the pattern of the example carefully.
"""
def generate_email(fullname: str, year: str, campus: str) -> str:
    while isinstance(fullname,str) :
        isinstance(year, str) or not isinstance(campus,str)
    return ""

