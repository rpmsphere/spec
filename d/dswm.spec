Name: dswm
Summary: Deep Space Window Manager
Version: 0.1
Release: 1
Group: User Interface/X
License: GPL
URL: http://sourceforge.net/projects/dswm/
Source0: http://sourceforge.net/projects/%{name}/files/%{version}/%{name}-%{version}.tar.gz
BuildRequires: sbcl
BuildRequires: cl-clx
BuildRequires: cl-ppcre
BuildRequires: cl-asdf

%description
Deep Space Window Manager is a tiling window manager, oriented for good
usability with minimum startup configuration and good integration with EMACS.
DSWM based on StumpWM code. Now project is under hard development so has many
experimental features.

%prep
%setup -q
#mkdir -p $HOME/.dswm.d/rules.d
#sed -i '345i @item C-t g' dswm.texi.in

%build
cd src
autoconf
%configure
make

%install
sed -i 's|/usr/share/xsessions/|$(destdir)/usr/share/xsessions/|g' Makefile
mkdir -p %{buildroot}/usr/share/xsessions
make install destdir=%{buildroot}

%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/%{name}
%exclude %{_datadir}/info/dir
%{_datadir}/info/%{name}.info.*
%{_datadir}/xsessions/%{name}.desktop
%{_datadir}/%{name}
/etc/dss/%{name}

%changelog
* Fri Jan 03 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
