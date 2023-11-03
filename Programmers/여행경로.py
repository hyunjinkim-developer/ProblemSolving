def dfs(tickets, path, start):
    path.append(start)

    if not tickets:
        return True

    done = False
    for i, ticket in enumerate(tickets):
        if ticket[0] == start:
            remains = tickets.copy()
            remains.pop(i)
            done = dfs(remains, path, ticket[1])
            if done:
                break
            else:
                path.pop()
    return done


def solution(tickets):
    answer = []

    tickets.sort()
    dfs(tickets, answer, "ICN")
    return answer

