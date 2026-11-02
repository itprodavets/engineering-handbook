using System;
using System.Collections.Generic;

// Sequential in-memory illustration. Real providers must deduplicate atomically and durably.
var withoutKey = new FakeProvider();
withoutKey.Charge(null);
withoutKey.Charge(null); // replay after a hypothetical lost response
var withKey = new FakeProvider();
withKey.Charge("order-7:attempt-1");
withKey.Charge("order-7:attempt-1"); // same logical charge
Console.WriteLine($"WithoutKeyCharges={withoutKey.Charges}; WithSameKeyCharges={withKey.Charges}");

sealed class FakeProvider
{
    private readonly HashSet<string> _keys = new();
    public int Charges { get; private set; }
    public void Charge(string? key)
    {
        if (key is not null && !_keys.Add(key)) return;
        Charges++;
    }
}
