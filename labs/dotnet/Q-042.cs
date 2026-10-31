using System;
using System.Threading;
using System.Threading.Tasks;

int counter = 0;
await Task.WhenAll(
    Task.Run(() => Interlocked.Increment(ref counter)),
    Task.Run(() => Interlocked.Increment(ref counter)));
Console.WriteLine($"Counter={counter}");
