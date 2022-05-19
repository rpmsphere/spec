%undefine _debugsource_packages

Summary: A new Unix shell
Name: oil
Version: 0.9.9
Release: 1
License: Apache
Group: Development/Language
URL: https://www.oilshell.org/
Source0: https://www.oilshell.org/download/%{name}-%{version}.tar.gz

%description
Oil is our upgrade path from bash to a better language and runtime.
It's also for Python and JavaScript users who avoid shell!

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
%make_install

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc *.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sun Apr 24 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.9
- Rebuilt for Fedora
