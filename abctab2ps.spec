%global debug_package %{nil}

Name: abctab2ps
Summary: A music and tablature typesetting program
Version: 1.8.12
Release: 3.1
Group: Applications
License: GPL
URL: http://www.lautengesellschaft.de/cdmm/
Source0: http://www.lautengesellschaft.de/cdmm/%{name}-%{version}.tar.gz

%description
A music and tablature typesetting program based on
Chris Walshaw's abc music language. abctab2ps converts
abc files directly into postscript without the need
of additional software.
In addition to the abc standard which only supports
music, abctab2ps supports lute and guitar tablature.
1999-2011 by Christoph Dalitz, based upon code by Michael Methfessel

%prep
%setup -q
sed -i -e 's|/man/|/share/man/|' -e 's|/usr/local|%{buildroot}/usr|' src/Makefile

%build
cd src
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/bin
cd src
%makeinstall

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.12
- Rebuild for Fedora
