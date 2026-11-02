using System;
using System.Threading;

// Demonstrate Monitor thread affinity with bounded, controlled threads.
// This does not deliberately leak a monitor across an await.
object gate = new();
using var entered = new ManualResetEventSlim(false);
using var allowExit = new ManualResetEventSlim(false);
var owner = new Thread(() =>
{
    Monitor.Enter(gate);
    try { entered.Set(); allowExit.Wait(); }
    finally { Monitor.Exit(gate); }
});
owner.Start();
entered.Wait();
bool wrongOwnerThrows = false;
try { Monitor.Exit(gate); }
catch (SynchronizationLockException) { wrongOwnerThrows = true; }
finally { allowExit.Set(); }
owner.Join();
Console.WriteLine($"WrongOwnerThrows={wrongOwnerThrows}");
