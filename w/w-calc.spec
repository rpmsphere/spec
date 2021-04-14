Summary: A flexible command-line calculator
Name: w-calc
Version: 2.5
Release: 4.1
Group: Office
License: GPL
URL: https://sourceforge.net/projects/w-calc
Source: https://sourceforge.net/projects/w-calc/files/Wcalc/%{version}/wcalc-%{version}.tar.bz2
BuildRequires: flex flex-static
BuildRequires: bison
BuildRequires: readline-devel 
BuildRequires: gmp-devel 
BuildRequires: mpfr-devel

%description
W-calc is a command-line calculator designed to accept all valid mathematical
expressions. It supports all standard mathematical operations, parenthesis,
brackets, braces, trigonometric functions, hyperbolic trig functions, logs,
and most boolean operators.

%prep
%setup -q -n wcalc-%{version}

%build
%configure
make CFLAGS+=-Wno-format-security

%install
rm -rf ${RPM_BUILD_ROOT}
%makeinstall
mv %{buildroot}%{_bindir}/wcalc %{buildroot}%{_bindir}/w-calc
mv %{buildroot}%{_mandir}/man1/wcalc.1 %{buildroot}%{_mandir}/man1/w-calc.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog NEWS README COPYRIGHT AUTHORS
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Dec 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
* Tue Jun 07 2010 slick50 <lxgator@gmail.com> 2.4-1pclos2010
- initial pkg
