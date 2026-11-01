using System;
using System.Threading.Tasks;

int data = 0;
Task producer = Task.Run(() => data = 42);
await producer;
Console.WriteLine($"Data={data}");
