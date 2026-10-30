using System;
using System.Threading.Tasks;

int before = Environment.CurrentManagedThreadId;
await Task.CompletedTask.ConfigureAwait(false);
Console.WriteLine(before == Environment.CurrentManagedThreadId);
