using System;
using System.Threading.Tasks;

// An independent timer never establishes completion of producer.
int data = 0;
var releaseProducer = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Task producer = Task.Run(async () =>
{
    await releaseProducer.Task;
    data = 42;
});
await Task.Delay(10);
int observed = data;
releaseProducer.SetResult();
await producer;
Console.WriteLine($"AfterDelay={observed}; AfterProducer={data}");
