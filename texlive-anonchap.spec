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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The command \simplechapter sets up the \chapter command not to number
chapters, though they may possibly have a prefix, and a suffix (the
\simplechapterdelim command, which the user may alter). The
\restorechapter command restores the status quo ante.

