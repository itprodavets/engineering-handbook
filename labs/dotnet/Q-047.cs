using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

static bool TryBuy(ref int stock)
{
    while (true)
    {
        int current = Volatile.Read(ref stock);
        if (current <= 0) return false;
        int previous = Interlocked.CompareExchange(ref stock, current - 1, current);
        if (previous == current) return true;
    }
}

int firstStock = 3;
bool[] pair = await Task.WhenAll(Enumerable.Range(0, 2)
    .Select(_ => Task.Run(() => TryBuy(ref firstStock))));
Console.WriteLine($"Stock3: Purchased={pair.Count(x => x)}; Stock={firstStock}");

int secondStock = 1;
bool[] five = await Task.WhenAll(Enumerable.Range(0, 5)
    .Select(_ => Task.Run(() => TryBuy(ref secondStock))));
Console.WriteLine($"Stock1: Purchased={five.Count(x => x)}; Rejected={five.Count(x => !x)}; Stock={secondStock}");
