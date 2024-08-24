At its core, Planet is a static site generator. However, unlike other static site generators like Jekyll, Planet is designed to be used with a graphical interface from the start.

I love Jekyll and Zola; both are exciting and inspiring software. But as I use them more, I feel friction at every step when I just want to write and publish something. I need to name a file, remember and use the correct metadata syntax, write a git message, push it to GitHub, and wait for a moment for the static site to build and publish. Installing Jekyll on a new computer is also a challenge, often requiring up-to-date Ruby and dependency instructions, which can be time-consuming.

So, when I started working on Planet, I aimed to reduce those frictions:

- Installation should be simple—just like a regular macOS app; you drag it into Applications, and it's done.
- Write with a live preview Markdown editor; no need to set a file name, use git or any command line, or sign up for an account.
- You just write, and the app generates a static site for you.
- A built-in IPFS node can easily publish the site with a shareable IPNS name, so you don't even need a server or cloud (which is essentially just someone else's computer).