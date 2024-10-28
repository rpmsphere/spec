%undefine _debugsource_packages

Summary:        WPS brute force attack
Name:           bully
Version:        1.1git
Release:        1
License:        GPLv3+
Group:          Networking/Other
URL:            https://github.com/aanarchyy/bully
Source0:        %{name}-master.zip
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig(openssl)

%description
Bully is a new implementation of the WPS brute force attack, written in C.
It is conceptually identical to other programs, in that it exploits the
(now well known) design flaw in the WPS specification. It has several
advantages over the original reaver code. These include fewer dependencies,
improved memory and cpu performance, correct handling of endianness, and a
more robust set of options. It runs on Linux, and was specifically developed
to run on embedded Linux systems (OpenWrt, etc) regardless of architecture.

%prep
%setup -q -n %{name}-master

%build
%make_build -C src prefix=/usr

%install
%make_install -C src prefix=/usr

%files
%doc *.md
%{_bindir}/%{name}

%changelog
* Tue Dec 10 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1git
- Rebuilt for Fedora
* Sun Feb 17 2019 abfonly <abfonly@gmail.com> 1.1-1
- (16bf86e) Imported from SRPM
