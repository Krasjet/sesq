sesq
====

<p align="center">
  <img width=480 src="https://krasjet.com/voice/sesq/imgs/palette.svg">
</p>

sesq is an adaptable **sesquichromatic** syntax highlighting color scheme for
[Pygments][pygments], designed to be used on web pages (instead of in editors),
in particular to match the styles of [karasu][karasu] and my maze.

Due to the limitations of the medium, please see [**here**][sesq] for detailed
introduction.

<p align="center">
  <img width=700 src="https://krasjet.com/voice/sesq/imgs/screenshot.png">
</p>

Usage
-----

```
sesq.py:
  Pygments definitions
syntax.css:
  CSS files generated by Pygments
pandoc.css:
  Manually crafted version for Pandoc, used when Pygments is not available.
  Skylighting's lexers are not very good, so use with caution.
```

Note that `italic` in the color theme definition means "medium" weight, not
actual italics. Pygments only support one font weight, so I have to use a hack.

License
-------

sesq is licensed under [CC BY-NC 4.0][cc] license.

[pygments]: https://pygments.org/
[karasu]: https://krasjet.com/voice/karasu/
[sesq]: https://krasjet.com/voice/sesq/
[cc]: https://creativecommons.org/licenses/by-nc/4.0/
