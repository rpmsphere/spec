%global debug_package %{nil}

Summary: A simple scientific calculator for complex numbers
Name: cgtkcalc
Version: 2.2.4
Release: 4.1
License: GPL
Group: X11/Applications
URL: http://cgtkcalc.sourceforge.net/
Source: http://cgtkcalc.sourceforge.net/%{name}-%{version}.tar.gz
BuildRequires: gtk2-devel

%description
This program is a simple desktop calculator for complex number calculation.
The real part, imaginary part, absolute value, and argument of a complex number
can be input.

%prep
%setup -q

%build
export LDFLAGS=-lm
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/%{_prefix} install
make mandir=$RPM_BUILD_ROOT/%{_mandir} install.man
gzip $RPM_BUILD_ROOT/%{_mandir}/man1/cgtkcalc.1
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
mkdir -p $RPM_BUILD_ROOT/usr/share/applications
make _pixmaps_share_=$RPM_BUILD_ROOT/usr/share/pixmaps \
_applnk_dir_=$RPM_BUILD_ROOT/usr/share/applications \
_applnk_sub_dir_="" _desktop_file_=cgtkcalc.desktop install.gnome
sed -i -e 's|Name=cgtkcalc|Name=Complex Calc|' -e '10i Categories=Utility;' $RPM_BUILD_ROOT%{_datadir}/applications/cgtkcalc.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog ReadMe ReadMe-jp example.gtkrc
%{_datadir}/applications/cgtkcalc.desktop
%{_bindir}/cgtkcalc
%{_datadir}/cgtkcalc
%{_mandir}/man1/cgtkcalc.1.*
%{_datadir}/pixmaps/cgtkcalc.png

%changelog
* Tue Apr 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.4
- Rebuild for Fedora
% Sun Oct 19 2007 SAITOH Akira <s-akira@users.sourceforge.net>
- Initial package
