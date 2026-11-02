using System;
using System.Threading;
using System.Threading.Tasks;

// Deliberately incorrect cancellation pattern, bounded and cleaned up.
using var sem = new SemaphoreSlim(1, 1);
await sem.WaitAsync(); // legitimate holder
using var cts = new CancellationTokenSource();
cts.Cancel();
bool canceled = false;
try
{
    try { await sem.WaitAsync(cts.Token); }
    finally { sem.Release(); } // BUG: no permit was acquired
}
catch (OperationCanceledException) { canceled = true; }
bool unauthorizedPermitReleased = sem.CurrentCount == 1;
bool ownerReleaseThrows = false;
try { sem.Release(); }
catch (SemaphoreFullException) { ownerReleaseThrows = true; }
Console.WriteLine($"Canceled={canceled}; UnauthorizedPermitReleased={unauthorizedPermitReleased}; OwnerReleaseThrows={ownerReleaseThrows}");
