Summary: Globalization Terminal
Name: g11ntty
Version: 0.9
Release: 10
License: GPL
Group: Applications/System
URL: http://people.debian.org.tw/~chihchun/debian/g11n/
Source: %{name}-%{version}.tar.gz
Patch: %{name}_%{version}-1.diff.gz
Vendor: Brian Lin <foxman@xlinux.com>
BuildRequires: g11n, vgl, zwin

%description
Globalization Terminal intends to support every single language in the
world.

%package fonts
Summary: g11ntty CCCII/CNS fonts
Group: User Interface/X

%description fonts
G11NTTY CCCII/CNS Fonts

%prep
%setup -q
%patch -p1
%{__sed} -i 's/ifdef 0/ifdef TESTING/' main.c tty.c
%{__sed} -i -e '1122i break;' -e '1285i break;' eterm.c
%{__sed} -i 's|/usr/fonts|/usr/share/fonts|' config.c g11nmode.c Makefile.cfg settings/etc/g11ntty/font.*
%{__sed} -i -e 's/-mpentium//' -e 's/g11ntty g11ntty.static/g11ntty/' Makefile

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"

%install
%{__rm} -rf %{buildroot}
%{__make} install ROOTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
/sbin/g11ntty
/sbin/g11nmode
/lib/g11n-modules
%{_sysconfdir}/g11ntty
%{_datadir}/fonts/gcs.16

%files fonts
%{_datadir}/fonts/gcs.24
%{_datadir}/fonts/gcs.32

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Fri Jan 11 2008 Wei-Lun Chao <bluebat@member.fsf.org>
- Add patch from Rex Tsai.
- Rebuild for M6(CentOS5).

* Mon Jun 26 2000 Ho Joy <joy@xlinux.com>
- add us issue

* Mon Jun 12 2000 Ho Joy <joy@xlinux.com>
- add g11nmode can detect and setup 800x600x256 mode

* Thu Jun 1 2000 Ho Joy <joy@xlinux.com>
- Can not reentry g11ntty

* Wed Mar 7 2000 Ho Joy <joy@xlinux.com>
- fix g11nmode.c

* Sat Jan 8 2000 Brian Lin <foxman@xlinux.com>
- Add resolution detection program
- Delete the incorrect documentation, it is too old and not tender.

* Thu Dec 23 1999 FongRong Kuo <fongrong@xinux.com>
- change Group
