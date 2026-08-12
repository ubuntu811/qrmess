# qrmess

A little chaos producer.

Feed it a text file full of random nonsense plus one actual coupon (or
whatever the real prize is). It turns every line into a QR code and lays
them all out on a printable PDF. Print them on sticky labels, plaster them
all over an otherwise boring present, and hand it to a workmate.

Watch them stand there scanning code after code with their phone, reading
out translated nonsense in front of everyone, until they finally stumble
onto the one that actually matters.

I never said I'm not nasty :D:D:D

## How it works

- Reads lines from `stuff.txt` (or from stdin, if you pipe something in)
- Shuffles them
- Renders each line as a QR code image (`img/<n>.png`)
- Arranges the codes in a grid on a landscape A4 PDF (`doc.pdf`)

## Requirements

```bash
pip install qrcode fpdf2
```

## Usage

Edit `stuff.txt` with your own nonsense lines and hide your real
message/link/coupon among them, then run:

```bash
./qrmess.py
```

or pipe in your own list:

```bash
cat mylines.txt | ./qrmess.py
```

Make sure an `img/` directory exists (it's gitignored) — the script writes
one PNG per line there before assembling `doc.pdf`.

Print `doc.pdf` on sticky paper, cut out the codes, and go decorate.
