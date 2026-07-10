%global tl_name beilstein
%global tl_revision 56193

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	Support for submissions to the Beilstein Journal of Nanotechnology
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beilstein
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beilstein.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beilstein.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beilstein.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a LaTeX class file and a BibTeX style file in
accordance with the requirements of submissions to the ``Beilstein
Journal of Nanotechnology''. Although the files can be used for any kind
of document, they have only been designed and tested to be suitable for
submissions to the Beilstein Journal of Nanotechnology.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/beilstein
%dir %{_datadir}/texmf-dist/doc/latex/beilstein
%dir %{_datadir}/texmf-dist/source/latex/beilstein
%dir %{_datadir}/texmf-dist/tex/latex/beilstein
%{_datadir}/texmf-dist/bibtex/bst/beilstein/bjnano.bst
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/BJNANO_Technical_Handbook.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/beilstein-template.bib
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/beilstein-template.tex
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/figure1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/scheme1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beilstein/scheme2.pdf
%doc %{_datadir}/texmf-dist/source/latex/beilstein/beilstein.dtx
%doc %{_datadir}/texmf-dist/source/latex/beilstein/beilstein.ins
%doc %{_datadir}/texmf-dist/source/latex/beilstein/bjnano_logo.pdf
%{_datadir}/texmf-dist/tex/latex/beilstein/beilstein.cls
