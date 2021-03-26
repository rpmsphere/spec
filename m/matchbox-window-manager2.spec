Summary: 	Matchbox Window Manager II
Name: 		matchbox-window-manager2
Version: 	0.1
Release: 	8.1
URL: 		http://git.yoctoproject.org/cgit/cgit.cgi/matchbox-window-manager-2/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://git.yoctoproject.org/cgit/cgit.cgi/matchbox-window-manager-2/snapshot/matchbox-window-manager-2-master.zip
BuildRequires: gtk2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: expat-devel

%description
Matchbox Window Manager II is a complete rewrite of the original
m-w-m. It is in early stages of development.

%prep
%setup -q -n matchbox-window-manager-2-master

%build
autoreconf -vfi
./configure --prefix=/usr --with-gtk --with-pango --enable-maemo-manager
sed -i 's|^LIBS =|LIBS = -lexpat|' matchbox/managers/*/Makefile
make

%install
%make_install

%files
%doc README TODO ChangeLog COPYING
%{_bindir}/matchbox-window-manager-2-*
%{_datadir}/themes/Default/matchbox2

%changelog
* Tue Aug 21 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
