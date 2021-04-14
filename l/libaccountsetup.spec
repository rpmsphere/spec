%undefine _debugsource_packages
%define __arch_install_post %{nil}

Name:           libaccountsetup
Version:        3.0
Release:        36.1
License:        LGPLv2.1
Summary:        Library for account setup plugins
URL:            https://github.com/nemomobile-graveyard/libaccountsetup
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(accounts-qt)
BuildRequires:	netpbm
BuildRequires:	ghostscript-core

%description
This library handles the IPC between a client application and the account setup
plugins. Account plugins are standalone executables which provide functionality
to create and edit user accounts.

Account plugins should also be implemented by using this library's classes.

%package devel
Summary:        Development files for libaccountsetup
Group:          Development/Libraries
Requires:       %{name} = %{version}

%description devel
Development package for applications which need to invoke MeeGo account
plugins, and for developing such plugins.

%prep
%setup -q
sed -i '1i #include <unistd.h>' AccountSetup/provider-plugin-*.cpp
sed -i 's|/usr|$${PREFIX}|' tests/testplugin.pro
#sed -i -e '275s|Provider \*provider|Provider provider|' -e '276s|d->startProcess(provider|d->startProcess(\&provider|' AccountSetup/provider-plugin-proxy.cpp
#sed -i -e 's|Provider \*provider|Provider provider|' -e 's|QVERIFY(provider|QVERIFY(\&provider|' -e 's|proxy->createAccount(provider|proxy->createAccount(\&provider|' tests/test.cpp

%build
qmake-qt4 CONFIG+=release PREFIX=%{buildroot}/usr
make %{?_smp_mflags}

%install
%makeinstall
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README COPYING
%{_libdir}/libAccountSetup.so.*

%files devel
%{_includedir}/AccountSetup/*
%{_libdir}/libAccountSetup.so
%{_libdir}/pkgconfig/AccountSetup.pc
%{_bindir}/libaccountsetup-test
%{_datadir}/libaccountsetup-tests/*
%{_libdir}/AccountSetup/testplugin
%{_datadir}/doc/*

%changelog
* Mon Nov 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
* Mon Mar 28 2011 Alberto Mardegan <mardy@users.sourceforge.net> - 0.5
- First packaging for MeeGo
