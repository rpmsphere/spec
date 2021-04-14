%undefine _missing_build_ids_terminate_build
%define       V_init  2012-01-01
%define       V_base  2011-02-08

Name:         nmake
Summary:      AT&T New Make
URL:          http://www2.research.att.com/~gsf/
Group:        Building
License:      CPL
Version:      20110208
Release:      1
Source0:      http://I%20accept%20www.opensource.org%2flicenses%2fcpl:.@www.research.att.com/~gsf/download/tgz/ast-base.%{V_base}.tgz
Source1:      http://I%20accept%20www.opensource.org%2flicenses%2fcpl:.@www.research.att.com/~gsf/download/tgz/INIT.%{V_init}.tgz
BuildRequires: compat-gcc-34
BuildRequires: nmake

%description
nmake(1) is the standard software construction tool at AT&T and
Lucent Technologies. It is a descendent of the UNIX make(1) and is
not related to the Microsoft program of the same name.

%prep
%setup -q -c -a 1
#sed -i '/typedef struct _sfio_s _sfio_FILE;/d' src/lib/libast/features/stdio

%build
SHELL=/bin/sh; export SHELL
$SHELL -c './bin/package "read" || true'
$SHELL -c './bin/package "make" CC=gcc34'

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_libdir} \
    $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 755 \
    arch/*/bin/nmake $RPM_BUILD_ROOT%{_bindir}
install -c -m 755 \
    arch/*/lib/libast* $RPM_BUILD_ROOT%{_libdir}
install -c -m 644 \
    arch/*/man/man1/nmake.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/%{name}
%{_libdir}/libast*
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20110208
- Rebuilt for Fedora
