# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class Heap:
    def __init__(self, x=[]):
        self.data = self.build_heap(x)
        self.size = len(self.data)

    def build_heap(self, data):
        n = len(data)
        for i in range(n//2, -1):
            self.sift_down(i,n)
        return data

    def left_child(self,i):
        return (2*i) + 1

    def right_child(self,i ):
        return (2*i) + 2

    def parent(self, i):
        return (i-1)//2

    def sift_down(self, i):
        min_index = i
        i = 'v'

        while i != min_index:
            i = min_index
            left = self.left_child(i)
            right = self.right_child(i)

            if left < len(self.data):
                if self.data[left][0] < self.data[min_index][0]:
                    min_index = left
                elif self.data[left][0] == self.data[min_index][0]:
                    if self.data[left][1] < self.data[min_index][1]:
                        min_index = left

            if right < len(self.data):
                if self.data[right][0] < self.data[min_index][0]:
                    min_index = right
                elif self.data[right][0] == self.data[min_index][0]:
                    if self.data[right][1] < self.data[min_index][1]:
                        min_index = right

            if min_index != i:
                self.data[min_index], self.data[i] = self.data[i], self.data[min_index]
            else:
                break

    def sift_up(self, i):
        while i > 0:
            top = self.parent(i)

            if self.data[top][0] > self.data[i][0]:
                self.data[top], self.data[i] = self.data[i], self.data[top]
            elif self.data[top][0] == self.data[i][0]:
                if self.data[top][1] > self.data[i][1]:
                    self.data[top], self.data[i] = self.data[i], self.data[top]
            else:
                break
            i = self.parent(i)

    def insert(self, val):
        self.size+=1
        self.data.append(val)
        self.sift_up(self.size - 1)

    def pop(self):
        result = self.data[0]
        self.data[0] = self.data[self.size - 1]
        del self.data[self.size - 1]
        self.size -= 1
        self.sift_down(0)
        return result

    def get_max(self):
        return self.data[0]

    # def change_priority(self, i, P):
    #     old_p = self.data[i]
    #     self.data[i] = P
    #     if P > old_p:
    #         self.sift_up(i)
    #     else:
    #         self.sift_down(i)

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = Heap([(0, i) for i in range(n_workers)])
    for job in jobs:
        cur = next_free_time.pop()
        result.append(AssignedJob(cur[1], cur[0]))
        next_free_time.insert((cur[0] + job ,cur[1]))

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
