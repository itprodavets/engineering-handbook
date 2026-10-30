using System;
using System.Threading.Tasks;

Task<Task> outer = Task.Factory.StartNew<Task>(
    async () => await Task.Delay(100));
Task inner = await outer;
Console.WriteLine("Outer awaited");
await inner;
Console.WriteLine("Inner awaited");
