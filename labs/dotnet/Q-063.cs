using System;
using System.Threading.Tasks;

static async Task FailAsync()
{
    await Task.CompletedTask;
    throw new InvalidOperationException("Error");
}

Task task = FailAsync();
Console.WriteLine($"AfterCall={task.Status}");
try
{
    await task;
}
catch (InvalidOperationException)
{
    Console.WriteLine("ExceptionThrownOnAwait=True");
}
