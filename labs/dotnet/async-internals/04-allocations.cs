using System;
using System.Threading.Tasks;

// Allocation figures are environment-specific, NOT normative .NET guarantees.
static async Task<int> ImmediateAsync()
{
    await Task.CompletedTask;
    return 7;
}

for (int i = 0; i < 2_000; i++) _ = await ImmediateAsync(); // Warm-up.
long before = GC.GetAllocatedBytesForCurrentThread();
int sum = 0;
for (int i = 0; i < 10_000; i++) sum += await ImmediateAsync();
long bytes = GC.GetAllocatedBytesForCurrentThread() - before;

Console.WriteLine($"Sum={sum}");
Console.WriteLine($"CallerThreadAllocatedBytes={bytes}");
