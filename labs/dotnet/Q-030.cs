using System;
using System.Threading;
using System.Threading.Tasks;

using var cts = new CancellationTokenSource();
var started = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);
var release = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);

var task = Task.Run(async () =>
{
    started.SetResult();
    await release.Task;
    Console.Write("DONE");
}, cts.Token);

await started.Task;
cts.Cancel();
release.SetResult();
await task;
Console.WriteLine();
