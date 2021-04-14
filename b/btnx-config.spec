Name:           btnx-config
Version:        0.4.9
Release:        15.1
Summary:        GUI Configuration Tool for btnx
Source:         http://www.ollisalonen.com/btnx/btnx-config-%{version}.tar.gz
Patch1:         btnx-config-desktop.patch
Patch2:         btnx-config-dep_downgrade.patch
URL:            http://www.ollisalonen.com/btnx/
Group:          Hardware/Other
License:        GNU General Public License version 2 (GPL v2)
BuildRequires:  libpng-devel
BuildRequires:  gtk2-devel libglade2-devel
BuildRequires:  scrollkeeper yelp
BuildRequires:  gcc make glibc-devel
BuildRequires:  autoconf automake libtool pkgconfig
BuildRequires:  notification-daemon sane-backends-devel
Requires:       btnx

%description
btnx-config is a GUI configuration tool for btnx. btnx requires btnx-config to
work, because btnx-config also detects your mouse and its buttons. This
combination should work for just about any mouse.

%prep
%setup -q
%patch1
%patch2

%build
export SUSE_ASNEEDED=0
autoreconf -fiv

export builddocs=yes
export init_scripts_path=/etc/init.d
export udev_rules_path=/etc/udev/rules.d
%configure
sed -i 's|-Wl -export-dynamic|-Wl,--export-dynamic|' src/Makefile
%__make %{?_smp_flags} CFLAGS+=-Wno-format-security

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang "%{name}"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files -f "%{name}.lang"
%{_sbindir}/btnx-config
%dir %{_datadir}/btnx-config
%{_datadir}/btnx-config/btnx-config.glade
%doc %{_datadir}/btnx-config/doc
%{_datadir}/omf/btnx-config
%{_datadir}/applications/btnx-config.desktop
%{_datadir}/pixmaps/btnx.png

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.9
- Rebuilt for Fedora
* Sun Aug 10 2008 guru@unixtech.be
- new upstream version
* Thu Apr 17 2008 guru@unixtech.be
- new package
