using System;
using System.Net;
using System.Net.Sockets;
using System.Threading.Tasks;

// Genuine loopback APM network read. Callback scheduling is intentionally not assumed.
using var listener = new TcpListener(IPAddress.Loopback, 0);
listener.Start();
int port = ((IPEndPoint)listener.LocalEndpoint).Port;
using var client = new TcpClient();
Task connecting = client.ConnectAsync(IPAddress.Loopback, port);
using TcpClient server = await listener.AcceptTcpClientAsync();
await connecting;
listener.Stop();
NetworkStream reader = client.GetStream();
byte[] buffer = new byte[1];
var finished = new TaskCompletionSource<int>(
    TaskCreationOptions.RunContinuationsAsynchronously);
reader.BeginRead(buffer, 0, buffer.Length, ar =>
{
    try { finished.TrySetResult(reader.EndRead(ar)); }
    catch (Exception error) { finished.TrySetException(error); }
}, null);
await server.GetStream().WriteAsync(new byte[] { 42 });
int count = await finished.Task.WaitAsync(TimeSpan.FromSeconds(10));
Console.WriteLine($"Read={count}; Byte={buffer[0]}");
