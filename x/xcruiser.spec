Summary: A filesystem visualization utility
Name: xcruiser
Version: 0.30
Release: 11.1
Group: X11/Applications
License: GNU General Public License
URL: http://xcruiser.sourceforge.net/
Source: http://prdownloads.sourceforge.net/xcruiser/xcruiser-0.30.tar.gz
BuildRequires: imake
BuildRequires: libXt-devel
BuildRequires: libXaw-devel
Obsoletes: xcruise

%description
XCruiser is a filesystem visualization
utility which compares a filesystem to a 3D-formed universe and
allows you to "cruise" within it.

%prep
%setup -q

%build
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT
sed -i 's|/usr/man|/usr/share/man|' Makefile
make install install.man DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/xcruiser
%{_mandir}/man1/xcruiser.1*
%doc README README.jp CHANGES TODO
/usr/lib/X11/app-defaults
%if %{fedora}>20
%{_datadir}/X11/app-defaults/XCruiser
%else
%{_sysconfdir}/X11/app-defaults/XCruiser
%endif

%changelog
* Fri May 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.30
- Rebuilt for Fedora
* Mon Feb 3 2003 Yusuke Shinyama <yusuke@cs.nyu.edu>
- Initial RPM release.
