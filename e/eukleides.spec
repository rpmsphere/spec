%undefine _debugsource_packages

Summary:	A computer language devoted to elementary plane geometry
Name:		eukleides
Version:	1.5.4
Release:	22.1
License:	GPL v3
Group:		Applications/Science
Source0:	https://www.eukleides.org/files/%{name}-%{version}.tar.bz2
Patch0:		%{name}-config.patch
Patch1:		%{name}-makefile-destdir.patch
URL:		https://www.eukleides.org/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	perl
BuildRequires:	readline-devel
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo-tex
BuildRequires:	texlive-latex

%description
Eukleides is a computer language devoted to elementary plane geometry.
It aims to be a fairly comprehensive system to create geometric
figures, either static or dynamic. Eukleides allows to handle basic
types of data: numbers and strings, as well as geometric types of
data: points, vectors, sets (of points), lines, circles and conics.

%package -n texlive-latex-eukleides
Summary:	Eukleides LaTeX style
Group:		Applications/Publishing/TeX

%description -n texlive-latex-eukleides
Eukleides LaTeX style.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i "s,ginstall-info,install-info,g" doc/Makefile
sed -i "9,14d" doc/eukleides.texi
sed -i "s|-lm|-lm -Wl,--allow-multiple-definition|" build/Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README doc/*.pdf doc/manual
%{_datadir}/doc/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/%{name}.info*
%exclude %{_infodir}/dir

%files -n texlive-latex-eukleides
%dir %{_datadir}/texmf-dist/tex/latex/eukleides
%{_datadir}/texmf-dist/tex/latex/eukleides/*

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.4
- Rebuilt for Fedora
* Wed Feb 02 2011 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.3  2011/02/02 15:11:04  sparky
- do not assume compressed info files
Revision 1.2  2010/01/24 19:12:22  sparky
- BR: flex, readline-devel
Revision 1.1  2010/01/24 18:52:40  uzsolt
- initial
