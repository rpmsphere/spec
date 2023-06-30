Name:           libg3d
Version:        0.0.8
Release:        6.1
Summary:        Library for 3D file/object viewer
Group:          Applications/Engineering
License:        GPLv2+
URL:            https://automagically.de/g3dviewer/
Source0:        https://automagically.de/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  glib2-devel
BuildRequires:  w3m

%description
This library loads 3D models from various file formats. Its aim is to support
basic import functionality for as much formats as possible. More complete
support is better, of course, and the long time goal.

To help developing plugins and for general use, too, there are a lot of
basic 3d manipulation function, including vector and matrix math, common
file reading stuff, transformations and 3d primitive support.

%package devel
Summary:        Development and documentation files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Libraries, header files and documentation for %{name}.

%prep
%setup -q

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm '{}' ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/g3d*
%{_libdir}/lib*.so.*

%files devel
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/lib*.so
%{_libdir}/%{name}/
%{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/g3d/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.8
- Rebuilt for Fedora
* Tue Feb 03 2009 Fabian Affolter <fabian@bernewireless.net> - 0.0.8-2
- Disabled rpath
* Tue Feb 03 2009 Fabian Affolter <fabian@bernewireless.net> - 0.0.8-1
- Initial package for Fedora
