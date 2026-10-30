using System;
using System.Threading;
using System.Threading.Tasks;

var gate = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);
var finished = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);
int completed = 0;

// Intentional trap: an async lambda passed to Action<int> becomes async void.
// The completion gate below makes this educational lab safe to run to completion.
Parallel.ForEach(new[] { 1, 2, 3 }, async _ =>
{
    await gate.Task;
    Console.Write("X");
    if (Interlocked.Increment(ref completed) == 3)
        finished.SetResult();
});
Console.Write("A");
gate.SetResult();
await finished.Task;
Console.WriteLine();
