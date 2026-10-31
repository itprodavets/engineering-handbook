using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

// Real local TCP I/O; no PostgreSQL dependency. Scheduling is non-deterministic.
using var listener = new TcpListener(IPAddress.Loopback, 0);
listener.Start();
int port = ((IPEndPoint)listener.LocalEndpoint).Port;

Task server = Task.Run(async () =>
{
    using var peer = await listener.AcceptTcpClientAsync();
    using NetworkStream stream = peer.GetStream();
    await Task.Delay(40); // Force a pending client receive.
    await stream.WriteAsync("READY"u8.ToArray());
});

using var client = new TcpClient();
await client.ConnectAsync(IPAddress.Loopback, port);
using NetworkStream reader = client.GetStream();

byte[] data = new byte[5];
int count = 0;
while (count < data.Length)
{
    int read = await reader.ReadAsync(data.AsMemory(count));
    if (read == 0) throw new InvalidOperationException("Socket closed early");
    count += read;
}
await server;
listener.Stop();
Console.WriteLine(Encoding.UTF8.GetString(data));
