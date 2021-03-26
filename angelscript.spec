Name:           angelscript
Version:        2.22.1
Release:        5.1
Summary:        An extremely flexible cross-platform scripting library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://www.angelcode.com/angelscript/
Source:         %{name}_%{version}.zip
Patch1:         makefile-flags.diff
Patch2:         %{name}-makefile.patch
BuildRequires:  gcc-c++
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The AngelCode Scripting Library, or AngelScript as it is also known,
is an extremely flexible cross-platform scripting library designed to allow
applications to extend their functionality through external scripts.
It has been designed from the beginning to be an easy to use component,
both for the application programmer and the script writer.

%package devel
Summary:        It is an extremely flexible cross-platform scripting library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
It supports Unix sockets and TCP/IP sockets with optional SSL/TLS (OpenSSL)
support. It allows you to write portable and secure network applications
quickly without needing to spend time learning low-level system functions
or reading OpenSSL manuals.

%prep
%setup -qn sdk
%patch1 -p1
%patch2 -p1

%build
pushd angelscript/projects/gnuc/
make %{?_smp_mflags} SHARED=1 CXXFLAGS="%{optflags}" SHARED=1 VERSION=%{version}
popd

%install
pushd angelscript/projects/gnuc/
make install DESTDIR=%{buildroot} DESTLIBDIR=%{_libdir} SHARED=1 VERSION=%{version}
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libangelscript-%{version}.so

%files devel
%defattr(-,root,root)
%{_includedir}/*.h
%{_libdir}/libangelscript.so
%doc docs/manual/

%changelog
* Sun Apr 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.22.1
- Rebuild for Fedora
* Sun Dec  9 2012 joop.boonen@opensuse.org
- Fixes in spec and patch files
* Thu Nov 15 2012 joop.boonen@opensuse.org
- Build version 2.22.1 for rigs of rods
* Wed Apr  4 2012 jengelh@medozas.de
- Avoid use of descending relative paths in %%files
- Add patch to allow using %%optflags and resolve the
  prior rpmlint message about the lack of it
* Sun Mar  4 2012 joop.boonen@opensuse.org
- added docs
- corrected the patch now it the soname and the devel file
  are symlinked to the version file
* Sun Mar  4 2012 joop.boonen@opensuse.org
- cleaned the spec file by means of spec-cleaner
* Sat Mar  3 2012 joop.boonen@opensuse.org
- corrected the license
- adapted the spec file to the openSUSE standard
* Fri Feb 24 2012 virus0025@gmail.com
- initial version
