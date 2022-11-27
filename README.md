Check out [the excellent guest post about Scale Buddy] by visiting professor Kilgore Trout on my website.

> Sorry that crappy Docker is the only supported runtime right now.  I should have instructions to run it as a container using `systemd-nspaw` soon-ish.

## Download

```
docker pull btoll/scale_buddy:beta
```

https://hub.docker.com/r/btoll/scale_buddy

## Build

```
$ docker build -t scale_buddy:beta .
```

## Examples

```
$ docker run --init --rm scale_buddy:beta G
G major:
G  A  B  C  D  E  F♯
```

```
$ docker run --init --rm scale_buddy:beta G --with-minor
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
$ docker run --init --rm scale_buddy:beta G --with-minor --with-pentatonic
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
$ docker run --init --rm scale_buddy:beta --sharp F
F♯ major:
F♯  G♯  A♯  B  C♯  D♯  E♯
```

```
$ docker run --init --rm scale_buddy:beta --flat E
E♭ major:
E♭  F  G  A♭  B♭  C  D
```

## Testing

```
$ python -m unittest discover
```

[the excellent guest post about Scale Buddy]: https://benjamintoll.com//2022/10/26/on-scale-buddy/

