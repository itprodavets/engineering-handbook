using System;
using System.Linq;
using System.Reflection;
using System.Runtime.CompilerServices;
using System.Threading.Tasks;

// Inspect compiler metadata; this does not prove the heap allocation count.
static async Task<int> ExampleAsync()
{
    await Task.CompletedTask;
    return 42;
}

Func<Task<int>> operation = ExampleAsync;
AsyncStateMachineAttribute? attribute =
    operation.Method.GetCustomAttribute<AsyncStateMachineAttribute>();

Console.WriteLine(attribute is not null &&
    typeof(IAsyncStateMachine).IsAssignableFrom(attribute.StateMachineType));
Console.WriteLine(await operation());
