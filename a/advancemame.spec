%undefine _debugsource_packages

Name:         advancemame
Release:      8.1
Group:        Games
License:      MAME
BuildRequires: SDL-devel gcc-c++ mesa-libGL-devel
BuildRequires: nasm
Version:      1.2
Summary:      A port of the MAME
Source: http://prdownloads.sourceforge.net/advancemame/%name-%version.tar.gz
URL: http://advancemame.sourceforge.net/readme.html

%description
AdvanceMAME is an unofficial MAME™ version with an advanced video support for
helping the use with TVs, Arcade Monitors, Fixed Frequencies Monitors and also
for PC Monitors.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure --prefix=/usr --bindir=%_bindir --mandir=%_mandir --docdir=%_docdir
make %{?jobs:-j%jobs}

%install
make install prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT%_bindir mandir=$RPM_BUILD_ROOT%_mandir docdir=$RPM_BUILD_ROOT%_docdir

# already in advancemenu
rm -f $RPM_BUILD_ROOT%_bindir/advcfg
rm -f $RPM_BUILD_ROOT%_bindir/advv
rm -f $RPM_BUILD_ROOT/%_mandir/man1/advcfg.1*
rm -f $RPM_BUILD_ROOT/%_mandir/man1/advv.1*
rm -f $RPM_BUILD_ROOT/%_docdir/advance/carddos.txt
rm -f $RPM_BUILD_ROOT/%_docdir/advance/cardlinx.txt

%clean
rm -fr $RPM_BUILD_ROOT

%files
%{_bindir}/adv*
%{_datadir}/advance
%{_docdir}/advance
%_mandir/man1/adv*.1.*

%changelog
* Sun Jan 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Tue Sep  8 2009 uli@suse.de
- update -> 0.106.1
- parallel build
* Thu Nov 13 2008 uli@suse.de
- remove man directory
