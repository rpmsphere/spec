Summary: Graphically display output of du command
Name: xdu
Version: 3.0
Release: 20.1
Source: https://sd.wareonearth.com/~phil/xdu/%{name}-%{version}.tar.Z
Patch1: https://www.nn.iij4u.or.jp/~tutimura/xdu/xdu-3.0.dirname.patch
Patch2: https://www.nn.iij4u.or.jp/~tutimura/xdu/xdu-3.0.i18n.patch
Patch3: https://www.nosuchhost.net/~cheese/xdu-title.patch
License: MIT
Group: X11/Utilities
BuildRequires: imake
BuildRequires: libXt-devel libXaw-devel

%description
xdu accepts output of "du" command on standard input and graphically
displays results in a window. One can navigate through that information.

%prep
%setup -q -c
%patch 1 -p1 -b .orig
%patch 2 -p1 -b .i18n
%patch 3 -p1 -b .title

%build
xmkmf -a
make %{?_smp_mflags} CCOPTIONS="$RPM_OPT_FLAGS -Wno-format-security"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
make DESTDIR=$RPM_BUILD_ROOT install.man
%if %{fedora}<21
mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
mv $RPM_BUILD_ROOT/etc/X11/app-defaults/XDu $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_datadir}/man
%endif
rm -rf $RPM_BUILD_ROOT/usr/lib/X11

%files
%{_bindir}/xdu
%{_mandir}/man1/xdu*
%config %{_datadir}/X11/app-defaults/XDu
%doc README

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
* Fri Sep 21 2012 josef radinger <cheese@nosuchhost.net> - 3.0-6
- fix removing of $RPM_BUILD_ROOT/%{_libdir}/X11/app-defaults on 64bit-systems
* Fri Sep 21 2012 josef radinger <cheese@nosuchhost.net> - 3.0-5
- fix \n in windowtitle
* Thu Sep 20 2012 josef radinger <cheese@nosuchhost.net> - 3.0-4
- cleanup spec-file
- move binary to /usr/bin/
- BuildRequires
* Mon Jul 16 2012 josef radinger <cheese@nosuchhost.net> - 3.0-3
- initial package
