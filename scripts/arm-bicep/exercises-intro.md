# ARM Templates with Bicep - Exercises Introduction

We've covered Bicep as the modern evolution of ARM templates with cleaner syntax. Now let's deploy infrastructure using Bicep's more maintainable approach.

## What You'll Do

You'll start by **deploying a simple Bicep template for a storage account**. Bicep templates have interactive parameter prompts (nice for learning) and command-line parameter options (better for automation). The syntax is immediately more readable than JSON - no more curly braces everywhere!

Then you'll use **what-if analysis to preview changes** when modifying resource properties. This is identical to JSON ARM templates functionally, but the Bicep source is easier to read and edit. You'll see how changing a property in Bicep shows up in the what-if diff.

Next comes the really interesting part: you'll **install Bicep CLI and decompile a complex JSON ARM template** for a Linux VM into Bicep format. Watch as 200+ lines of verbose JSON become much more concise, readable Bicep code. The decompiled code includes warnings about potential issues - Bicep's compiler is smarter about detecting problems.

You'll **edit the generated Bicep file** to fix warnings and implement static IP allocation (addressing the idempotency issue from the JSON version). This demonstrates Bicep's advantage: it's easier to understand and modify than JSON.

Finally, you'll practice **incremental deployment by adding SQL Server resources** to existing VM infrastructure. The Bicep file describes both old and new resources together. When you deploy, Azure recognizes which resources already exist (no changes) and creates only the new SQL Server components. This is incremental mode in action - adding to existing infrastructure without recreating everything.

Let's deploy infrastructure with modern Bicep syntax!
