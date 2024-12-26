%undefine _debugsource_packages

Summary: A new Unix shell
Name: oils
Version: 0.23.0
Release: 1
License: Apache
Group: Development/Language
URL: https://www.oilshell.org/
Source0: https://www.oilshell.org/download/oils-for-unix-%{version}.tar.gz

%description
Oil is our upgrade path from bash to a better language and runtime.
It's also for Python and JavaScript users who avoid shell!

%prep
%setup -q -n oils-for-unix-%{version}

%build
./configure --prefix=/usr
_build/oils.sh

%install
install -Dm755 _bin/cxx-opt-sh/oils-for-unix %{buildroot}%{_bindir}/osh
ln -s osh %{buildroot}%{_bindir}/ysh
install -Dm644 doc/osh.1 %{buildroot}%{_mandir}/man1/osh.1

%files
%doc *.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 0.23.0
- Rebuilt for Fedora
