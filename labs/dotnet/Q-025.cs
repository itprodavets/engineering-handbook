using System;
using System.Threading.Tasks;

var gate = new TaskCompletionSource(TaskCreationOptions.RunContinuationsAsynchronously);

async Task PrintAsync()
{
    Console.Write("A");
    await gate.Task;
    Console.Write("B");
}

var task = PrintAsync();
Console.Write("C");
gate.SetResult();
await task;
Console.WriteLine();
