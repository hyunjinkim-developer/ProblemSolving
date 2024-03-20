def main():
    answer = 0

    h = int(input())

    for h in range(h + 1):
        for m in range(60):
            for s in range(60):
                current_time = "".join(map(str, [h, m, s]))
                if "3" in current_time:
                # if "3" in str(h) + str(m) + str(s): # the same as above
                    answer += 1
    print(answer)

if __name__ == "__main__":
    main()