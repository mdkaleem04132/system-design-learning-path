
import sys

def solve():
    input = sys.stdin.read
    data = input().split()

    if not data:
        return
    
    n = int data([0])
    arr [int(x for x in data[1:n+1])]
    target = int(data[n+1])

    left = 0
    right = n-1

    while left < right:
        current_sun = arr[left] + arr[right]

        if current_sun == target:

            print(f"{left + 1} {right + 1}")
            return

        elif current_sum <target:
            left -= 1

        else:
            right -= 1

if __name__ == '__main__':
    solve()
