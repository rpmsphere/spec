%global debug_package %{nil}

Name:           gxe
Version:        1.28
Release:        16.4
License:        GPLv2
Group:          Productivity/Security
BuildRequires:  ncurses-devel
BuildRequires:  cups-devel
BuildRequires:  pkgconfig
BuildRequires:  libgnomeui-devel
BuildRequires:  gvfs-devel
BuildRequires:  w3m udisks2
URL:            http://www.geocities.jp/sakachin2/
Source:         http://www.geocities.jp/sakachin2/%{name}-%{version}.tar.gz
Summary:        Hybrid Editor XE

%description
This editor is fit for programmers working on both main-frame and PC. Its
operation is based on mainframe SPF editor, and like as other editor on PC,
convenient short-cut key operation is hybrid. Basic filer operation is also
provided such as Delete/Copy/Move/Print. It can also manipulate binary file.
(Dump format or 3 line virtical Hex display mode) Powerfull data file edit
function is provided to analyze logfile etc by Excel.

%prep
%setup -q

%build
%configure
sed -i 's|-O0|-O0 -fPIC -Wl,--allow-multiple-definition|' Makefile */Makefile */*/Makefile
make

%install
%make_install
cd %{buildroot}%{_bindir}
rename x xe xbc xci xcv xdc xdd xfc xff xfg xpe xprint xts

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/gnome/help/gxe
%{_datadir}/pixmaps/gxe

%changelog
* Thu Jan 07 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.28
- Rebuild for Fedora
* Fri Jan 20 2012 mrueckert@suse.de
- initial package
