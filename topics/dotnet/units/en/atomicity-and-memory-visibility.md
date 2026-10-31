# Atomicity, volatile and Interlocked

[Русский](../atomicity-and-memory-visibility.md) · [English](atomicity-and-memory-visibility.md)

[Home](../../../../README.en.md) · [Module](../../en/shared-memory.md) · [All units](README.md) · [Learning app](https://itprodavets.github.io/engineering-handbook/#/en/unit/atomicity-and-memory-visibility)

> Understand read-modify-write and memory visibility.

## Definition

counter++ is a read/modify/write sequence, not a guaranteed atomic operation. volatile controls certain access/ordering semantics but does not make ++ atomic. Interlocked.Increment atomically changes one variable.

## Internal mechanics

1. Roslyn emits reads and writes for ++; their ordering can interleave across workers.
2. Two threads can read the same old value and overwrite one another: a lost update.
3. Interlocked performs atomic read-modify-write for one memory location.
4. For multi-field invariants, use synchronization such as a shared lock.

## Resources

Shared memory and cache coherence; atomic instructions may contend between cores.

## Pitfalls and constraints

volatile does not fix counter++; the number of scheduled Tasks does not determine the final counter value.

## Example

```csharp
int counter = 0;
Interlocked.Increment(ref counter);
```

## Review questions

- [Q-021: Why is volatile counter++ unsafe, and how do Interlocked.Increment and lock differ?](../../../../questions/dotnet/en/Q-021-volatile-vs-interlocked.md)
- [Q-028: Is counter always 10,000? Why or why not?](../../../../questions/dotnet/en/Q-028-lost-update-race.md)

## References

- [https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked](https://learn.microsoft.com/en-us/dotnet/api/system.threading.interlocked)

---

[Next →](mutual-exclusion-and-semaphores.md) · [Русский](../atomicity-and-memory-visibility.md) · [English](atomicity-and-memory-visibility.md)
