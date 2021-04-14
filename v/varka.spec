%undefine _debugsource_packages

Name:           varka
Version:        0.1.0
Release:        25.1
License:        GPL-3.0
Summary:        A library on top of gtk to build applications
URL:            http://launchpad.net/varka
Group:          Development/Libraries/GNOME
Source:         %{name}_%{version}-0~16.tar.gz
BuildRequires:  vala
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtk3-devel
BuildRequires:  gobject-introspection-devel

%description
A library on top of gtk to build applications used for Marlin File Manager.

%package devel
Summary:        A library on top of gtk to build applications
Group:          Development/Libraries/GNOME
Requires:       varka

%description devel
A library on top of gtk to build applications.Package for Development

%prep
%setup -q
sed -i '/add_target_gir/d' lib/CMakeLists.txt

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README COPYING
#{_prefix}/lib/girepository-1.0/Varka-0.1.typelib
%{_libdir}/libvarka.so.0.1
%{_libdir}/libvarka.so.0
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/vala/vapi/varka.deps
%{_datadir}/vala/vapi/varka.vapi
%{_datadir}/varka

%files devel
%{_includedir}/varka
%{_libdir}/pkgconfig/varka.pc
%{_libdir}/libvarka.so
#{_datadir}/gir-1.0/Varka-0.1.gir

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0
- Rebuilt for Fedora
* Fri Sep 21 2012 sethu@gatech.edu
- Initial Spec file
