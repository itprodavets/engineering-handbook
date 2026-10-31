using System;
using System.Threading.Tasks;

// Force both logical operations to read 0 before either writes.
int value = 0;
var release = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);

async Task IncrementAsync()
{
    int snapshot = value;
    await release.Task;
    value = snapshot + 1;
}

Task first = IncrementAsync();
Task second = IncrementAsync();
release.SetResult();
await Task.WhenAll(first, second);
Console.WriteLine($"Value={value}"); // Value=1: one update was lost.
