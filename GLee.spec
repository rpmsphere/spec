%define major 5
Name:           GLee
Version:        %{major}.4.0
Release:        12.1
Summary:        GL Easy Extension library
Group:          Development/Libraries
License:        BSD
URL:            http://elf-stone.com/glee.php
Source0:        http://www.elf-stone.com/downloads/GLee/GLee-5.4.0-src.tar.gz
BuildRequires:  mesa-libGL-devel

%description
GLee (GL Easy Extension library) is a free cross-platform extension loading
library for OpenGL. It provides seamless support for OpenGL functions up
to version 3.0 and 399 extensions. 

%package devel
Summary:        Development headers for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       mesa-libGL-devel

%description devel
Development headers for %{name}

%prep
%setup -q -c %{name}-%{version}

sed -i "s|\r||g" *.h *.c *.txt
chmod -x *.h *.c *.txt
iconv -f=iso-8859-1 -t=utf-8 readme.txt > tmp && mv tmp readme.txt

sed -i -e '/${LDCONFIG}/d' Makefile.in
sed -i -e '/doc/d' Makefile.in

sed -i 's|-shared|-shared -Wl,-soname,lib%{name}.so.%{major} -fPIC|g' Makefile.in
sed -i 's|LIBNAME=.*|LIBNAME=lib%{name}.so.%{version}|g' Makefile.in

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 $RPM_BUILD_ROOT{%{_includedir}/GL,%{_libdir}}
make install INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir} \
             LIBDIR=$RPM_BUILD_ROOT%{_libdir}

pushd $RPM_BUILD_ROOT%{_libdir}
    ldconfig -n .
    ln -s lib%{name}.so.%{version} lib%{name}.so
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc readme.txt
%{_libdir}/lib%{name}.so.*

%files devel
%doc extensionList.txt
%{_libdir}/lib%{name}.so
%{_includedir}/GL/%{name}.h

%changelog
* Thu Aug 17 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 5.4.0
- Rebuild for Fedora
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 5.4.0-8
- Rebuilt for GCC 5 C++11 ABI change
* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Sat Aug 07 2010 Hicham HAOUARI <hicham.haouari@gmail.com> - 5.4.0-1
- Initial package
