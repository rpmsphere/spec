%undefine _debugsource_packages

Name:           lomse
Version:        0.20.0
Release:        19.1
Summary:        A library to add capabilities to any program for rendering
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
Source:         lib%{name}_%{version}.tar.gz
URL:            http://www.lenmus.org/en/lomse/intro
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libpng-devel
BuildRequires:  make

%description
Lomse is a project designed to provide software developers with a library to
add capabilities to any program for rendering, editing and playing back music
scores. It is written in C++ and it is free open source and platform
independent. It is based on the experience gained developing the Phonascus
program. Lomse stands for "LenMus Open Music Score Edition Library".

%package devel
Summary:        A library to add capabilities to any program for rendering
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files for the package lomse.

%prep
%setup -q -n lib%{name}-%{version}

%build
cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLOMSE_BUILD_STATIC_LIB=ON \
        -DCMAKE_BUILD_TYPE=Release -DFREETYPE_INCLUDE_DIRS=%{_includedir}/freetype2 .
make

%install
make DESTDIR=%{buildroot} install
cp -r test-scores %{buildroot}%{_datadir}/%{name}/
if [ ! -d "%{buildroot}%{_libdir}" ]; then
   mv %{buildroot}/usr/lib %{buildroot}%{_libdir}
fi
rm %{buildroot}%{_libdir}/liblomse.so
ln -s liblomse.so.%{version} %{buildroot}%{_libdir}/liblomse.so
install -m755 bin/lib%{name}.a %{buildroot}%{_libdir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE NEWS THANKS *.md
%{_datadir}/%{name}
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.a
%{_libdir}/lib%{name}*.so
%{_libdir}/pkgconfig/lib%{name}.pc

%changelog
* Wed Nov 09 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20.0
- Rebuilt for Fedora
* Thu Jun 13 2013 joop.boonen@opensuse.org
- Update to version 0.14.0
* Sun Dec 16 2012 joop.boonen@opensuse.org
- Build lomse with fonts etc inside
* Sat Dec 15 2012 joop.boonen@opensuse.org
- Build version 0.12.5
