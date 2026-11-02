using System;
using System.Threading;
using System.Threading.Tasks;

using var sem = new SemaphoreSlim(2, 2);
var release = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
int entered = 0;
async Task WorkAsync()
{
    await sem.WaitAsync();
    try
    {
        Interlocked.Increment(ref entered);
        await release.Task;
    }
    finally { sem.Release(); }
}
Task first = WorkAsync(), second = WorkAsync(), third = WorkAsync(), fourth = WorkAsync();
Console.WriteLine($"EnteredBeforeRelease={entered}; PermitCount={sem.CurrentCount}; ThirdPending={!third.IsCompleted}");
release.SetResult();
await Task.WhenAll(first, second, third, fourth);
Console.WriteLine($"EnteredAfterRelease={entered}; PermitCount={sem.CurrentCount}");
