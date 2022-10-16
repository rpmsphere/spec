%undefine _debugsource_packages

Summary: A programming language
Name: perfume
Version: 1.6.2
Release: 1
License: MIT
Group: Development/Languages
Source0: https://github.com/mitchan0321/perfume/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL: https://github.com/mitchan0321/perfume
BuildRequires: libpcl-devel
BuildRequires: onigmo-devel

%description
A programming language Perfume and a text editor Pmacs writen by Perfume.

%prep
%setup -q
sed -i -e 's|PREFIX.*= |PREFIX = %{buildroot}|' -e 's|/usr/local|/usr|' -e 's|mkdir|mkdir -p|' Makefile
#sed -i -e 's|/usr/lib|/usr/lib64|' -e 's|$(PREFIX)/lib|$(PREFIX)/lib64|' Makefile

%build
#export CFLAGS=-fPIE
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install
#install -d %{buildroot}%{_bindir}
#install -m755 *-linux-build/%{name}* *-linux-build/stategraph %{buildroot}%{_bindir}
#install -d %{buildroot}%{_includedir}/%{name}
#install -m644 include/* %{buildroot}%{_includedir}/%{name}

%files 
%doc README RELEASE COPYING
%{_bindir}/*
/usr/lib/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.2
- Rebuilt for Fedora
