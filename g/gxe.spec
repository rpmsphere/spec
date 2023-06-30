%undefine _debugsource_packages

Name:           gxe
Version:        1.29
Release:        1
License:        GPLv2
Group:          Productivity/Security
BuildRequires:  ncurses-devel
BuildRequires:  cups-devel
BuildRequires:  pkgconfig
BuildRequires:  libgnomeui-devel
BuildRequires:  gvfs-devel
BuildRequires:  w3m udisks2
URL:            https://www.geocities.jp/sakachin2/
Source:         https://www.geocities.jp/sakachin2/%{name}-%{version}.tar.gz
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
sed -i -e 's|-O0|-O0 -fPIC -Wl,--allow-multiple-definition|' -e 's|-Werror=format-security||' Makefile */Makefile */*/Makefile
make

%install
%make_install
cd %{buildroot}%{_bindir}
rename x xe xbc xci xcv xdc xdd xfc xff xfg xpe xprint xts

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/help/gxe
%{_datadir}/pixmaps/gxe

%changelog
* Sun Jan 15 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.29
- Rebuilt for Fedora
* Fri Jan 20 2012 mrueckert@suse.de
- initial package
