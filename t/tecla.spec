%undefine _missing_build_ids_terminate_build

Name:           tecla
Version:        1.6.3
Release:        7.1
Summary:        Interactive command line editing library
License:        X11
Group:          Development/Libraries/C and C++
URL:            http://www.astro.caltech.edu/~mcs/tecla/
Source:         http://www.astro.caltech.edu/~mcs/tecla/libtecla-%{version}.tar.gz
Patch0:         libtecla_add-destdir.patch
Patch1:         libtecla-makefiles-rules-no-rpath.diff
Patch2:         tecla-cppflags.diff
Patch3:         tecla-only-reentrant.diff
BuildRequires:  autoconf
BuildRequires:  ncurses-devel

%description
The tecla library provides programs with interactive command line
editing facilities, similar to those of the tcsh shell.
In addition to simple command-line editing, it supports recall of
previously entered command lines, TAB completion of file names or
other tokens, and in-line wild-card expansion of filenames. The
internal functions which perform file-name completion and wild-card
expansion are also available externally for optional use by programs.

%package devel
Summary:        Development files for tecla, an interactive command line editing library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
The tecla library provides programs with interactive command line
editing facilities, similar to those of the tcsh shell.

%prep
%setup -q -n libtecla
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoconf # patch3
%configure CPPFLAGS=-Wno-cpp
make #%{?_smp_mflags} # parallel build is broken

%install
%make_install
find "%{buildroot}/%{_libdir}" -type f -name "*.a" -delete
rm -f "%{buildroot}/%{_libdir}"/libtecla.so*
ln -fsv libtecla_r.so "%{buildroot}/%{_libdir}/libtecla.so"
ln -s enhance_r %{buildroot}/%{_bindir}/enhance

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc CHANGES README RELEASE.NOTES LICENSE.TERMS
%{_bindir}/enhance
%{_bindir}/enhance_r
%{_mandir}/man1/enhance.1*
%{_mandir}/man5/teclarc.5*
%{_mandir}/man7/tecla.7*
%{_libdir}/libtecla_r.so.*

%files devel
%{_mandir}/man3/*.3*
%{_includedir}/libtecla.h
%{_libdir}/libtecla.so
%{_libdir}/libtecla_r.so

%changelog
* Fri Apr 13 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.3
- Rebuilt for Fedora
* Fri Jul  7 2017 adam.majer@suse.de
- Add enhance->enhance_r compatibility symlink to binary
* Thu Jul  6 2017 jengelh@inai.de
- Add tecla-only-reentrant.diff: have the tecla tools built
  with tecla_r [boo#1047552].
- Add tecla-cppflags.diff
* Fri May  5 2017 jengelh@inai.de
- Make libtecla and libtecla_r be the same thing to avoid having
  both loaded into the same process image [similar to boo#996551].
* Sat Apr 29 2017 jengelh@inai.de
- RPM group fix; make descriptions the same (but -devel shorter).
* Wed Apr 26 2017 mpluskal@suse.com
- Prepare spec file for factory submission
* Thu Apr 20 2017 mardnh@gmx.de
- update to version 1.6.3
- remove patch: libtecla_pkgconfig.patch
- add patch: libtecla-makefiles-rules-no-rpath.diff
- specfile cleanup
* Sat Feb 28 2015 mardnh@gmx.de
- add libtecla_pkgconfig.patch
* Mon Aug  4 2014 mardnh@gmx.de
- minor specfile cleanup
* Tue Oct 22 2013 mardnh@gmx.de
- initial package
