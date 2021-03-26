Summary: Enlightenment thumbnailing library
Name: ethumb
Version: 0.1.1.65643
Release: 1%{dist}
License: LGPLv3+
Group: System Environment/Libraries
URL: http://www.enlightenment.org/
Source: http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: evas-devel
BuildRequires: ecore-devel
BuildRequires: edje-devel edje
BuildRequires: e_dbus-devel
BuildRequires: libexif-devel
BuildRequires: libtool, subversion

%description
New library to generate thumbnails.
There are still some important features to be implemented, like
client-server framework, edje thumbnails and a plugin API to integrate
it with emotion and like.

%package devel
Summary: Enlightenment thumbnailing library - devel files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
ethumb development headers and development libraries.

%prep
%setup -q

%build
autoreconf -fi
%configure --disable-static
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="$RPM_BUILD_ROOT" install

find %buildroot -name *.la | xargs rm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS README
%{_bindir}/ethumb
%{_bindir}/ethumbd
%{_bindir}/ethumbd_client
%{_libdir}/*.so.*
%{_datadir}/dbus-1/services/org.enlightenment.Ethumb.service
%{_datadir}/ethumb
#%{_libdir}/ethumb
%{_libexecdir}/ethumbd_slave

%files devel
%defattr(-,root,root)
%{_includedir}/ethumb-0/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Fri Mar 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> 0.1.1
- Update to r65643

* Sun Dec 5 2010 Firefly <firefly@opendesktop.org.tw> - 0.1.1.55225-1
- new version 0.1.1.55225
