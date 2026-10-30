using System;
using System.Linq;
using System.Threading.Tasks;

int counter = 0;
await Task.WhenAll(
    Enumerable.Range(0, 10_000)
        .Select(_ => Task.Run(() => counter++)));
Console.WriteLine(counter);
