import sys
import os
import stat

# TODO : some console messages
main_content = r"""
\documentclass[13pt,a4paper]{scrartcl}
\usepackage[utf8]{inputenc}
\usepackage[english,russian]{babel}
\usepackage{indentfirst}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{listings}
\usepackage{array}
\usepackage{import}

% Некоторые множества

\def\Q{\mathbb{Q}}
\def\Z{\mathbb{Z}}
\def\N{\mathbb{N}}
\def\R{\mathbb{R}}
\def\C{\mathbb{C}}

% Бинарные операции над множествами

% xor
\def\xor{\oplus}
% объединение
\def\u{\cup}
% объединение
\def\i{\cap}


% Комбинаторика

% Биномиальный коэффициент : (из n  по k)
\def\set{\binom}
% ((из n по k))
\def\mset#1#2{\ensuremath{\left(\kern-.3em\left(\genfrac{}{}{0pt}{}{#1}{#2}\right)\kern-.3em\right)}}


% Опеации над несколькими множествами

% Сумма
\def\suml{\sum\limits}
\def\sumfor#1#2#3{\suml_{{#1}={#2}}^{#3}}
\def\sumi#1#2{\sumfor{#1}{#2}{\inf}}
\def\sumin#1#2{\suml_{{#1} \in {#2}}}

% Перемножение (знак П)
\def\mul{\prod}
\def\mull{\mul\limits}
\def\muli#1#2{\mull{#1}{#2}{\inf}}
\def\mulin#1#2{\mul\limits_{{#1} \in {#2}}}

% Объединение
\def\U{\bigcup}
\def\Ul#1#2#3{\U\limits_{{#1}={#2}}^{#3}}
\def\Ui#1#2{\Ul{#1}{#2}{\inf}}
\def\Uin#1#2{\U\limits_{{#1} \in {#2}}}

% Пересечение
\def\I{\bigcap}
\def\Il#1#2#3{\I\limits_{{#1}={#2}}^{#3}}
\def\Ii#1#2{\Il{#1}{#2}{\inf}}
\def\Iin#1#2{\I\limits_{{#1} \in {#2}}}


% Разделители

\def\ms{\medskip}
\def\bs{\bigskip}


% Греческий алфавит

\def\a{\alpha}
\def\b{\beta}
\def\g{\gamma}
\def\l{\lambda}
\def\e{\varepsilon}
\def\eps{\varepsilon}
\def\d{\delta}
\def\m{\mu}
\def\p{\phi}

\def\L{\Lambda}
\def\D{\Delta}
\def\M{\Mu}
\def\P{\Phi}


% Кванторы

\def\A{\forall}
\def\E{\exists\;}


% Что-то еще

\def\inf{\t{+}\infty}    % +inf
\def\O{\mathcal{O}}      %
\def\t{\text}
\def\bs{\textbackslash{}}

\begin{document}

\end{document}
"""

compile = r"""
!#/bin/bash

#compile hw into tex
mkdir build
cd raw
for item in *.hw; do
    python3 "../../../converter/convert.py" $item
done

cd ../

#compile whole conspect
pdflatex #PROJECT_NAME#.tex
open #PROJECT_NAME#.pdf
"""

def main():
	project_name = sys.argv[1]
	os.makedirs(project_name)

	path_to_raw = os.path.join(project_name, "raw")
	os.makedirs(path_to_raw)

	path_to_compile = os.path.join(project_name, "compile.sh")
	with open(path_to_compile, 'w') as file:
		file.write(compile.replace("#PROJECT_NAME#", project_name))
	st = os.stat(path_to_compile)
	os.chmod(path_to_compile, st.st_mode | stat.S_IEXEC)

	path_to_tex = os.path.join(project_name, project_name + ".tex")
	with open(path_to_tex, 'w') as file:
		file.write(main_content)

if __name__ == "__main__":
    main()