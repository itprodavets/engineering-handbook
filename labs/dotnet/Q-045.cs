using System;
using System.Threading;
using System.Threading.Tasks;

int stock = 1, purchased = 0;
await Task.WhenAll(
    Task.Run(() => { if (Interlocked.CompareExchange(ref stock, 0, 1) == 1) Interlocked.Increment(ref purchased); }),
    Task.Run(() => { if (Interlocked.CompareExchange(ref stock, 0, 1) == 1) Interlocked.Increment(ref purchased); }));
Console.WriteLine($"Purchased={purchased}; Stock={stock}");
