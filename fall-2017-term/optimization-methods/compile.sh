#/bin/bash

#compile hw into tex
mkdir build
cd raw
for item in *.hw; do
    python3 "../../../converter/convert.py" $item
done

cd ../

#compile whole conspect
pdflatex optimization-methods.tex
open optimization-methods.pdf
