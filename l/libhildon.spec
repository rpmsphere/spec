Name: libhildon
License: GPL
Group: System Environment/Libraries
Summary: Widgets for the Maemo environment
Version: 1.0.5
Release: 1
Source: https://moblin.org/build-results/projects/hildon-1/lpia/libhildon_%{version}-7.tar.gz
URL: https://www.moblin.org/projects/projects_ui.php
BuildRequires: gtk2-devel
BuildRequires: esound-devel

%description
The Hildon Application Framework is the same set of GTK-based classes
that Nokia used with Maemo.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n hildon-1
sed -i 's/-Werror /-Wno-format-security -lX11 /' configure.ac
sed -i 's|inline void|static void|' src/hildon-color-chooser.c

%build
#./autogen.sh
autoreconf -ifv
%configure --without-maemo-gtk
%__make

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README NEWS HACKING INSTALL AUTHORS ChangeLog ChangeLog.1 ChangeLog.2 COPYING
%{_libdir}/libhildon-1.so.0*
%{_datadir}/locale/*/LC_MESSAGES/hildon.mo

%files devel
%{_includedir}/hildon-1
%{_libdir}/libhildon-1.a
#{_libdir}/libhildon-1.la
%{_libdir}/libhildon-1.so
%{_libdir}/pkgconfig/hildon-1.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.5
- Rebuilt for Fedora
