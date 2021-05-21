Summary: Package and settings manager for Wine
Name: winetricks
Version: 20160109
Release: 2.1
BuildArch: noarch
License: GPL+
Group: System Utilities
Source0: https://raw.githubusercontent.com/Winetricks/winetricks/master/src/%{name}
URL: http://wiki.winehq.org/winetricks
Requires: wine-core, cabextract, unzip, wget

%description
Winetricks is an easy way to work around problems in Wine. It has a menu of
supported games/apps for which it can do all the workarounds automatically.
It also lets you install missing DLLs or tweak various Wine settings individually.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 0755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Feb 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 20160109
- Rebuilt for Fedora
* Thu Feb 28 2011 Andrew Wyatt <andrew.wyatt@fewt.com> 20110123
- Initial Release
