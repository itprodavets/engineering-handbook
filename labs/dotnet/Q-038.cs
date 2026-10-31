using System;
using System.Threading;

// Deterministic inline-callback simulation, NOT a guarantee about a real socket.
IAsyncResult? captured = null;
captured = BeginInline(ar =>
    Console.WriteLine($"CapturedIsNull={captured is null}; CallbackHasResult={ar is not null}"));

static IAsyncResult BeginInline(AsyncCallback callback)
{
    IAsyncResult completed = new CompletedResult();
    callback(completed);
    return completed;
}

sealed class CompletedResult : IAsyncResult
{
    public object? AsyncState => null;
    public WaitHandle AsyncWaitHandle => throw new NotSupportedException();
    public bool CompletedSynchronously => true;
    public bool IsCompleted => true;
}
