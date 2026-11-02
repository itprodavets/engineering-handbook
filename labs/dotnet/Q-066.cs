using System;
using System.Threading;
using System.Threading.Tasks;

// Demonstrate a pending circular async wait, then cancel it to avoid hanging CI.
using var sem = new SemaphoreSlim(1, 1);
using var cts = new CancellationTokenSource();
bool outerEntered = false, innerEntered = false;
async Task InnerAsync()
{
    await sem.WaitAsync(cts.Token);
    try { innerEntered = true; }
    finally { sem.Release(); }
}
async Task OuterAsync()
{
    await sem.WaitAsync();
    try
    {
        outerEntered = true;
        await InnerAsync();
    }
    finally { sem.Release(); }
}
Task pending = OuterAsync();
Console.WriteLine($"OuterEntered={outerEntered}; InnerEntered={innerEntered}; Pending={!pending.IsCompleted}");
cts.Cancel();
bool canceled = false;
try { await pending; }
catch (OperationCanceledException) { canceled = true; }
Console.WriteLine($"Canceled={canceled}; RestoredCount={sem.CurrentCount}");
