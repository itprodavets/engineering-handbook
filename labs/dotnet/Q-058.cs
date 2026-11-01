using System;
using System.Threading;
using System.Threading.Tasks;

Task first = Task.FromException(new InvalidOperationException("Database failed"));
Task second = Task.FromCanceled(new CancellationToken(canceled: true));
Task combined = Task.WhenAll(first, second);
try
{
    await combined;
}
catch (InvalidOperationException)
{
    Console.WriteLine("Caught=InvalidOperationException");
}
Console.WriteLine($"Combined={combined.Status}; Second={second.Status}; Inner={combined.Exception!.InnerExceptions.Count}");
