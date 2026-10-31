using System;
using System.Threading;
using System.Threading.Tasks;

// Force both buyers to check stock=1 before either decrements.
int stock = 1, readers = 0, purchased = 0;
var bothChecked = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);

async Task BuyAsync()
{
    if (Volatile.Read(ref stock) <= 0) return;
    if (Interlocked.Increment(ref readers) == 2) bothChecked.SetResult();
    await bothChecked.Task;
    Interlocked.Decrement(ref stock);
    Interlocked.Increment(ref purchased);
}

await Task.WhenAll(BuyAsync(), BuyAsync());
Console.WriteLine($"Purchased={purchased}; Stock={stock}");
