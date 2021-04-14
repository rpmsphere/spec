%undefine _debugsource_packages

Summary: Gravity Programming Language
Name: gravity
Version: 0.8.1
Release: 1
License: MIT
Group: Development/Languages
Source: https://github.com/marcobambini/gravity/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/marcobambini/gravity

%description
Gravity is a powerful, dynamically typed, lightweight, embeddable programming
language written in C without any external dependencies (except for stdlib).
It is a class-based concurrent scripting language with modern Swift-like syntax.

%prep
%setup -q

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files 
%doc README.md LICENSE CONTRIBUTORS
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.1
- Rebuilt for Fedora
