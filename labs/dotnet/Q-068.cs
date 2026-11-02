using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

// Three independent gates modeled in one process, NOT a Kubernetes/network test.
var release = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
int active = 0;
async Task EnterAsync(SemaphoreSlim localGate)
{
    await localGate.WaitAsync();
    try
    {
        Interlocked.Increment(ref active);
        await release.Task;
    }
    finally { localGate.Release(); }
}
Task[] calls = Enumerable.Range(0, 3)
    .Select(_ => EnterAsync(new SemaphoreSlim(1, 1))).ToArray();
Console.WriteLine($"ActiveSeparateGates={active}");
release.SetResult();
await Task.WhenAll(calls);
Console.WriteLine("Completed=True");
