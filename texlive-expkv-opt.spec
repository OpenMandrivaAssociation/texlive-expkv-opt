Name:		texlive-expkv-opt
Version:	58772
Release:	1
Summary:	Parse class and package options with expkv
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/expkv-opt
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-opt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-opt.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/expkv-opt.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides option parsing for classes and packages
in LaTeX2e based on expkv. Global and local options are parsed
individually by different commands. The package supports
key=value options and keys without a value. expkv is the only
required package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/expkv-opt
%{_texmfdistdir}/tex/generic/expkv-opt
%doc %{_texmfdistdir}/doc/generic/expkv-opt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
