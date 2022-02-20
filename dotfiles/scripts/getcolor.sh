# usage: ./getcolor.sh <image-URI>
curl -s $1 > /tmp/image.png
convert /tmp/image.png -colorspace RGB -format %c histogram:info:- | sort -nr | \
    grep -v -e '#000000' -e '#FFFFFF' | \
    sed -n 3p | \
    grep -Eo '#[A-F0-9]*'
rm /tmp/image.png
