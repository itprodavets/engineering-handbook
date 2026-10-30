using System;
using System.Threading;
using System.Threading.Tasks;

using var semaphore = new SemaphoreSlim(1, 1);
await semaphore.WaitAsync();
Task second = semaphore.WaitAsync();
Console.WriteLine(second.IsCompleted);
semaphore.Release();
await second;
semaphore.Release();
