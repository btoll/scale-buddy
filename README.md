# `scale-buddy`

Check out [the excellent guest post about Scale Buddy] by visiting professor Kilgore Trout on my website.

## Installation

### Source

```bash
$ go install github.com/btoll/scale-buddy
```

If `scale-buddy` cannot be found as a command-line tool, make sure that `$GOBIN` is in your `PATH`.

```bash
$ scale-buddy G
G major:
G  A  B  C  D  E  F♯
```

### Podman

```bash
$ podman pull docker.io/btoll/scale-buddy:beta
```

```bash
$ export docker=podman
```

### Docker

```bash
$ docker pull btoll/scale-buddy:beta
```

#### Examples

```bash
$ podman run --init --rm scale-buddy:beta G
G major:
G  A  B  C  D  E  F♯
```

```bash
$ podman run --init --rm scale-buddy:beta G --with-minor
G major:
G  A  B  C  D  E  F♯

G natural minor (Aeolian):
G  A  B♭  C  D  E♭  F

G harmonic minor:
G  A  B♭  C  D  E♭  F♯

G melodic minor:
G  A  B♭  C  D  E  F♯
```

```bash
$ podman run --init --rm scale-buddy:beta G --with-minor --with-pentatonic
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

```bash
$ podman run --init --rm scale-buddy:beta --sharp F
F♯ major:
F♯  G♯  A♯  B  C♯  D♯  E♯
```

```bash
$ podman run --init --rm scale-buddy:beta --flat E
E♭ major:
E♭  F  G  A♭  B♭  C  D
```

## Testing

```bash
$ ginkgo scales/...
```

## Ports

- [Python](https://github.com/btoll/py-scale-buddy)

## References

- [`scale-buddy`](https://hub.docker.com/r/btoll/scale-buddy)

[the excellent guest post about Scale Buddy]: https://benjamintoll.com//2022/10/26/on-scale-buddy/

