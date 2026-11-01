using System;
using System.Threading.Tasks;

static async Task FirstAsync()
{
    await Task.Yield();
    throw new OperationCanceledException("Cancelled");
}

Task first = FirstAsync();
Task second = Task.FromException(new OperationCanceledException("Cancelled"));
try
{
    await first;
}
catch (OperationCanceledException) { }
Console.WriteLine($"AsyncMethod={first.Status}; FromException={second.Status}");
