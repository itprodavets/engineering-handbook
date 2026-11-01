using System;
using System.Threading.Tasks;

var pending = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Task winner = await Task.WhenAny(Task.CompletedTask, pending.Task);
Console.WriteLine($"LoserCompletedBefore={pending.Task.IsCompleted}");
pending.SetResult();
await pending.Task;
Console.WriteLine($"LoserCompletedAfter={pending.Task.IsCompleted}");
