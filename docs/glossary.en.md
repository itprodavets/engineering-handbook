# Glossary

[Русский](glossary.md) · [English](glossary.en.md)

[Home](../README.en.md) · [Interactive glossary](https://itprodavets.github.io/engineering-handbook/#/en/glossary)

C#/.NET, OS, and concurrency terminology. Full mechanisms live in one canonical lesson rather than being duplicated across answers.

## I/O

Data exchange with a network, storage or device.

Example: `await socket.ReceiveAsync(...)`

## CPU Core

Hardware resource executing machine instructions.

Example: `CPU-bound code`

## OS Kernel

Privileged software managing threads, memory and I/O.

Example: `Linux kernel`

## Thread

An OS-schedulable sequence of execution.

Example: `Thread.CurrentThread`

## ThreadPool

A runtime-managed pool of workers for queued work.

Example: `Task.Run(...)`

## Task

An object representing the eventual completion of an operation.

Example: `Task<List<Order>>`

## await

Suspends an async method if the awaited operation is incomplete.

Example: `await db.Orders.ToListAsync()`

## Continuation

Work that resumes after an awaited operation completes.

Example: `code after await`

## State Machine

Compiler-generated mechanism retaining async execution state.

Example: `compiler async rewrite`

## OS Scheduler

Selects which runnable threads execute on logical CPUs.

Example: `preemptive scheduling`

## Time Slice

Scheduling interval after which a thread may be preempted.

Example: `time sharing`

## Context Switch

Switching execution between threads while retaining their states.

Example: `preemption`

## Concurrency

Several tasks make progress over overlapping time periods.

Example: `100 runnable threads`

## Parallelism

Computations actually execute at the same instant.

Example: `8 logical CPUs`

## I/O-bound

Performance primarily limited by I/O latency or throughput.

Example: `PostgreSQL network request`

## CPU-bound

Performance primarily limited by computation.

Example: `large hash computation`

## Socket

An operating-system abstraction for network communication.

Example: `TCP connection to PostgreSQL`

## epoll

Linux API to monitor file-descriptor readiness.

Example: `network event loop`

## IOCP

Windows mechanism for efficient asynchronous I/O completion.

Example: `Windows socket I/O`

## SMT

Hardware feature exposing multiple logical CPUs per physical core.

Example: `Hyper-Threading`

## Task<T>

Represents a future outcome that yields a value of type T.

Example: `Task<int> result = ...`

## Task.Run

Queues a delegate for execution, normally on a ThreadPool worker.

Example: `await Task.Run(Compute)`

## TaskScheduler

Chooses how Task work is queued and executed; not which CPU core is used.

Example: `TaskScheduler.Default`

## Preemption

The OS scheduler interrupts a running thread so another can execute.

Example: `CPU time slice`

## Task.Delay

Returns a Task completed after a timer delay without occupying a worker for the wait.

Example: `await Task.Delay(5000)`

## Thread.Sleep

Blocks the current thread for a specified interval.

Example: `Thread.Sleep(5000)`

## Timer

A runtime or OS mechanism that signals when a specified interval elapses.

Example: `Task.Delay(5000)`

## Task.WhenAll

Returns a Task that completes after all provided tasks complete.

Example: `await Task.WhenAll(tasks)`

## ThreadPool starvation

A shortage of available workers delays queued work, often because workers are blocked.

Example: `Task.Run(() => Thread.Sleep(5000))`

## Worker Thread

An OS thread used by the runtime to execute queued work.

Example: `ThreadPool worker executing Task.Run`

## Thread Creation

Starting an additional OS thread, distinct from allocating a Task object.

Example: `new Thread(...).Start(); ThreadPool scales workers`
