%define _qt4_qmake qmake-qt4
%define _qt4_datadir %{_datadir}/qt4
%define _qt4_plugindir %{_libdir}/qt4/plugins
%define _qt4_translationdir %(qmake-qt4 -query QT_INSTALL_TRANSLATIONS)

Name:           meego-inputmethodkeyboard
Version:        0.6.10
Release:        2.2
Summary:        MeeGo Virtual Keyboard
Group:		System Environment/Libraries
License:        BSD
URL:            http://meego.gitorious.org/meegotouch/meegotouch-inputmethodkeyboard
Source0:        %{name}-%{version}.tar.bz2
Patch0:         meego-inputmethodkeyboard-0.6.8-translations.patch
BuildRequires:  meego-inputmethodframework-devel >= 0.20.16
BuildRequires:  meego-inputmethodengine-devel >= 0.4.7
BuildRequires:  gcc-c++
BuildRequires:	pkgconfig(QtCore) >= 4.7.0
BuildRequires:  pkgconfig(QtDeclarative)
BuildRequires:	pkgconfig(meegotouch) >= 0.20.77
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(gconf-2.0)
Requires:       meegotouch-theme
Requires:       meego-inputmethodframework
Requires(pre):    /usr/bin/gconftool-2
Requires(post):   /usr/bin/gconftool-2
Requires(preun):  /usr/bin/gconftool-2
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
MeeGo Virtual Keyboard

%package devel
Summary:	MeeGo Virtual Keyboard Development Package
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the files necessary to develop input 
method plugins for MeeGo

%prep
%setup -q
%patch0 -p1 -b .translations

%build
%{_qt4_qmake} -r GCONF_SCHEMAS_DIR=%{_sysconfdir}/gconf/schemas \
		 CONFIG+=noreactionmap \
                 CONFIG+=notests

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install INSTALL="install -p" INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%pre
%gconf_schema_prepare meego-keyboard

%post
/sbin/ldconfig
%gconf_schema_upgrade meego-keyboard

%preun
%gconf_schema_remove meego-keyboard

%postun 
/sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE NEWS README
%{_libdir}/meego-im-plugins/*.so
%{_libdir}/meego-im-plugins/meego-keyboard-qml/
%{_datadir}/meegotouch/virtual-keyboard/
%{_datadir}/themes/base/meegotouch/libmeego-keyboard/
%{_datadir}/themes/base/meegotouch/meego-im-uiserver/
%{_datadir}/themes/base/meegotouch/svg/meegotouch-keyboard.svg
%{_qt4_translationdir}/meegotouch/*.qm
%{_sysconfdir}/gconf/schemas/meego-keyboard.schemas

%files devel
%defattr(-,root,root,-)
%{_includedir}/meego-keyboard/

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Dec 06 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.10
- Rebuild for OSSII

* Sun Jun 05 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.6.10-0
- Update to 0.6.10

* Thu May 26 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.6.8-1
- rebuilt

* Wed May 25 2011 Jan Arne Petersen <jpetersen@openismus.com> - 0.6.8-0
- Initial packaging

