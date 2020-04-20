h, m = map(int, input().split())
m_diff = 45

total = h * 60 + m 
if total < m_diff:
    
    total = total + 24*60 - m_diff
else:
    total-=m_diff
h = int(total / 60)
m = int(total % 60)
    
print(f"{h} {m}")
