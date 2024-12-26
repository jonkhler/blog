## starting a blog

Following [the request](https://bsky.app/profile/imtd.bsky.social/post/3ldr7e5ge722x) of my close friend [Tim](https://www.trdavidson.com), I turned my [old researcher CV website](https://argmin.xyz/_old) into a blog to write about some stuff that I find interesting and worth to share with others.

While I cannot fully anticipate what this will be exactly, I expect it to around:

- mathematical curiosities
- coding stuff
- intros to some stuff in machine learning for the sciences

### the setup of this blog

To begin with something technical let me lay out the design principles:

- all writing must be in markdown - [one file per entry](https://github.com/jonkhler/blog/tree/main/entries).
- all state must be maintained in [GitHub](https://github.com/jonkhler/blog/)
- [building](https://github.com/jonkhler/blog/tree/main/Makefile) is done with [pandoc](https://pandoc.org/)
- anything blogspecific that goes beyond vanilla markdown is implemented in some [preprocessor script](https://github.com/jonkhler/blog/tree/main/mdcat.py):
    - nested including of other markdown files via `@include path/to/other/file`
    - adding adding timestamps to blog posts
    - maybe further features (adding social links etc.)

I do not know if and how I will integrate a comment/discussion section. Maybe I can maintain that via Bluesky? So far GitHub issues will do the job :).
