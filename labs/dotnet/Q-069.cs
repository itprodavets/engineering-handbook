using System;
using System.Threading;
using System.Threading.Tasks;

// Pending TaskCompletionSource models a slow remote response; no real network I/O.
using var gate = new SemaphoreSlim(1, 1);
var response = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
int entered = 0;
async Task CheckoutAsync()
{
    await gate.WaitAsync();
    try
    {
        Interlocked.Increment(ref entered);
        await response.Task;
    }
    finally { gate.Release(); }
}
Task first = CheckoutAsync();
Task second = CheckoutAsync();
Console.WriteLine($"EnteredBeforeReply={entered}; PermitCount={gate.CurrentCount}; SecondPending={!second.IsCompleted}");
response.SetResult();
await Task.WhenAll(first, second);
Console.WriteLine($"EnteredAfterReply={entered}; PermitCount={gate.CurrentCount}");
