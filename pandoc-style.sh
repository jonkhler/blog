#!/bin/sh
style=${1:-breezedark}
tmp=
trap 'rm -f "$tmp"' EXIT
tmp=$(mktemp)
echo '$highlighting-css$' > "$tmp"
echo '`test`{.c}' | pandoc --highlight-style ./my.theme --template=$tmp