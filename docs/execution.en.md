# Running C# examples

[Русский](execution.md) · [English](execution.en.md)

[Home](../README.en.md) · [Labs](../labs/README.en.md) · [Interactive practice](https://itprodavets.github.io/engineering-handbook/#/en/practice)

GitHub Pages does not execute C#. The learning site lets you predict output, check it against a model answer, edit the code, and copy it. **Checking a prediction is not program execution.**

## GitHub Codespaces

[Open Codespaces](https://codespaces.new/itprodavets/engineering-handbook), create a cloud environment, and run this command:

```bash
dotnet run --file labs/dotnet/Q-024.cs
```

To run an edited snippet, click **Copy code** on the website, paste it into the matching `labs/dotnet/Q-###.cs` file in Codespaces, and execute it there. The environment uses the .NET 10 SDK.

## GitHub Actions

Open [Run one lab](https://github.com/itprodavets/engineering-handbook/actions/workflows/run-lab.yml) → **Run workflow** → select Q-024–Q-035. Output appears in the job logs and Job Summary. **Actions runs the committed code, not unsaved edits in Pages.**

## Local execution

With the .NET 10 SDK installed, run the same command at the repository root. Concurrent examples may produce nondeterministic results; one successful run does not prove a race condition is absent.

## Pages publication

Publishing GitHub Pages from a private repository requires an eligible GitHub plan. Select Settings → Pages → Source → GitHub Actions. **The published website can be publicly accessible even if the repository remains private.** No personal answers, scores, or secrets are published.

[GitHub Pages docs](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) · [.NET 10 file-based apps](https://learn.microsoft.com/en-us/dotnet/core/sdk/file-based-apps)
