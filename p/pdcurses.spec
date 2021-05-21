%undefine _debugsource_packages

Name:           pdcurses
Version:        3.9
Release:        1
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

%build
cd x11
%configure
make

%install
cd x11
install -d %{buildroot}%{_includedir}/xcurses
install -Dm644 ../*.h %{buildroot}%{_includedir}/xcurses
install -Dm644 libXCurses.a %{buildroot}%{_libdir}/libXCurses.a
install -m755 lib*.so %{buildroot}%{_libdir}
install -Dm755 xcurses-config %{buildroot}%{_bindir}/xcurses-config

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc docs/*
%{_libdir}/libXCurses.so

%files devel
%{_bindir}/xcurses-config
%{_libdir}/libXCurses.a
%{_includedir}/xcurses

%changelog
* Sun Apr 25 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.9
- Rebuilt for Fedora
