# revision 17049
# category Package
# catalog-ctan /macros/latex/contrib/anonchap
# catalog-date 2010-02-23 16:03:07 +0100
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-anonchap
Version:	1.1a
Release:	1
Summary:	Make chapters be typeset like sections
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anonchap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonchap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anonchap.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The command \simplechapter sets up the \chapter command not to
number chapters, though they may possibly have a prefix, and a
suffix (the \simplechapterdelim command, which the user may
alter). The \restorechapter command restores the status quo
ante.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/anonchap/anonchap.sty
%doc %{_texmfdistdir}/doc/latex/anonchap/anonchap.pdf
%doc %{_texmfdistdir}/doc/latex/anonchap/anonchap.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
