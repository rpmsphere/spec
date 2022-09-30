Name:		libYGP		
Version:	0.9.42
Release:	1
Summary:	YGP library
Group:		library/System
License:	GPL
URL: 		http://libymp.sourceforge.net			
Source0:	http://sourceforge.net/projects/libymp/files/%{name}-%{version}.tar.gz	
BuildRequires:	gmp-devel, gtkmm24-devel, gtkhtml3-devel

%description
A portable general purpose library, written in C++ consisting of:
- A common part, containing things like a general parser, classes to handle
  regular expressions (file and real ones), and the like.
- An X-windows part, basing on gtkmm-2.

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q 
sed -i 's|return child|return bool(child)|' YGP/StatusObj.h
sed -i '1i #include <glibmm/main.h>' XGP/AnimWindow.cpp

%build
%configure
sed -i 's|-Wall|-Wall -std=gnu++14 -fpermissive|' Makefile */Makefile */*/Makefile
sed -i -e 's/, fs::native//g' -e 's/path.file_string/path.string /g' YGP/IVIOAppl.cpp
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc README NEWS COPYING ChangeLog AUTHORS
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/XGP
%{_libdir}/lib*.so
%{_bindir}/*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.*a
%{_includedir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.42
- Rebuilt for Fedora
* Thu Nov 15 2012 kevinchen <kevin.chen@ossii.com.tw> - 0.9.42-2
- Compiler debug & Package. 
* Mon Jun 4 2012 johnwu <johnwu@ossii.com.tw>
- First
