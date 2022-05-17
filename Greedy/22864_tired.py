get_tired, can_work, dec_tired, max_tired = map(int, input().split())

now_tired = 0
now_tasks = 0

for _ in range(24):
    if now_tired < 0:
        now_tired = 0
    if now_tired + get_tired > max_tired:
        now_tired -= dec_tired
    else:
        now_tired += get_tired
        now_tasks += can_work

print(now_tasks)