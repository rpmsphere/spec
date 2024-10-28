%undefine _debugsource_packages

Summary: An Interpreted language
Name: lily
Version: 2.0
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/fascinatedbox/lily
Source0: https://github.com/FascinatedBox/lily/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Lily is a programming language focused on expressiveness and type safety.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make

%install
%make_install
mv %{buildroot}/usr/lib %{buildroot}%{_libdir}

%files
%doc *.txt *.md
%{_bindir}/%{name}
%{_includedir}/*
%{_libdir}/lib*

%changelog
* Sun Apr 24 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
