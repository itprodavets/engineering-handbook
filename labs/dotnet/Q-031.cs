using System;
using System.Threading;
using System.Threading.Tasks;

var trace = new AsyncLocal<string>();
trace.Value = "X";
await Task.Run(() => Console.Write(trace.Value));
Console.WriteLine();
