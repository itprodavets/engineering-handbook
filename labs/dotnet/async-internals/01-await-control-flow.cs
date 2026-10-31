using System;
using System.Threading.Tasks;

// Two deterministic timelines: a completed await and an explicitly gated one.
static async Task ReadyAsync()
{
    Console.Write("A");
    await Task.CompletedTask;
    Console.Write("B");
}
static async Task PendingAsync(Task gate)
{
    Console.Write("D");
    await gate;
    Console.Write("F");
}

Task ready = ReadyAsync();
Console.Write("C");
await ready;
Console.Write("|");

var gate = new TaskCompletionSource<bool>(
    TaskCreationOptions.RunContinuationsAsynchronously);
Task pending = PendingAsync(gate.Task);
Console.Write("E");
gate.SetResult(true);
await pending;
Console.WriteLine(); // ABC|DEF
