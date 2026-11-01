using System;
using System.Threading;
using System.Threading.Tasks;

int data = 0, ready = 0;
Task producer = Task.Run(() =>
{
    data = 42;
    Volatile.Write(ref ready, 1);
});
Task<int> consumer = Task.Run(() =>
{
    while (Volatile.Read(ref ready) == 0)
        Thread.Yield();
    return data;
});
int observed = await consumer.WaitAsync(TimeSpan.FromSeconds(10));
await producer;
Console.WriteLine($"Published={observed}");
