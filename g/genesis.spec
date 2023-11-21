Name:           genesis
Version:        0.1
Release:        1
Summary:        Moblin Application Lifecycle Manager 
Group:          Development/Languages
License:        LGPLv2+
URL:            https://test.moblin.org/projects/application-launcher
Source0:        genesis-0.1.tar.bz2
BuildRequires:  cairo-devel clutter-devel libwnck libwnck-devel

%description
This project is part of the Moblin application framework, 
exposing interface for application developers to conveniently access application information, 
starting an application by calling a single API, 
and processing various run-time statuses for each running application.
It also maintains the application list for the applications that are installed in the system, 
and updates the list whenever a change happens in the monitored applications.

%prep
%setup -q -n %{name}

%build
./autogen.sh --prefix=/usr
sed -i 's|-Werror ||' Makefile */Makefile
make 

%install
rm -rf $RPM_BUILD_ROOT
%make_install 
%ifarch x86_64 aarch64
mkdir $RPM_BUILD_ROOT/usr/lib64
mv $RPM_BUILD_ROOT/usr/lib/* $RPM_BUILD_ROOT/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/libgenesis.*
%{_libdir}/pkgconfig/genesis.pc
%{_includedir}/genesis/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Wed Sep 10 2008 Feather Mountain <john@ossii.com.tw> 0.1
- Build for OSSII
