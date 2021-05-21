%define _qt4_qmake qmake-qt4
%define _qt4_datadir %{_datadir}/qt4
%define _qt4_plugindir %{_libdir}/qt4/plugins
%define _qt4_translationdir %(qmake-qt4 -query QT_INSTALL_TRANSLATIONS)

Name:		meego-inputmethodframework
Version:	0.20.17
Release:	6.1
Summary:	MeeGo Input Method Framework
Group:		System Environment/Libraries
License:	LGPLv2
URL:		http://meego.gitorious.org/meegotouch/meegotouch-inputmethodframework
Source0:	%{name}-%{version}.tar.bz2
Patch0:         meego-inputmethodframework-0.20.16-translations.patch
BuildRequires:	pkgconfig(QtCore) >= 4.7.0
BuildRequires:	pkgconfig(QtDeclarative)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(meegotouch) >= 0.20.77
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:  gcc-c++
Requires(pre):		/usr/bin/gconftool-2
Requires(post):		/usr/bin/gconftool-2
Requires(preun):	/usr/bin/gconftool-2
Requires(post):		/sbin/ldconfig
Requires(postun):	/sbin/ldconfig

%description
MeeGo UI Input Method Framework

%package devel
Summary:	MeeGo Input Method Development Package
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop
input method plugins for MeeGo

%prep
%setup -q

# Fix translations install dir
%patch0 -p1 -b .translations

%build
%{_qt4_qmake} -r M_IM_VERSION=%{version} \
		M_IM_PREFIX=%{_prefix} \
		M_IM_INSTALL_BIN=%{_bindir} \
		M_IM_INSTALL_LIBS=%{_libdir} \
		M_IM_INSTALL_HEADERS=%{_includedir} \
		M_IM_INSTALL_SCHEMAS=%{_sysconfdir}/gconf/schemas \
		M_IM_ENABLE_MULTITOUCH=false \
		CONFIG+=noduicontrolpanel \
		CONFIG+=notests

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot}

# Make dir for plugins
mkdir -p %{buildroot}%{_libdir}/meego-im-plugins

%clean
rm -rf %{buildroot}

%pre
%gconf_schema_prepare meego-im-framework

%post 
/sbin/ldconfig
%gconf_schema_upgrade meego-im-framework

%preun
%gconf_schema_remove meego-im-framework

%postun 
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README LICENSE.LGPL RELEASENOTES NEWS
%{_bindir}/meego-im-uiserver
%{_libdir}/*.so.*
%dir %{_libdir}/meego-im-plugins
%{_qt4_plugindir}/inputmethods/*.so
%{_qt4_translationdir}/meegotouch/text-input-settings.qm
%{_sysconfdir}/gconf/schemas/meego-im-framework.schemas

%files devel
%defattr(-,root,root,-)
%{_includedir}/meegoimframework/
%{_includedir}/meegoimquick/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/qt4/mkspecs/features/*.prf

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Dec 06 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20.17
- Rebuild for OSSII

* Sat Jun 04 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.20.17-0
- Update to 0.20.17
- Update GConf processing for Fedora and OpenSuse

* Wed May 25 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.20.16-0
- Update to 0.20.16

* Sat Apr 30 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.20.7-0.2
- Add meego-inputmethodframework-0.20.7-buildsystem.patch
- Fix build by using configs for qmake
- Install GConf schemas file

* Thu Apr 28 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.20.7-0.1
- Add *.prf file to -devel package

* Tue Apr 26 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.20.7-0
- Initial packaging
