class Stack:
    def __init__(self):
        self.__st = list()

    def __str__(self):
        return ';'.join(self.__st)

    def push(self, elem):
        self.__st.append(elem)

    def pop(self):
        if len(self.__st) == 0:
            return None
        return self.__st.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        display = list()
        if self.task:
            for i in sorted(self.task.keys()):
                display.append(f'{str(i)} {self.task[i]}\n')

        return ''.join(display)

    def new_task(self, task, priority):
        if priority not in self.task:
            self.task[priority] = Stack()
        self.task[priority].push(task)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)

# зачтено