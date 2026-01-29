
class Node:

    def __init__(self, value):

        self.value = value

        self.next = None


def create_track_with_cycle(prefix_len, cycle_len):

    """Создает трассу: прямая (prefix) + кольцо (cycle)"""

    head = Node(0)

    current = head

    

 

    for i in range(1, prefix_len):

        current.next = Node(i)

        current = current.next

    

    cycle_start_node = current

    



    for i in range(cycle_len - 1):

        current.next = Node(prefix_len + i)

        current = current.next

    

    # Замыкаем круг

    current.next = cycle_start_node

    return head


# --- 1. Классический Алгоритм Флойда ---

def floyd_runner(head):

    tortoise = head

    hare = head

    steps = 0

    

    while True:

        steps += 1

        # Черепаха +1

        tortoise = tortoise.next

        
        if hare.next and hare.next.next:

            hare = hare.next.next

        else:

            return -1 # Цикла нет

            

        if tortoise == hare:

            return steps


# --- 2. Алгоритм с Гепардом ---

def roma_cheetah_runner(head):

    tortoise = head

    hare = head

    cheetah = head

    steps = 0

    

    while True:

        steps += 1

      

        tortoise = tortoise.next

        

      

        if hare.next and hare.next.next:

            hare = hare.next.next

        

    

        if cheetah.next and cheetah.next.next and cheetah.next.next.next:

            cheetah = cheetah.next.next.next

            

        
        if tortoise == hare or hare == cheetah or tortoise == cheetah:

            return steps


prefix = 100   # Длина входа до цикла

cycle = 500    # Длина самого круга

track = create_track_with_cycle(prefix, cycle)


print(f"Трасса: вход {prefix} метров, круг {cycle} метров.\n")


# Тест Флойда

start_time = time.time_ns()

floyd_steps = floyd_runner(track)

end_time = time.time_ns()

print(f"🐢 vs 🐇 (Флойд): Нашел цикл за {floyd_steps} шагов.")


# Тест Ромы

start_time = time.time_ns()

roma_steps = roma_cheetah_runner(track)

end_time = time.time_ns()

print(f"🐢 vs 🐇 vs 🐆 (Рома): Нашел цикл за {roma_steps} шагов.")


diff = floyd_steps - roma_steps

print(f"\nИТОГ: Твой алгоритм сэкономил {diff} итераций цикла!")
