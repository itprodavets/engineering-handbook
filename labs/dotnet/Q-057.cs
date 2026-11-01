using System;
using System.Threading.Tasks;

Task first = Task.FromException(new InvalidOperationException("Error 1"));
Task second = Task.FromException(new ArgumentException("Error 2"));
Task combined = Task.WhenAll(first, second);
try
{
    await combined;
}
catch (Exception error)
{
    Console.WriteLine($"AwaitCaughtOne={error is InvalidOperationException || error is ArgumentException}");
}
Console.WriteLine($"InnerExceptions={combined.Exception!.InnerExceptions.Count}");
