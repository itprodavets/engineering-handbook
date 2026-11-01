using System;
using System.Threading.Tasks;

var gate = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Task failure = Task.FromException(new InvalidOperationException("Error"));
Task combined = Task.WhenAll(failure, gate.Task);
Console.WriteLine($"CompletedBeforeGate={combined.IsCompleted}");
gate.SetResult();
try
{
    await combined;
}
catch (InvalidOperationException)
{
    Console.WriteLine($"StatusAfterGate={combined.Status}");
}
