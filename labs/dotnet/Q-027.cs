using System;
using System.Threading.Tasks;

var all = Task.WhenAll(
    Task.FromException(new InvalidOperationException("A")),
    Task.FromException(new ArgumentException("B")));
try
{
    await all;
}
catch (Exception)
{
    Console.WriteLine(all.Exception!.InnerExceptions.Count);
}
