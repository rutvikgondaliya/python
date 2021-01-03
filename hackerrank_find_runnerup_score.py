if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    runnerup = list(set(arr))
    runnerup.sort(reverse = True)

    print(runnerup[1])