%define _qt4_qmake qmake-qt4
%define _qt4_datadir %{_datadir}/qt4

Name:           meego-inputmethodengine
Version:        0.4.8
Release:        4.1
Summary:        Meego UI Input Method Engine
License:        LGPLv2
URL:            https://meego.gitorious.org/meegotouch/meegotouch-inputmethodengine
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
BuildRequires:  pkgconfig(QtCore) >= 4.7.0
BuildRequires:  gcc-c++

%description
Meego UI Input Method Engine

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header 
files for developing applications that use 
%{name}.

%prep
%setup -q

sed '/^Version:/c\Version: %{version}' -i src/MeegoImEngine.pc.in
sed -e 's#^MEEGOIMENGINE_PREFIX=/usr#MEEGOIMENGINE_PREFIX=%{_prefix}#' \
    -e 's#^LIBS+=-L$${MEEGOIMENGINE_PREFIX}/lib#LIBS+=-L%{_libdir}#' -i meegoimengine.prf
sed -e 's#^MEEGOIMENGINE_WORDS_PREFIX=.*#MEEGOIMENGINE_WORDS_PREFIX=%{_prefix}#' \
    -e 's#^LIBS+=-L.*#LIBS+=-L%{_libdir}#' -i meegoimengine.prf
sed -e 's#target.path += $$MEEGOIMENGINE_PREFIX/lib#target.path += %{_libdir}#' \
    -e 's#install_pkgconfig.path = .*#install_pkgconfig.path = %{_libdir}/pkgconfig#' \
    -e 's#install_pkgconfig.config = .*#install_pkgconfig.CONFIG += no_check_exist#' \
    -i src/src.pro
sed -e 's#/usr/lib/#%{_libdir}/#g' -i ./src/mimenginefactory.cpp
sed -e 's#/usr/lib/#%{_libdir}/#g' -i dummydriver/dummydriver_hwr/dummydriver_hwr.pro
sed -e 's#/usr/lib/#%{_libdir}/#g' -i dummydriver/dummydriver_words/dummydriver_words.pro
sed -e 's#/usr/lib/#%{_libdir}/#g' -i dummydriver/dummydriver_words/dummydriver.pro

%build
%{_qt4_qmake} -r
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot}

# Remove tests
rm -rf %{buildroot}%{_prefix}/lib/libmeegoimengine-tests
rm -rf %{buildroot}%{_datadir}/libmeegoimengine-tests
rm -rf %{buildroot}%{_prefix}/lib/meego-imengines/drivers/hwr/libstubdriver*.so
rm -rf %{buildroot}%{_prefix}/lib/meego-imengines/drivers/words/libstubdriver*.so
rm -rf %{buildroot}%{_prefix}/lib/meego-imengines/drivers/hwr/libdummyimdriver*.so
rm -rf %{buildroot}%{_prefix}/lib/meego-imengines/drivers/words/libdummyimdriver*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc RELEASENOTES
%{_libdir}/*.so.*
%{_libdir}/meego-imengines/

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/qt4/mkspecs/features/*.prf

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Dec 06 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.8
- Rebuild for OSSII

* Thu May 26 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.4.7-1
- rebuilt

* Wed May 25 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.4.7-0
- Update to 0.4.7

* Wed Apr 27 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.4.6-0
- Initial packaging

