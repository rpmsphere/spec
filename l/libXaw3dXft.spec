Summary:        An extended version of Xaw3d with support for UTF8
Name:           libXaw3dXft
Version:        1.6.2h
Release:        1
License:        GPLv3+
Group:          System Environment/Libraries
URL:            http://sourceforge.net/projects/sf-xpaint
Source0:        http://sourceforge.net/projects/sf-xpaint/files/libxaw3dxft/%{name}-%{version}.tar.bz2
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXft-devel

%description
Xaw3dxft is an extended version of Xaw3d, developed as part of xpaint
with support for UTF8 input and UTF8 encoding of text, and rendering
text with the Freetype library and Truetype fonts.

It should be mostly compatible with the original Xaw3d library, except
for font management: everything using the old X11 core font routines
should be replaced by their freetype equivalents.

%package devel
Summary: Development files for %{name}
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with %{name}.

%prep
%setup -q
sed -i -e 's|/usr/lib|%{_libdir}|g' configure

%build
%configure --enable-internationalization --enable-arrow-scrollbars
make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%doc README README.xaw3d COPYING 
%{_libdir}/libXaw3dxft*.so.*

%files devel
%doc
%{_includedir}/X11/Xaw3dxft
%{_libdir}/libXaw3dxft.so
%{_libdir}/pkgconfig/libxaw3dxft.pc
%exclude %{_libdir}/libXaw3dxft.la
%exclude %{_libdir}/libXaw3dxft.a
%exclude %{_datadir}/doc

%changelog
* Sun Sep 19 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.2h
- Rebuilt for Fedora
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2d-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun May 10 2015 Paulo Roma <roma@lcg.ufrj.br> - 1.6.2d-1
- Update to 1.6.2d
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Tue Sep 03 2013 Paulo Roma <roma@lcg.ufrj.br> 1.6.2b-1
- Initial version.
