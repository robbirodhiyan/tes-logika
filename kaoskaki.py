def count_sock_pairs(socks):
    from collections import Counter
    sock_count = Counter(socks)
    pairs = sum(count // 2 for count in sock_count.values())
    return pairs

input_string = input("Input: ").strip()

socks = list(map(int, input_string.strip('[]').split()))

output = count_sock_pairs(socks)

print(f"Output yang diharapkan: {output}")
