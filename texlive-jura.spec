Name:		texlive-jura
Version:	15878
Release:	1
Summary:	A document class for German legal texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jura
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jura.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jura.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jura.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Implements the standard layout for German term papers in law
(one-and-half linespacing, 7 cm margins, etc.). Includes
alphanum that permits alphanumeric section numbering (e.g., A.
Introduction; III. International Law).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/jura/alphanum.sty
%{_texmfdistdir}/tex/latex/jura/jura.cls
%doc %{_texmfdistdir}/doc/latex/jura/README
%doc %{_texmfdistdir}/doc/latex/jura/jura.pdf
%doc %{_texmfdistdir}/doc/latex/jura/jura2html
%doc %{_texmfdistdir}/doc/latex/jura/juratest.ltx
#- source
%doc %{_texmfdistdir}/source/latex/jura/jura.dtx
%doc %{_texmfdistdir}/source/latex/jura/jura.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
