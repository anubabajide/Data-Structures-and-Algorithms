# python3

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size, shift=0):
        self.size = size
        self.finish_time = deque()
        self.current_size = 0
        self.shift=shift

    def process(self, request):
        if self.current_size >0:
            while self.finish_time[0]<=request[0]:
                self.finish_time.popleft()
                self.current_size-=1
                if self.current_size==0:
                    break

        if self.current_size < self.size:
            self.finish_time.append(self.shift + request[1])
            self.shift += request[1]
            self.current_size+=1
            return Response(False, max((self.shift - request[1]), request[0]))

        else:
            return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    if len(requests) > 0:
        buffer = Buffer(buffer_size, requests[0][0])
    else:
        buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
