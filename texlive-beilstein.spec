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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a LaTeX class file and a BibTeX style file in
accordance with the requirements of submissions to the ``Beilstein
Journal of Nanotechnology''. Although the files can be used for any kind
of document, they have only been designed and tested to be suitable for
submissions to the Beilstein Journal of Nanotechnology.

