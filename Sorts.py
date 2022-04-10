class Sorts():


    __private_swaps = 0
    __private_compares = 0
    var = 0

    def round(self, f: float):
        """Округляем число в меньшую сторону"""
        x = int(f)
        if float(x) < f:
            x -= 1
        return x

    def compare(self, el1, el2, reverse = False):
        """сравниваем значения для убывающиего и возрастающего порядка - если параметр reverse = False,
        а первый элемент больше второго, то их нужно поменять местами, то есть возвращаем True, если же
        reverse = True, то если первый элемент меньше второго, меняем их местами, возвращяя значение True"""
        self.__private_compares += 1
        if(el1 > el2):
            reverse = not reverse
        return reverse

    def swap(self, clist: list, el, nel):
        self.__private_swaps += 1
        clist[el], clist[nel] = clist[nel], clist[el]


    def bubble_sort(self, clist: list, reverse: bool):
        """Сложность алгоритма O(x^2), так как в худшем случае сравниваем элементы n - 1 + n - 2 + ... =
        n * (1 + n - 1)/2 = (n^2)/2 = O(x^2) раз, в лучшем случае массив будет отсортирован pf n = O(n) раз,
        в среднем случае O(x^2), так как любое самоме малое число в конце вынуждает сортировать максимальное
        количество раз"""
        changed = True
        last = len(clist) - 1
        while (changed):
            """Если значения не были переставлены в текущей итерации, то массив отсортирован - завершаем сортировку,
            проходим по всем элементам списка, кроме последнего"""
            changed = False
            for el in range(0, last):
                if(self.compare(clist[el], clist[el + 1], reverse)):
                    self.swap(clist, el, el+1)
                    changed = True
            last -= 1

    def shaker_sort(self, clist: list, reverse: bool):
        """Модификация сортировки пузырьком - можно заметить, что при наличии самого малого элемента в конце
        списка количество сортировок достигает максимума, тогда для ускорения работы можно проходить от начала
        к концу списка и от конца к началу, тогда эта проблема уже не возникает, асимптотика та же, что и у пузырька,
        однако реальное время работы лучше"""
        changed = True
        last = len(clist) - 1
        first = -1;
        while (changed):
            """Если значения не были переставлены в текущей итерации, то массив отсортирован - завершаем сортировку,
            проходим по всем элементам списка, кроме последнего"""
            changed = False

            first += 1

            for el in range(first, last):
                if (self.compare(clist[el], clist[el + 1], reverse)):
                    self.swap(clist, el, el+1)
                    changed = True

            if(not changed):#если при итерации массив не сортировался, значит он отсортирован - завершаем сортировку
                break

            last -= 1

            for el in range(last, first, -1):
                if (self.compare(clist[el - 1], clist[el], reverse)):

                    self.swap(clist, el, el-1)
                    changed = True


    def comb_sort(self, clist: list, reverse: bool):
        """Модификация сортировки пузырьком - начала сортируем дальние друг от друга элемента на рсстоянии step,
         которое определяется коэффициентом k ,затем ближние, в конце обычная сортировка
        пузырьком, но с меньшим количеством итераций"""
        k = 1.2473309;

        step = len(clist) - 2;
        while (step > 1):
            i = 0
            while (i + step < len(clist)):
                if(clist[i + step] < clist[i]):
                    self.swap(clist, i, i + step)
                i += 1
            step /= k
            step = self.round(step)#Округляем число в меньшую сторону, чтобы не попасть в бесконечный цикл

        changed = True
        last = len(clist) - 1
        while (changed):
            """Обычная сортировка пузырьком"""
            changed = False
            for i in range(0, last):
                if (self.compare(clist[i], clist[i + 1], reverse)):
                    self.__private_swaps += 1
                    clist[i], clist[i + 1] = clist[i + 1], clist[i]
                    changed = True
            last -= 1

    def insertion_sort(self, clist: list, reverse: bool):
        """Сортировка вставками - вставляем каждый последующий элемент в подходящую для него позицию,
        сложность в лучшем случае - O(n) сравнений, в худшем и среднем O(n^2) сравнений и обменов"""

        for el in range(0, len(clist) - 1):
            i = el
            self.__private_compares += 1
            while(self.compare(clist[i], clist[i + 1], reverse) and i >= 0):
                self.__private_swaps += 1
                clist[i], clist[i + 1] = clist[i + 1], clist[i]
                i -= 1

    def shell_sort(self, clist: list, reverse: bool):
        """Модификация сортировки вставками - предварительно разбиваем элементы на
         множества с шагом step, затем сравниваем между собой и меняем местами элементы
         этих множеств, их сортируем вставками пока step не станет равным 0"""
        step = len(clist) // 2


        while(step > 0):
            i = step
            while(i < len(clist) - 1):
                j = i - step
                while(j >= 0 and self.compare(clist[j], clist[j + step])):
                    clist[j], clist[j + step] = clist[j + step], clist[j]
                    self.__private_compares += 1
                    self.__private_swaps += 1
                    j -= step
                i += 1
            step //= 2



    def tree_sort(self, clist: list, reverse: bool):

        pass

    def gnome_sort(self, clist: list, reverse: bool):

        pass

    def selection_sort(self, clist: list, reverse: bool):

        pass

    def heap_sort(self, clist: list, reverse: bool):

        pass

    def quick_sort(self, clist: list, reverse: bool):

        pass

    def merge_sort(self, clist: list, reverse: bool):

        pass



    def sort(self, clist: list, sort_type: str, reverse = False):
        self.__private_compares = self.__private_swaps = 0
        if (len(clist) < 2):
            return
        match sort_type:
            case 'Сортировка пузырьком':
                self.bubble_sort(clist, reverse)
            case 'Коктейльная сортировка':
                self.shaker_sort(clist, reverse)
            case 'Сортировка расчёской':
                self.comb_sort(clist, reverse)
            case 'Сортировка вставками':
                self.insertion_sort(clist, reverse)
            case 'Сортровка Шелла':
                self.shell_sort(clist, reverse)
            case 'Сортировка деревом':
                self.tree_sort(clist, reverse)
            case 'Гномья сортировка':
                self.gnome_sort(clist, reverse)
            case 'Сортировка выбором':
                self.selection_sort(clist, reverse)
            case 'Пирамидальная сортировка':
                self.heap_sort(clist, reverse)
            case 'Быстрая сортировка':
                self.quick_sort(clist, reverse)
            case 'Сортировка слиянием':
                self.merge_sort(clist, reverse)
        return self.__private_compares, self.__private_swaps