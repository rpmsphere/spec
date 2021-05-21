%global archive_name wncksync

Name:          libwncksync
Version:       0.2.8
Release:       1
Summary:       Match .desktop files to window xid's and the reverse

Group:         System Environment/Libraries
License:       GPLv3 and GPLv3+ and LGPLv3
URL:           https://launchpad.net/wncksync
Source0:       http://launchpad.net/wncksync/0.2/%{version}/+download/%{archive_name}-%{version}.tar.gz

BuildRequires: dbus-glib-devel
BuildRequires: libwnck-devel
BuildRequires: libgtop2-devel
BuildRequires: mate-menus-devel
BuildRequires: glib2-devel
Requires:      glib2

%description
%{name} is a library and a DBus daemon for matching .desktop files
to window xid's and the reverse.


%package devel
Summary:       Match .desktop files to window xid's and the reverse
Group:         Development/Libraries
Requires:      pkgconfig >= 1:0.14
Requires:      %{name} = %{version}-%{release}

%description devel
The %{name}-devel package includes the header files for the
%{name} library.


%prep
%setup -q -n %{archive_name}-%{version}
sed -i 's/GNOME/MATE/g' configure.in
sed -i 's/gnome/mate/g' configure*
sed -i -e 's/GMenu/MateMenu/g' -e 's/gmenu/matemenu/g' -e 's/GMENU/MATEMENU/g' src/windowmatcher.c
sed -i 's/GMENU/MATEMENU/g' configure* Makefile.* */Makefile.* */*/Makefile.*
# temporary fix for implicit DSO linking
# reported upstream: https://bugs.launchpad.net/wncksync/+bug/578972
sed -i 's/CFLAGS="$CFLAGS -lm"/CFLAGS="$CFLAGS -lm -lX11"/g' configure*


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/gio/modules/libgiowncksync.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libwncksync.la


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING COPYING.LGPL
%{_libdir}/gio/modules/libgiowncksync.so
%{_libdir}/libwncksync.so.*
%{_libexecdir}/wncksyncdaemon
%{_datadir}/dbus-1/services/org.wncksync.Matcher.service


%files devel
%defattr(-,root,root,-)
%doc COPYING COPYING.LGPL
%{_includedir}/%{name}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libwncksync.so


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu May 13 2010 Mathieu Bridon <bochecha@fedoraproject.org> - 0.2.8-1
- First build of wncksync
