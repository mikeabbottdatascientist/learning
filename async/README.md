I followed this tutorial: https://realpython.com/async-io-python/#setting-up-your-environment

# Notes
* async def introduces either a native coroutine or an asynchronous generator
* the keyword await passes ntrol back to the event loop

# Terms
* Concurrency: an umbrella term generally meaning that you allow the execution of tasks to overlap (task execution is non-sequential). Note this does not imply parallelism
* Parallelism: executing multiple tasks at the same time.
* Multiprocessing: A particular method of parallelism involving splitting tasks over multiple cpu cores
* Cooperative multitasking: A single-process, single-thread form of concurrency. This is achieved in Python's asyncio package. Imagine you have a program that must make 100 slow calls to external databases and then store the response of each one in a dictionary (assume each call is unrelated to the result of the other calls). A classical way to do this would be to make the first call and then wait for the database to respond. During this time the process is idle in the sense that the ONLY thing it's doing is checking to see if it has gotten a response yet. A different way to approach this would be to make the first call and then immediately make the next call while waiting for the first one, and then immediately move on to the next call and so on. As you go down the line making calls, you can periodically go back and check each call to see if it has a response yet, and if it does, then you can store the response in the dictionary. In this way, you are not doing parallelism (you are only executing once task at a time), but you are more efficiently alternating between tasks that would otherwise have you idling. The downside to this approach is that you don't get to use the response of a call immediately. (when the response from call 1 comes in, you might be busy making call 5).
* Coroutine:
  - TLDR: A specialized version of a Python generator function which can suspend its execution before reaching "return", and during that time it can let another coroutine execute.
* Native Coroutine
* Asynchronous generator
* Event loop



# Questions
* I've seen two conflicting statements:
  - "One process can contain multiple threads"
  - "Each thread runs a process"