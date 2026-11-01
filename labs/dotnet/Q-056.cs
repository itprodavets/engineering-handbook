using System;
using System.Threading.Tasks;

Task failed = Task.FromException(new InvalidOperationException("Database error"));
Task winner = await Task.WhenAny(failed, Task.Delay(1000));
Console.WriteLine($"AfterWhenAny={winner.IsFaulted}");
try
{
    await winner;
}
catch (InvalidOperationException)
{
    Console.WriteLine("AwaitWinnerCaught=InvalidOperationException");
}
