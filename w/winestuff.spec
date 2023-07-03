Name:           winestuff
Version:        0.2.0
Release:        10.1
Summary:        A library for WineGame
License:        LGPL-2.1+
Group:          System/Emulators/PC
URL:            https://code.google.com/p/winegame/
Source0:        https://winegame.googlecode.com/files/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  qt4-devel
#Requires:       fuseiso
#Requires:       winegame

%description
WineGame is a simple front-end to Wine, provides an easy
interface to install some game from DVD.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package provides development libraries and headers
needed to build software using %{name}

%prep
%setup -q

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
# fix crappy CMakeLists.txt
if [ "%{_lib}" != "lib" ]; then
  mv $RPM_BUILD_ROOT%{_prefix}/lib $RPM_BUILD_ROOT%{_libdir}
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGELOG LICENSE README TODO VERSION
%doc %lang(ru) LICENSE.Russian
# no versioned library yet
# %{_libdir}/*.so.*
%{_libdir}/*.so
%{_libdir}/winestuff/
%{_datadir}/winestuff/

%files devel
# %{_libdir}/*.so
%dir %{_includedir}/winestuff
%{_includedir}/winestuff/
%{_datadir}/cmake/Modules/FindWineStuff.cmake

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Mon Mar 19 2012 toddrme2178@gmail.com
- Added 32bit compatibility package (needed to use winegame on 64bit systems)
- Cleaned up spec file formatting
- Updated to current upstream tarball structure
* Sun Feb 19 2012 jengelh@medozas.de
- Update license field to reflect actual license
- Remove redundant tags/sections from specfile
* Tue Aug 31 2010 yar@sibnet.ru
- update to 0.2.0
* Sun Aug 22 2010 yar@sibnet.ru
- update to 0.1.92
* Mon Jul 19 2010 yar@sibnet.ru
- update to 0.1.91
* Mon Jun 28 2010 prusnak@opensuse.org
- spec cleanup
* Wed Jun 16 2010 yar@sibnet.ru
- initial packaging
