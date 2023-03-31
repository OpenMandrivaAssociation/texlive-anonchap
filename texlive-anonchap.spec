Name:		texlive-anonchap
Version:	17049
Release:	2
Summary:	Make chapters be typeset like sections
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anonchap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonchap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonchap.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The command \simplechapter sets up the \chapter command not to
number chapters, though they may possibly have a prefix, and a
suffix (the \simplechapterdelim command, which the user may
alter). The \restorechapter command restores the status quo
ante.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/anonchap/anonchap.sty
%doc %{_texmfdistdir}/doc/latex/anonchap/anonchap.pdf
%doc %{_texmfdistdir}/doc/latex/anonchap/anonchap.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
