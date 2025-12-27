# id узла и id родителя, None - корень
tree = {
    1: None,
    10: 1,
    20: 1,
    30: 1,
    100: 10,
    101: 10,
    200: 20,
    300: 30,
    301: 30,
    1000: 100,
    1001: 100,
    1010: 101,
    2000: 200,
    2001: 200,
    2002: 200,
    3010: 301,
    3011: 301
}

def make_closure(adj):
    # Собираем детей для каждого узла
    children = {}
    for node in adj:
        children[node] = []
    for node, parent in adj.items():
        if parent is not None:
            children[parent].append(node)
    
    closure = []

    def dfs(ancestor, current, depth):
        closure.append((ancestor, current, depth))
        for child in children[current]:
            dfs(ancestor, child, depth + 1)

    for node in adj:
        dfs(node, node, 0)

    return closure

# Запуск
closure_table = make_closure(tree)

# Выводим только несколько строк (чтобы не засорять экран)
print("Первые 20 записей из таблицы замыканий:")
for i, (a, d, dep) in enumerate(closure_table[:20]):
    print(f"{a} → {d} (глубина {dep})")

print("...")
print(f"Всего записей: {len(closure_table)}")



