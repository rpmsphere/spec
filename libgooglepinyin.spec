%global debug_package %{nil}

Name:       libgooglepinyin
Version:    0.1.2
Release:    1
Summary:    A fork from google pinyin on android
URL:        http://code.google.com/p/libgooglepinyin/
License:    APL2.0
Source0:    http://libgooglepinyin.googlecode.com/files/%{name}-%{version}.tar.bz2
Group:      User Interface/Desktops
BuildRequires:  cairo-devel, pango-devel, intltool, cmake, gtk2-devel, gcc-c++
 
%description
A fork from google pinyin on android.

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   libX11-devel
Requires:   %{name} = %{version}
 
%description devel
The %{name}-devel package includes the header files for the googlepinyin package.
 
%prep
%setup -q
 
%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
cmake ../ -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_libdir}
popd
 
make %{?_smp_mflags} -C %{_target_platform}
 
%install
rm -rf %{buildroot}
make install/fast -C %{_target_platform} DESTDIR=%{buildroot}
 
%clean
rm -rf %{buildroot}
 
%files
%{_libdir}/googlepinyin
%{_libdir}/libgooglepinyin.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_libdir}/libgooglepinyin.so

%changelog
* Tue Mar 06 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuild for Fedora
* Tue Sep  6 2011 Percy Lau <percy.lau@gmail.com> 0.1.0
- package for openSUSE.
