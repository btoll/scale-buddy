Check out [the excellent guest post about Scale Buddy] by visiting professor Kilgore Trout on my website.

## Installation

### Source

```
$ git clone https://github.com/btoll/scale-buddy.git
$ cd scale-buddy
$ pip3 install --editable .
```

This will install a "binary" to `$HOME/.local/bin/scale-buddy`.

If `scale-buddy` cannot be found as a command-line tool, make sure that `$HOME/.local/bin` is in your `PATH`.

> Want to know more about how the binary is installed?  Of course you do!  The Python tooling is called [`console_scripts`], and you can find a brief introduction and example [elsewhere on my website].

```
$ scale-buddy G
G major:
G  A  B  C  D  E  F♯
```

### Docker

> Sorry that crappy Docker is the only supported runtime right now.  I should have instructions to run it as a container using `systemd-nspaw` soon-ish.

#### Download

```
docker pull btoll/scale-buddy:beta
```

https://hub.docker.com/r/btoll/scale-buddy

#### Build

```
$ docker build -t scale-buddy:beta .
```

#### Examples

```
$ docker run --init --rm scale-buddy:beta G
G major:
G  A  B  C  D  E  F♯
```

```
$ docker run --init --rm scale-buddy:beta G --with-minor
G major:
G  A  B  C  D  E  F♯

G natural minor (Aeolian):
G  A  B♭  C  D  E♭  F

G harmonic minor:
G  A  B♭  C  D  E♭  F♯

G melodic minor:
G  A  B♭  C  D  E  F♯
```

```
$ docker run --init --rm scale-buddy:beta G --with-minor --with-pentatonic
G major:
G  A  B  C  D  E  F♯

G natural minor (Aeolian):
G  A  B♭  C  D  E♭  F

G harmonic minor:
G  A  B♭  C  D  E♭  F♯

G melodic minor:
G  A  B♭  C  D  E  F♯

G major pentatonic:
G    A    B    D    E

G minor pentatonic scale:
G    B♭    C    D    F
```

For sharps and flats, there are the `--sharp` and `--flat` switches, respectively:

```
$ docker run --init --rm scale-buddy:beta --sharp F
F♯ major:
F♯  G♯  A♯  B  C♯  D♯  E♯
```

```
$ docker run --init --rm scale-buddy:beta --flat E
E♭ major:
E♭  F  G  A♭  B♭  C  D
```

## Testing

```
$ python -m unittest discover
```

## References

- [On Python `entry_points`](https://benjamintoll.com/2021/04/04/on-python-entry_points/)

[the excellent guest post about Scale Buddy]: https://benjamintoll.com//2022/10/26/on-scale-buddy/
[`console_scripts`]: https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
[elsewhere on my website]: https://benjamintoll.com/2021/04/04/on-python-entry_points/#console_scripts

