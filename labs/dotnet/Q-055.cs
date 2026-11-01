using System;
using System.Threading.Tasks;

// A timeout-like already-completed Task wins; producer completes before inspection.
var producerSignal = new TaskCompletionSource(
    TaskCreationOptions.RunContinuationsAsynchronously);
Task producer = producerSignal.Task;
Task winner = await Task.WhenAny(producer, Task.CompletedTask);
producerSignal.SetResult();
await producer;
Console.WriteLine($"ProducerWon={ReferenceEquals(winner, producer)}; ProducerCompleteNow={producer.IsCompleted}");
