using System;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;

// Bounded illustrative workload. Do not expect exact thread or queue counts.
const int tasksCount = 24;
Task[] blockedWorkers = Enumerable.Range(0, tasksCount)
    .Select(_ => Task.Run(() => Thread.Sleep(150)))
    .ToArray();

await Task.Delay(25);
Console.WriteLine($"ThreadPoolThreadCount={ThreadPool.ThreadCount}");
Console.WriteLine($"PendingWorkItemCount={ThreadPool.PendingWorkItemCount}");
await Task.WhenAll(blockedWorkers);
Console.WriteLine("Finished=True");
