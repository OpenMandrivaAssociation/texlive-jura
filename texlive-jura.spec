# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/jura
# catalog-date 2007-01-08 14:12:54 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-jura
Version:	20070108
Release:	1
Summary:	A document class for German legal texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jura
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jura.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jura.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jura.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Implements the standard layout for German term papers in law
(one-and-half linespacing, 7 cm margins, etc.). Includes
alphanum that permits alphanumeric section numbering (e.g., A.
Introduction; III. International Law).

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
%{_texmfdistdir}/tex/latex/jura/alphanum.sty
%{_texmfdistdir}/tex/latex/jura/jura.cls
%doc %{_texmfdistdir}/doc/latex/jura/README
%doc %{_texmfdistdir}/doc/latex/jura/jura.pdf
%doc %{_texmfdistdir}/doc/latex/jura/jura2html
%doc %{_texmfdistdir}/doc/latex/jura/juratest.ltx
#- source
%doc %{_texmfdistdir}/source/latex/jura/jura.dtx
%doc %{_texmfdistdir}/source/latex/jura/jura.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
