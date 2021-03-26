%global debug_package %{nil}

Name:         advancemess
Release:      15.1
Group:        Games
License:      MAME
BuildRequires: SDL-devel gcc-c++ mesa-libGL-devel
BuildRequires: nasm libtool
Version:      0.102.0.1
Summary:      A port of the MESS
Source:	      http://prdownloads.sourceforge.net/advancemame/%name-%version.tar.gz
Patch:        fix-overflow.patch
URL: http://advancemame.sourceforge.net/readme.html

%description
AdvanceMESS is an unofficial MESS version with an advanced video support for
helping the use with TVs, Arcade Monitors, Fixed Frequencies Monitors and also
for PC Monitors.

%prep
%setup -q
%patch

%build
CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-format-security" CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Wno-format-security" \
./configure --prefix=/usr --bindir=/usr/games --mandir=%_mandir --build=x86_64
make

%install
make install prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT%{_bindir} mandir=$RPM_BUILD_ROOT%_mandir docdir=$RPM_BUILD_ROOT%_docdir

# already in advancemenu
rm -f $RPM_BUILD_ROOT%_bindir/advcfg
rm -f $RPM_BUILD_ROOT%_bindir/advv
rm -f $RPM_BUILD_ROOT%_bindir/advs
rm -f $RPM_BUILD_ROOT%_bindir/advm
rm -f $RPM_BUILD_ROOT%_bindir/advk
rm -f $RPM_BUILD_ROOT%_bindir/advj
rm -f $RPM_BUILD_ROOT/%_mandir/man1/advcfg.1*
rm -f $RPM_BUILD_ROOT/%_mandir/man1/advv.1*
rm -f $RPM_BUILD_ROOT/%_mandir/man1/advmame.1*
rm -f $RPM_BUILD_ROOT/%_mandir/man1/advdev.1*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%{_bindir}/adv*
%{_datadir}/advance
%exclude %{_docdir}/advance
%_mandir/man1/adv*.1.*

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.102.0.1
- Rebuild for Fedora
* Thu Nov 13 2008 - uli@suse.de
- remove man directory
