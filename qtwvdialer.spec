Name:          qtwvdialer
Version:       0.4.4
Release:       8.1
Summary:       A simple graphical front-end for wvdialer
Group:         Application/Graphical/Networking
URL:           http://www.mtoussaint.de/qtwvdialer.html
Source:        http://www.mtoussaint.de/qtwvdialer-%{version}.tgz
License:       GPL
BuildRequires: libpng-devel
BuildRequires: gcc-c++
BuildRequires: qt3-devel
BuildRequires: libstdc++-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel
Requires:      wvdial

%description
QtWvdialer is a simple graphical front-end to wvdial and it's free software.
You need the Qt library version 2.1.0 or better and wvdial. It provides you
with a easy to use GUI to fire up a ppp connection. Additionally you have
access to the output of wvdial, some PPP statistics and a editor for the
wvdial configuration. The code for PPP statistics retrieval was extracted
from the very fine program kpppload from Sean Vyain.

%prep
%setup -q -n QtWvDialer-%{version}

%build
%configure
sed -i 's|-Werror=format-security||' Makefile */Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mv bin/qtwvdialer $RPM_BUILD_ROOT/usr/bin/qtwvdialer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/qtwvdialer
%doc AUTHORS COPYING README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.4
- Rebuild for Fedora
* Fri Aug 01 2008 Ercole 'ercolinux' Carpanetto <ercole69@gmail.com> 0.4.4-1mamba
- package created by autospec
