Name:          jamvm
Version:       2.0.0
Release:       5.1
Summary:       A Java Virtual Machine which conforms to the JVM specification version 2
Group:         System/Tools
URL:           http://jamvm.sourceforge.net/
Source:        http://kent.dl.sourceforge.net/sourceforge/jamvm/jamvm-%{version}.tar.gz
License:       GPL
BuildRequires: glibc-devel
BuildRequires: zlib-devel
#Requires:      classpath

%description
JamVM is a new Java Virtual Machine conforming to the JVM specification edition 2 (blue book).
It is extremely small - stripped on PowerPC ~110K, Intel 80K. However, unlike other small VMs
it supports the full spec, inc. object finalisation and JNI.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
JamVM is a new Java Virtual Machine conforming to the JVM specification edition 2 (blue book). It is extremely small - stripped on PowerPC ~110K, Intel 80K. However, unlike other small VMs it supports the full spec, inc. object finalisation and JNI.

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
# Don't pass -fomit-frame-pointer, see:
# http://www.nabble.com/Javavm-segmentation-fault-td4490648.html

CC="%{__cc}" \
./configure \
   --prefix=%{_prefix} \
   --bindir=%{_bindir} \
   --libdir=%{_libdir} \
   --with-classpath-install-dir=%{_prefix}

# NOTE: using standard configure with CFLAGS causes jamvm to segfault

#   CPPFLAGS='' \
#   CXXFLAGS='' \
#   FFLAGS='' \
make

%install
%makeinstall

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/jamvm
%{_libdir}/rt.jar
%{_datadir}/jamvm/classes.zip
%doc AUTHORS COPYING ChangeLog NEWS README

%files devel
%{_includedir}/*.h
%{_libdir}/libjvm.la
%{_libdir}/libjvm.so

%changelog
* Mon Jan 30 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.0
- Rebuild for Fedora
* Wed Jul 14 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.4-2mamba
- don't use configure macro to avoid passing default CFLAGS, which causes jamvm to segfault
* Sat May 08 2010 Automatic Build System <autodist@mambasoft.it> 1.5.4-1mamba
- automatic update by autodist
* Wed Jul 01 2009 Automatic Build System <autodist@mambasoft.it> 1.5.3-1mamba
- automatic update by autodist
* Thu Feb 19 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.2-1mamba
- automatic update by autodist
* Tue Jul 08 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.1-1mamba
- package created by autospec
