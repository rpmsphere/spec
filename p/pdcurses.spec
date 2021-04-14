%undefine _debugsource_packages

Name:           pdcurses
Version:        3.4
Release:        27.1
Summary:        Public Domain Curses for X11
License:        Public Domain
Group:          Development/Libraries
URL:            http://pdcurses.sourceforge.net/
Source0:        http://downloads.sourceforge.net/pdcurses/PDCurses-%{version}.tar.gz
BuildRequires:  libX11-devel
BuildRequires:  libXt-devel
BuildRequires:  libXaw-devel

%description
PDCurses is a public domain curses library for DOS, OS/2, Win32, X11
and SDL, implementing most of the functions available in X/Open and
System V R4 curses. It supports many compilers for these
platforms. The X11 port lets you recompile existing text-mode curses
programs to produce native X11 applications.

%package devel
Summary: Development files for PDCurses
Requires: %{name}

%description devel
Header files and Libraries for the package pdcurses.

%prep
%setup -q -n PDCurses-%{version}
sed -i 's|ln -f -s $(libdir)/|ln -f -s |' Makefile.in
%ifarch x86_64 aarch64
sed -i 's|include/lib|include/lib64|' configure
%endif

%build
%configure
make
make -C doc

%install
make DESTDIR=$RPM_BUILD_ROOT install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README HISTORY IMPLEMNT doc/*.txt
%{_libdir}/libXCurses.so
%{_libdir}/libXpanel.so

%files devel
%{_bindir}/xcurses-config
%{_libdir}/libXCurses.a
%{_libdir}/libXpanel.a
%{_includedir}/xcurses.h
%{_includedir}/xpanel.h
%{_includedir}/xcurses/curses.h
%{_includedir}/xcurses/panel.h
%{_includedir}/xcurses/term.h

%changelog
* Sun Jun 23 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4
- Rebuilt for Fedora
