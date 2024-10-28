Summary: Conky Manager Extra Themes
Name: conky-manager-extra
Version: 1
BuildArch: noarch
Release: 6.1
License: freeware
Group: User Interface/X
URL: https://www.teejeetech.in/2014/06/conky-manager-v2-themes.html
Source0: https://www.mediafire.com/download/icvmpzhlk7vgejt/default-themes-extra-1.cmtp.7z
Source1: All_In_one_circle.cmtp.7z
Requires: conky-manager

%description
Extra themes for conky-manager.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/conky-manager/themepacks
cp %{SOURCE0} %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/conky-manager/themepacks

%files
%{_datadir}/conky-manager/themepacks/*

%changelog
* Wed Apr 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
