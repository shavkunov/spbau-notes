!#/bin/bash

#compile hw into tex
mkdir build
cd raw
for item in *.hw; do
    python3 "../../../converter/convert-db.py" $item
done

cd ../

#compile whole conspect
pdflatex -shell-escape main.tex
pdflatex -shell-escape main.tex
pdflatex -shell-escape main.tex