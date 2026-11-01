using System;
using System.Threading.Tasks;

// A gate forces the consumer to read before producer writes.
int data = 0;
var consumerHasRead = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Task<int> consumer = Task.Run(() =>
{
    int observed = data;
    consumerHasRead.SetResult();
    return observed;
});
Task producer = Task.Run(async () =>
{
    await consumerHasRead.Task;
    data = 42;
});
await Task.WhenAll(producer, consumer).WaitAsync(TimeSpan.FromSeconds(10));
Console.WriteLine($"Observed={consumer.Result}; Final={data}");
