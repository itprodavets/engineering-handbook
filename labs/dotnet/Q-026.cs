using System;
using System.Threading;
using System.Threading.Tasks;

var failed = Task.FromException(new InvalidOperationException("boom"));
var winner = await Task.WhenAny(failed, Task.Delay(Timeout.Infinite));
Console.WriteLine(winner.IsFaulted);
