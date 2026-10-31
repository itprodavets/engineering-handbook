using System;
using System.Threading;

int stock = 1;
int previous = Interlocked.CompareExchange(ref stock, 0, 1);
Console.WriteLine($"Previous={previous}; Stock={stock}");
int original = 10, current = 10;
int old = Interlocked.CompareExchange(ref original, current - 3, current);
Console.WriteLine($"Current={current}; Previous={old}; Stock={original}");
