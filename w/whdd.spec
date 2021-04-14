%undefine _debugsource_packages

Summary:	Diagnostic and recovery tool for block devices
Name:		whdd
Version:	2.2
Release:	7.1
License:	GPLv1+
Group:		System/Kernel and hardware
URL:		https://github.com/whdd/whdd
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	dialog-devel
BuildRequires:	pkgconfig(ncurses)

%description
WHDD is a diagnostic and recovery tool for block devices
(near to replace MHDD for Linux).

%prep
%setup -q

%build
%cmake -DCFLAGS=-fPIC -DDIALOG_INCLUDE_DIR=/usr/include/dialog
make

%install
%make_install

%files
%{_sbindir}/*

%changelog
* Tue Aug 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
* Mon May 09 2016 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.2-0.11_ge88b96e1.2
- (2190c8f) Don't override system optflags
