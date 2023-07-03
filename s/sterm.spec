Name: sterm
Summary: Serial Terminal for Linux
Version: 0.6
Release: 9.1
Group: Applications/Communications
License: MIT
URL: https://sterm.sourceforge.net/
Source0: https://sourceforge.net/projects/sterm/files/%{name}-%{version}.tar.gz
Source1: scroll.h
BuildRequires: readline-devel, lua-devel

%description
STerm intended for embedded developers and system administrators,
intended to replace minicom.

%prep
%setup -q
cp %{SOURCE1} .

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
