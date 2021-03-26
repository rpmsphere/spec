%global debug_package %{nil}

Name:           libircclient-qt
Version:        0.5.0
Release:        12.1
Summary:        Cross-platform IRC client library written with Qt 4
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.bitbucket.org/jpnurmi/libircclient-qt
Source0:        https://bitbucket.org/jpnurmi/libircclient-qt/downloads/%{name}-src-%{version}.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, qt4-devel
BuildRequires:  libicu-devel

%description
LibIrcClient-Qt is a cross-platform IRC client library written with Qt 4.

%prep
%setup -q
# Comment out silent config option to show compiler output
sed -i 's|CONFIG += silent|#CONFIG += silent|g' libircclient-qt.pro

%build
qmake-qt4
make %{_smp_mflags}

%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING AUTHORS README CHANGELOG
%{_libdir}/libircclient-qt.so.0
%{_libdir}/libircclient-qt.so.0.5
%{_libdir}/libircclient-qt.so.0.5.0

%package devel
Summary:        Cross-platform IRC client library written with Qt 4 (development files)
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt-devel

%description devel
LibIrcClient-Qt is a cross-platform IRC client library written with Qt 4.

%files devel
%doc doc/
%dir %{_includedir}/ircclient-qt/
%{_includedir}/ircclient-qt/Irc
%{_includedir}/ircclient-qt/IrcBuffer
%{_includedir}/ircclient-qt/IrcGlobal
%{_includedir}/ircclient-qt/IrcSession
%{_includedir}/ircclient-qt/IrcUtil
%{_includedir}/ircclient-qt/irc.h
%{_includedir}/ircclient-qt/ircbuffer.h
%{_includedir}/ircclient-qt/ircglobal.h
%{_includedir}/ircclient-qt/ircsession.h
%{_includedir}/ircclient-qt/ircutil.h
%{_libdir}/libircclient-qt.so
%{_libdir}/qt4/mkspecs/features/libircclient-qt-config.prf
%{_libdir}/qt4/mkspecs/features/libircclient-qt.prf

%changelog
* Thu Jun 04 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuild for Fedora
* Fri Apr 27 2012 Jan Kaluza <jkaluza@redhat.com> 0.5.0-5
- Rebuild because of libicu
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Mon Sep 12 2011 Jan Kaluza <jkaluza@redhat.com> 0.5.0-3
- Rebuild because of libicu
* Wed Aug 03 2011 Jan Kaluza <jkaluza@redhat.com> 0.5.0-2
- fixed URL and Group, added proper Requires for -devel
- fixed directories ownership. docs are included now
- show compiler output
* Wed May 25 2011 Jan Kaluza <jkaluza@redhat.com> 0.5.0-1
- Initial Fedora packaging
