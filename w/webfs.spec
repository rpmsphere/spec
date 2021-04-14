%undefine _debugsource_packages

Summary: Simple http server for mostly static content
Name: webfs
Version: 1.21
Release: 4.1
License: GPL-2.0
Source0:  %{name}-%{version}.tar.gz
URL: http://linux.bytesex.org/misc/webfs.html
Group: System Environment/Daemons

%description
Webfs is a simple http server for mostly static content. You can use it to
serve the content of a ftp server via http for example. It is also nice to
export some files the quick way by starting a http server in a few seconds,
without editing some config file first.

It uses sendfile() and knows how to use sendfile on linux and FreeBSD.
Adding other systems should'nt be difficuilt. There is some sendfile emulation
code which uses read()+write() and a userland bounce buffer, this allows to
compile and use webfs on systems without sendfile() too. Recent versions also
got limited CGI support (GET requests only) and optional SSL support.

%prep
%setup -q

%build
make 

%install
make prefix=$RPM_BUILD_ROOT%{_prefix} install 

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Feb 10 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.21
- Rebuilt for Fedora
