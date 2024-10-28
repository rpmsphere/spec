%global __os_install_post %{nil}

Name:           ucimf
Version:        2.3.8
Release:        5.1
Summary:        Unicode Console Input Method Framework
Group:          System Environment/Libraries
License:        GPL
URL:            https://code.google.com/p/ucimf/
Source0:        https://ucimf.googlecode.com/files/lib%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++, libtool-ltdl-devel, freetype-devel, fontconfig-devel
Requires:       freetype, dialog

%description
UCIMF provides a unified framework to use input methods
in unicode console enviroment.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n lib%{name}-%{version}
sed -i '1i #include <unistd.h>' src/ucimf.cpp
sed -i 's|"\[DEBUG\]:"format|format|' include/debug.h

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.*a' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/*.so.*
%{_datadir}/%{name}
%{_mandir}/man?/%{name}*
%{_sysconfdir}/%{name}.conf

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Thu Mar 31 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.8
- Rebuilt for Fedora
