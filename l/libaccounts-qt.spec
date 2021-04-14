%global commit0 2a9cc22ff7b0b62b60541423763cb3dd992c0f40

Name:           libaccounts-qt
Summary:        Accounts framework Qt bindings
Version:        1.13
Release:        14.1
License:        LGPLv2
URL:            https://gitlab.com/accounts-sso/libaccounts-qt
Source0:        https://gitlab.com/accounts-sso/libaccounts-qt/repository/archive.tar.gz?ref=%{version}#/libaccounts-qt-%{version}-%{commit0}.tar.gz
## upstream patches
Patch102: 0002-Fix-memory-leaks-found-by-valgrind.patch
patch105: 0005-Use-gboolean-instead-of-bool.patch
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  doxygen
BuildRequires:  graphviz

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep
%setup -q -n libaccounts-qt-%{version}-%{commit0}

# See https://community.kde.org/KTp/Setting_up_KAccounts#libaccounts-qt
# "Note that at this very day libaccounts-qt qmake does **NOT** support compiling the library outside the source directory"

%patch102 -p1 -b .0002
%patch105 -p1 -b .0005

# See https://community.kde.org/KTp/Setting_up_KAccounts#libaccounts-qt
# "Note that at this very day libaccounts-qt qmake does **NOT** support compiling the library outside the source directory"
## HACK ##
mkdir orig
mv * orig/ ||:
cp -a orig/ %{_target_platform}-qt4/
mv orig/* .


%build
pushd %{_target_platform}-qt4
%{qmake_qt4} \
    QMF_INSTALL_ROOT=%{_prefix} \
    CONFIG+=release \
    LIBDIR=%{_libdir} \
    accounts-qt.pro

make %{?_smp_mflags}
popd

%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}-qt4

# create/own dirs
mkdir -p %{buildroot}%{_datadir}/accounts/{providers,services}

## unpackaged files
rm -rfv %{buildroot}%{_datadir}/doc/accounts-qt

#remove tests for now
rm -rfv %{buildroot}%{_datadir}/libaccounts-qt-tests
rm -fv %{buildroot}%{_bindir}/accountstest


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libaccounts-qt.so.*
%dir %{_datadir}/accounts/
%dir %{_datadir}/accounts/providers/
%dir %{_datadir}/accounts/services/

%files devel
%{_libdir}/libaccounts-qt.so
%{_includedir}/accounts-qt/
%{_libdir}/pkgconfig/accounts-qt.pc
%{_libdir}/cmake/AccountsQt/

%changelog
* Thu Aug 17 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.13
- Rebuilt for Fedora
* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 1.13-13
- more robust libdir handling (#1366692)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 30 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13-11
- name qt5 subpkgs properly (libaccounts-qt-qt5 => libaccounts-qt5)

* Thu Oct 29 2015 Rex Dieter <rdieter@fedoraproject.org> - 1.13-10
- hack around cannot build out of src-tree
- provide -qt5, -doc here
- own %%_datadir/accounts/{providers,services}

* Mon Sep 28 2015 Rex Dieter <rdieter@fedoraproject.org> 1.13-1
- libaccounts-qt-1.13, merge improvements from libaccounts-qt5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.11-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 25 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.11-4
- Update 64 bits arch patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.11-2
- Rebuild against fixed qt to fix -debuginfo (#1074041)

* Wed Feb 26 2014 Daniel Vrátil <dvratil@redhat.com> - 1.11-1
- Update to 1.11

* Sat Dec 14 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.6-4
- Fix duplicate documentation (#1001255)
- Add %%?_isa to -devel base package dep
- Remove %%defattr

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 06 2013 Karsten Hopp <karsten@redhat.com> 1.6-2
- add s390x and ppc64 to 64bit archs using lib64

* Mon Mar 04 2013 Jaroslav Reznik <jreznik@redhat.com> - 1.6-1
- Update to 1.6
- Fix rebuild issues with GCC 4.8
- Remove accounts-tool
- Cleanup
