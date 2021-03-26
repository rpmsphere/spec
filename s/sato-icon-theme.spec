%define theme_name Sato

Summary: %{theme_name} icon theme
Name: sato-icon-theme
Version: 0.4.1
Release: 6.1
License: CC-BY-SA3
Group: User Interface/Desktops
Source: http://downloads.yoctoproject.org/releases/sato/%{name}-%{version}.tar.gz
URL: https://www.yoctoproject.org/
BuildRequires: icon-naming-utils
BuildArch: noarch

%description
Default icon theme for Yocto project (Pokylinux),
with limited iconset for embedded system.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog AUTHORS NEWS README COPYING
%{_datadir}/icons/%{theme_name}

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1
- Rebuild for Fedora
