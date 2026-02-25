import sys

INF = 10**9

def resolve():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    out_lines = []

    while True:
        try:
            M = int(next(it))
            N = int(next(it))
        except StopIteration:
            break

        if M == 0:
            break

        coins = [int(next(it)) for _ in range(N)]

        dp = [INF] * (M + 1)
        dp[0] = 0

        # unbounded knapSack / coin change
        for c in coins:
            # iterando para frente, pois moedas são ilimitadas
            for v in range(c, M + 1):
                # evita acesso desnecessário
                prev = dp[v - c] + 1
                if prev < dp[v]:
                    dp[v] = prev

        if dp[M] >= INF:
            out_lines.append("impossivel\n")
        else:
            out_lines.append(str(dp[M]) + "\n")

    sys.stdout.write("".join(out_lines))

if __name__ == "__main__":
    resolve()
