Name:           clish
Version:        0.7.3
Release:        4.1
Summary:        CISCO-like Command Line Interface
Group:          System Environment/Shells
License:        GPLv2 
URL:		http://clish.sourceforge.net/
Source0: 	http://downloads.sourceforge.net/%{name}-%{version}.tar.gz   
BuildRequires:  gcc-c++
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
A modular framework for implementing a CISCO-like CLI on a *NIX system.
Arbitary command menus and actions can be defined using XML files.
This software handles the user interaction,
and forks the appropriate system commands to perform any actions.

%package devel 
Summary: Development files for the clish Library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, ldconfig

%description devel 
Develop Libraries and head files for Clish 
 
%prep
%setup -q

%build
cp -f /usr/share/automake-*/config.guess */config.guess
./configure --prefix=/usr
sed -i 's|-Werror | |' Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/clish
install -m 775 xml-examples/*.xml ${RPM_BUILD_ROOT}%{_sysconfdir}/clish
%ifarch x86_64 aarch64
mv ${RPM_BUILD_ROOT}/usr/lib ${RPM_BUILD_ROOT}/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_libdir}/*.so.*
%exclude %{_libdir}/libtinyxml.so.*
%{_bindir}/*

%files devel
%{_libdir}/*.so 
%exclude %{_libdir}/libtinyxml.so
%{_includedir}/clish/*.h
%{_includedir}/lub/*.h
%{_includedir}/tinyrl/*.h
%{_includedir}/tinyxml/*.h
%{_sysconfdir}/clish/*.xml
%exclude %{_libdir}/*.a	
%exclude %{_libdir}/*.la 

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.3
- Rebuild for Fedora
* Mon Apr 26 2010 Devil Wang <wxjeacen@gmail.com> 0.7.3-2
- Modify SPEC for integrating deve files
* Fri Apr 16 2010 Devil Wang <wxjeacen@gmail.com> 0.7.3-1
- Initial Build for clish
