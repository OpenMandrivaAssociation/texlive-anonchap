%global tl_name anonchap
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Make chapters be typeset like sections
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/anonchap
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anonchap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anonchap.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The command \simplechapter sets up the \chapter command not to number
chapters, though they may possibly have a prefix, and a suffix (the
\simplechapterdelim command, which the user may alter). The
\restorechapter command restores the status quo ante.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/anonchap
%dir %{_datadir}/texmf-dist/tex/latex/anonchap
%doc %{_datadir}/texmf-dist/doc/latex/anonchap/README.md
%doc %{_datadir}/texmf-dist/doc/latex/anonchap/anonchap.pdf
%doc %{_datadir}/texmf-dist/doc/latex/anonchap/anonchap.tex
%{_datadir}/texmf-dist/tex/latex/anonchap/anonchap.sty
