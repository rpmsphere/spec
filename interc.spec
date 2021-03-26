%global debug_package %{nil}

Summary:	A tiny "pseudo C" interpreter
Name:		interc
Version:	20120304
Release:	6.1
License:	opensource
Group:		Development/C
URL:		https://github.com/frenchduff/inter_c
Source0:	frenchduff-inter_c-77059b6.tar.gz
BuildRequires: flex-static

%description
A tiny "pseudo C" interpreter.

%prep
%setup -q -n frenchduff-inter_c-77059b6
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 interpreter $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README doc/*
%{_bindir}/%{name}

%changelog
* Mon Aug 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20120304
- Rebuild for Fedora
