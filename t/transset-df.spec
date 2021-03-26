%global debug_package %{nil}

Name:           transset-df
Version:        6
Release:        3.1
Summary:        Sets translucency properties
License:        MIT
Group:          System/X11
URL:            http://forchheimer.se/transset-df/
Source0:        http://forchheimer.se/transset-df/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  libXrender-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXdamage-devel

%description
This is a modified version of xorg's original transset. It allows
setting and unsetting window's transparency by pressing a key without
bringing up the crosshair.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -D -p -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc README ChangeLog
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Jul 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 6
- Rebuild for Fedora
* Wed Apr 13 2011 obgr_seneca <obgr_seneca> 6-1.mga1
+ Revision: 84418
- removed unneccessary Source1
- imported package transset-df
* Tue Apr 12 2011 Chris Ringeval <dirteat@gmail.com> 6-1mga1
- mga release
