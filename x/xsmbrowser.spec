Summary: Tcl/Tk based Samba shares browser
Name: xsmbrowser
Version: 3.4.0
Release: 14.1
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}-commands.bz2
URL: https://www.public.iastate.edu/~chadspen/
License: GPL
Group: Networking/File transfer
BuildArch: noarch
Requires: expect

%description
xSMBrowser is a fully-capable Samba browsing utility which supports both
WINS and Broadcast networks. It's been tested to work on Redhat, SuSe, DEC
Alphas, and others. It browses all aspects of networks: workgroups,
computers, shares, and files. The ability to add more than one network is
included, and the interface resembles Netscape Navigator (back/forward
buttons, stop, favorites). Mount/unmount buttons are also included.

%prep
%setup -q

%build
# no build for noarch packages
perl -pi -e "s|set image_path \"pixmaps\"|set image_path \"%_datadir/pixmaps/xsmbrowser\"||g;" xsmbrowser

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},/etc,%_datadir/pixmaps/xsmbrowser}/
install -m 755 xsmbrowser $RPM_BUILD_ROOT%{_bindir}
sed -i -e 's|/usr/bin/expectk -f|/usr/bin/tclsh|' -e '2i package require Expect\npackage require Tk' $RPM_BUILD_ROOT%{_bindir}/xsmbrowser
install -m 644  pixmaps/* $RPM_BUILD_ROOT%{_datadir}/pixmaps/xsmbrowser/

# install KDE xsmbrowser-commands file
install -m 644  %{SOURCE1}  $RPM_BUILD_ROOT/etc/
bunzip2 $RPM_BUILD_ROOT/etc/*.bz2

%files
%doc INSTALL
%config(noreplace) %_sysconfdir/*
%_bindir/xsmbrowser
%dir %_datadir/pixmaps/xsmbrowser/
%_datadir/pixmaps/xsmbrowser/*

%changelog
* Mon Apr 27 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4.0
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 3.4.0-11
+ Revision: 60e9aad
- MassBuild#464: Increase release tag
