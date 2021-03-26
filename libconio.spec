Name:           libconio
Version:        1.0.0
Release:        3.1
License:        GPL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Group:          Development/Libraries
Summary:        Implementation of conio.h functions
Source:         %{name}-%{version}.tar.bz2

%description
libconio is an implementation of conio.h functions that some DOS and Windows
compilers provide. It's purpose is to allow developers to use functions like
getch, getche, textcolor and others in a linux environment.

%package devel
Group:          Development/Libraries
Summary:        implementation of conio.h functions
Requires:       libconio = %{version} glibc-devel

%description devel
libconio is an implementation of conio.h functions that some DOS and Windows
compilers provide. It's purpose is to allow developers to use functions like
getch, getche, textcolor and others in a linux environment.

%prep
%setup -q

%build
autoreconf -fi
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%configure --disable-static --with-pic
%{__make} %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libconio.so.0*

%files devel
%defattr(-,root,root)
%{_includedir}/conio.h
%{_libdir}/libconio.so
%{_mandir}/man3/*

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuild for Fedora
* Mon Oct 22 2007 crrodriguez@suse.de
- first version in the OBS
