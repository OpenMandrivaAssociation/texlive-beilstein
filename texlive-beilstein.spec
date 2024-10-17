Name:		texlive-beilstein
Version:	56193
Release:	2
Summary:	Support for submissions to the "Beilstein Journal of Nanotechnology"
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beilstein
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beilstein.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beilstein.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beilstein.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a LaTeX class file and a BibTeX style file
in accordance with the requirements of submissions to the
``Beilstein Journal of Nanotechnology''. Although the files can
be used for any kind of document, they have only been designed
and tested to be suitable for submissions to the Beilstein
Journal of Nanotechnology.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/beilstein
%{_texmfdistdir}/tex/latex/beilstein
%{_texmfdistdir}/bibtex/bst/beilstein
%doc %{_texmfdistdir}/doc/latex/beilstein

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
