using System;
using System.Threading;
using System.Threading.Tasks;

// Test gate forces a legal wrong-order interleaving; no timing assumptions.
int data = 0, ready = 0, observed = -1;
var readBeforeDataWrite = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Task producer = Task.Run(async () =>
{
    Volatile.Write(ref ready, 1);
    await readBeforeDataWrite.Task;
    data = 42;
});
Task consumer = Task.Run(() =>
{
    while (Volatile.Read(ref ready) == 0)
        Thread.Yield();
    observed = data;
    readBeforeDataWrite.SetResult();
});
await Task.WhenAll(producer, consumer).WaitAsync(TimeSpan.FromSeconds(10));
Console.WriteLine($"Observed={observed}; Final={data}");
