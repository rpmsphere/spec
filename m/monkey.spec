Name: monkey
Summary: Small WebServer
Version: 1.6.9
Release: 10.1
Group: System Environment/Daemons
License: GPLv2
URL: http://www.monkey-project.com/
Source0: http://monkey-project.com/releases/1.6/%{name}-%{version}.tar.gz
BuildRequires: cmake

%description
Monkey is a lightweight and powerful web server and development ostack for
GNU/Linux. It has been designed to be very scalable with low memory and CPU
consumption, the perfect solution for embedded devices.

%package devel
Summary: Development files for the package %{name}
Requires: %{name} = %{version}

%description devel
Header files and development libraries of %{name}.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
./configure	--default-port=80		\
		--prefix=%{_prefix}		\
		--sysconfdir=%{_sysconfdir}/monkey/	\
		--sbindir=%{_prefix}/sbin		\
		--mandir=%{_mandir}/man1/	\
		--webroot=/var/www/html/monkey/ \
        	--libdir=%{_libdir}
        
make

%install
%make_install

%files
%{_sbindir}/*
%{_sysconfdir}/monkey
%{_mandir}/man1/*
/var/www/html/monkey/*

%files devel
%{_includedir}/%{name}
%{_libdir}/monkey-*.so

%changelog
* Thu Aug 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.9
- Rebuilt for Fedora
* Wed Nov 16 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.21.0-1
+ Revision: 730913
- imported package monkey
