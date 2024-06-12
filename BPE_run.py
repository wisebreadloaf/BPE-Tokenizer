import json

with open("./output.json", "r", encoding="utf-8") as f:
        text = f.read()
        y = json.loads(text)

s = "Once upon a time"
m = []
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        t = s[i:j]
        if y.get(t):
            m.append(t)

m = sorted(m, key=lambda x: len(x), reverse=True)
print(m)
n = 0
print(f"given s: {s}")
while n < len(m) and s:
    substring = m[n]
    if s.endswith(substring):
        s = s[:-len(substring)]
        print(f'"{s}" ends with: "{substring}"')
    elif s.startswith(substring):
        s = s[len(substring):]
        print(f'"{s}" starts with: "{substring}"')
    elif substring in s:
        s = s.replace(substring, "")
        print(f'"{s}" in middle: "{substring}"')
    n+=1
