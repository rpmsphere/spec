%global debug_package %{nil}
%global _name musl

Summary: A small, embeddable BASIC interpreter in C
Name: muslbasic
Version: 0.1234
Release: 4.1
License: Public Domain
Group: Development/Languages
Source: %{_name}-master.zip
URL: https://github.com/wernsey/musl

%description
My Unstructured Scripting Language is my own small BASIC interpreter.

%prep
%setup -q -n %{_name}-master
sed -i 's|-s ||' Makefile

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{_name} %{buildroot}%{_bindir}/%{name}

%files 
%doc *.md manual.html
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Sep 11 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1234
- Rebuild for Fedora
