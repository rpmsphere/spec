Name: kkedit
Summary: A source code text editor
Version: 0.4.2
Release: 6.1
Group: Applications/Editors
License: GPL
URL: https://github.com/KeithDHedger/KKEdit
Source0: http://keithhedger.hostingsiteforfree.com/zips/kkedit/KKEdit-%{version}.tar.gz
BuildRequires: gtk2-devel
BuildRequires: gtksourceview2-devel
BuildRequires: unique-devel
BuildRequires: webkitgtk-devel
BuildRequires: ctags
BuildRequires: vte-devel
BuildRequires: aspell-devel

%description
KKEdit is a deceptively simple text editor with syntax colouring.

%prep
%setup -q -n KKEdit-%{version}

%build
%configure
make %{?_smp_mflags} CXXFLAGS="-O2 -g -Wall -fPIC"

%install
%make_install

%files
%doc README ChangeLog
%{_bindir}/%{name}*
%{_datadir}/KKEdit
%{_datadir}/applications/KKEdit.desktop
%{_datadir}/pixmaps/KKEdit.png
%{_bindir}/KKEditProgressBar
%{_includedir}/kkedit-plugins.h
%{_datadir}/applications/KKEditRoot.desktop
%{_datadir}/icons/hicolor/128x128/apps/*.png
%{_datadir}/locale/fr_FR/LC_MESSAGES/*.mo
%{_datadir}/pixmaps/*.png
%{_mandir}/man1/*.1.*

%changelog
* Wed Nov 29 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.2
- Rebuild for Fedora
