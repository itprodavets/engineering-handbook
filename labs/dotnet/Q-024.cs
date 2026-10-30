using System;
using System.Threading.Tasks;

async Task PrintAsync()
{
    Console.Write("A");
    await Task.CompletedTask;
    Console.Write("B");
}

var task = PrintAsync();
Console.Write("C");
await task;
Console.WriteLine();
