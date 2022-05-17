'''
Simple Asyncio example (adds numbers asynchronously)

Creates two addition threads that run asynchronously:
- Addition threads take in a list
- Adds one element to the thread's sum then sleeps for 1 second

TODO: Add more to this script/setup networking
'''

import asyncio
import time


async def addition_thread(numbers_to_add, start_time, thread_id):
    '''
    Adds numbers and sleeps for one second between adds
    '''
    print('Started thread {}: time is {:.3}'.format(thread_id, time.time() - start_time))
    sum = 0
    for number in numbers_to_add:
        sum += number
        # await asyncio.sleep(1)
        await asyncio.sleep(1)
        print('Thread: {}   -   Current Sum: {}   -   Time: {:.3}'.format(thread_id, sum, time.time() - start_time))
    return sum


async def main():
    start_time = time.time()
    num_threads = 0

    sum1, sum2 = await asyncio.gather(
        addition_thread(numbers_to_add=[1, 2, 3], start_time=start_time, thread_id=num_threads),  # Sum is 6
        addition_thread(numbers_to_add=[4, 5, 6], start_time=start_time, thread_id=num_threads+1)  # Sum is 15
    )

    print('sum1 = {}'.format(sum1))
    print('sum2 = {}'.format(sum2))

if __name__ == '__main__':
    asyncio.run(main())
