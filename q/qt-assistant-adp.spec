Summary: Compatibility version of Qt Assistant
Name:    qt-assistant-adp
Version: 4.6.3
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPLv2 with exceptions or GPLv3 with exceptions
Group: System Environment/Libraries
Url: http://qt.nokia.com/doc/4.6/qassistantclient.html
Source: ftp://ftp.qt.nokia.com/qt/source/qt-assistant-qassistantclient-library-compat-src-%{version}.tar.gz
# missing header files from Debian (Fathi Boudra)
Source1: QAssistantClient
Source2: QtAssistant
# build fixes from Debian (Fathi Boudra)
Patch1: 01_build_system.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: qt4-devel >= 4.7.0
%{?_qt4_version:Requires: qt4%{?_isa} >= %{_qt4_version}}

%description
The old version of Qt Assistant, based on Assistant Document Profile (.adp)
files, and the associated QtAssistantClient library, for compatibility with
applications providing help in that format.

New applications should use the new version of Qt Assistant introduced in Qt
4.4, based on the Qt Help Framework also introduced in Qt 4.4, instead.


%package devel
Summary: Development files for the compatibility QAssistantClient
Group: Development/Libraries
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt4-devel

%description devel
This package contains the files necessary to build applications using the
deprecated QAssistantClient class (in the deprecated QtAssistantClient library),
which is used together with the legacy Assistant Document Profile (.adp) version
of Qt Assistant.

This class is obsolete. It is provided to keep old source code working. We
strongly advise against using it in new code. New code should use the Qt Help
Framework introduced in Qt 4.4 and/or the version of Qt Assistant based on it
(also introduced in Qt 4.4) instead.


%prep
%setup -q -n qt-assistant-qassistantclient-library-compat-version-%{version}
%patch1 -p1 -b .build_system
mkdir include
cp -p %{SOURCE1} %{SOURCE2} include/


%build
# build assistant_adp
qmake-qt4 QT_PRODUCT=OpenSource
make %{?_smp_mflags}

# build libQtAssistantClient
cd lib
qmake-qt4 CONFIG=create_prl
make %{?_smp_mflags}

# build assistant_adp translations
cd ../translations
lrelease-qt4 assistant_adp_*.ts
cd ..


%install
rm -rf %{buildroot}

# install assistant_adp
make install INSTALL_ROOT=%{buildroot}

# install libQtAssistantClient
make install INSTALL_ROOT=%{buildroot} -C lib

# install assistant_adp translations
mkdir -p %{buildroot}%{_qt4_translationdir}
install -p -m644 translations/assistant_adp_*.qm \
                 %{buildroot}%{_qt4_translationdir}/

# install assistant.prf mkspec
install -D -p -m644 features/assistant.prf \
                    %{buildroot}%{_qt4_datadir}/mkspecs/features/assistant.prf

# install missing headers (thanks to Fathi Boudra from Debian)
install -p -m644 include/Q* %{buildroot}%{_qt4_headerdir}/QtAssistant/

# nuke dangling reference(s) to the buildroot
sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" %{buildroot}%{_qt4_libdir}/*.prl

# let rpm handle binaries conflicts
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt4_bindir}
mv assistant_adp ../../../bin/
ln -s ../../../bin/assistant_adp .
popd

# _debug target (see bug #196513)
pushd %{buildroot}%{_qt4_libdir}
echo "INPUT(-lQtAssistantClient)" >libQtAssistantClient_debug.so
popd

# Note that we intentionally DO NOT install a .desktop file for assistant_adp
# because it makes no sense to invoke it without a specific .adp file to open.
# By default, it views the Qt documentation, for which we already have a menu
# entry using the current version of the Qt Assistant, and there is no UI for
# viewing anything different. The .adp file needs to be passed on the command
# line, which is usually done by the application.

%find_lang assistant_adp --with-qt --without-mo


%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f assistant_adp.lang
%defattr(-,root,root,-)
%doc LGPL_EXCEPTION.txt LICENSE.LGPL LICENSE.GPL3
%{_bindir}/assistant_adp
%{_qt4_bindir}/assistant_adp
%{_qt4_libdir}/libQtAssistantClient.so.4*

%files devel
%defattr(-,root,root,-)
%{_qt4_headerdir}/QtAssistant/
%{_qt4_libdir}/libQtAssistantClient.so
%{_qt4_libdir}/libQtAssistantClient_debug.so
%{_qt4_libdir}/libQtAssistantClient.prl
%{_libdir}/pkgconfig/QtAssistantClient.pc
%{_qt4_datadir}/mkspecs/features/assistant.prf


%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 05 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.6.3-1
- new upstream tarball with only the compat assistant_adp and QAssistantClient
- build fixes from Debian (Fathi Boudra)
- use find_lang to package the qm files (#609749)

* Tue Mar 16 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.6.2-2
- use versioned BR/Requires to avoid Conflicts

* Sat Mar 13 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.6.2-1
- first Fedora package
