Summary: Moblin GNOME theme
Name: moblin-gnome-theme
Version: 1.0.0
Release: 3.1
BuildArch: noarch
License: GPL
Group: User Interface/Desktops
Source0: %{name}-%{version}.tar.bz2
URL: http://www.redhat.com
Requires: gtk-nodoka-engine
Requires: vibrant-icon-theme
BuildRequires: perl(XML::Parser)

%description
This package contains the Moblin GNOME meta theme.

%prep
%setup -q 

%build
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
sed -i 's|vibrant|Vibrant|' $RPM_BUILD_ROOT%{_datadir}/themes/Moblin/index.theme
rm $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gtkrc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING
%{_datadir}/themes/Moblin

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
* Thu Jun 10 2010 awafaa@opensuse.org
- Initial import for openSUSE version 1.0.0
