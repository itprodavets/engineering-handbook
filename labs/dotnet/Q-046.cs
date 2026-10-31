using System;
using System.Threading;
using System.Threading.Tasks;

int stock = 3;
int[] previous = new int[2];
await Task.WhenAll(
    Task.Run(() => previous[0] = Interlocked.CompareExchange(ref stock, 2, 3)),
    Task.Run(() => previous[1] = Interlocked.CompareExchange(ref stock, 2, 3)));
Array.Sort(previous);
Console.WriteLine($"Previous={previous[0]},{previous[1]}; Stock={stock}");
