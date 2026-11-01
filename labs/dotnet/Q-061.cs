using System;
using System.Threading;
using System.Threading.Tasks;

Task faulted = Task.FromException(new OperationCanceledException("Cancelled"));
Task canceled = Task.FromCanceled(new CancellationToken(canceled: true));
Console.WriteLine($"FromException={faulted.Status}; FromCanceled={canceled.Status}");
