Name: ttyd
Summary: Share your terminal over the web
Version: 1.6.3
Release: 1
License: MIT
Group: System/Monitoring
URL: https://tsl0922.github.io/ttyd/
Source0: https://github.com/tsl0922/ttyd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: json-c-devel
BuildRequires: vim-common
BuildRequires: cmake
BuildRequires: openssl-devel
BuildRequires: libwebsockets-devel

%description
ttyd is a simple command-line tool for sharing terminal over the web, inspired by GoTTY.

%prep  
%setup -q

%build
%cmake
%cmake_build

%install
%cmake_install
  
%clean  
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README.md
%{_bindir}/ttyd
%{_mandir}/man1/ttyd.1.*

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.3
- Rebuilt for Fedora
