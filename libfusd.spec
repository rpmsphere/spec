%global debug_package %{nil}
%define majver %(echo %version | cut -d. -f 1-2)
%define minver %(echo %version | cut -d. -f 3)

Name:          libfusd
Version:       1.10.11
Release:       13.1
Summary:       A Linux framework for proxying device file callbacks into user-space
Group:         System/Libraries
URL:           http://www.circlemud.org/~jelson/software/fusd/
Source:        http://fort.xdas.com/~kor/oss2jack/fusd-kor-%{majver}-%{minver}.tar.gz
Patch:         libfusd-1.10-10-Makefile.patch
Patch1:        libfusd-1.10.11-kernel2.6.26.patch
Patch2:        libfusd-1.10.11-flag-for-more-data.patch
License:       GPL

%description
FUSD (pronounced fused) is a Linux framework for proxying device file callbacks
into user-space, allowing device files to be implemented by daemons instead
of kernel code. Despite being implemented in user-space, FUSD devices can look
and act just like any other file under /dev which is implemented by kernel callbacks. 

%package devel
Group: Development/Libraries
Summary: A Linux framework for proxying device file callbacks into user-space

%description devel
FUSD (pronounced fused) is a Linux framework for proxying device file callbacks
into user-space, allowing device files to be implemented by daemons instead
of kernel code. Despite being implemented in user-space, FUSD devices can look
and act just like any other file under /dev which is implemented by kernel callbacks. 

This package contains the static library libfusd.a to be used for development.

%prep
%setup -q -n fusd-kor-%{majver}-%{minver}
%patch2 -p1

%build
sed -i "s|/usr/local|$RPM_BUILD_ROOT%{_prefix}|" Makefile
%ifarch x86_64
make obj.x86_64-linux/libfusd.a
%else
%ifarch aarch64
make obj.aarch64-linux/libfusd.a
%else
make obj.i686-linux/libfusd.a
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d -m0755 $RPM_BUILD_ROOT%{_libdir}
%ifarch x86_64
cp obj.x86_64-linux/libfusd.a $RPM_BUILD_ROOT%{_libdir}
%else
%ifarch aarch64
cp obj.aarch64-linux/libfusd.a $RPM_BUILD_ROOT%{_libdir}
%else
cp obj.i686-linux/libfusd.a $RPM_BUILD_ROOT%{_libdir}
%endif
%endif
install -d -m0755 $RPM_BUILD_ROOT%{_includedir}
cp include/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%{_includedir}/*.h
%{_libdir}/libfusd.a
%doc ChangeLog LICENSE README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10.11
- Rebuild for Fedora
* Sat Nov 29 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.10.11-2mamba
- added flag-for-more-data patch
* Fri Nov 28 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.10.11-1mamba
- update to 1.10.11
* Sat Nov 19 2005 Silvan Calarco <silvan.calarco@qilinux.it> 10-1qilnx
- package created by autospec
