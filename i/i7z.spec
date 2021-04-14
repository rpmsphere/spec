%undefine _debugsource_packages

Name:           i7z
Version:        0.28git
Release:        1
Summary:        Reporting tool for i7, i5, i3 CPUs
License:        GPLv2
URL:            https://github.com/afontenot/i7z
Source0:        i7z-master.zip
BuildRequires:  ncurses-devel

%description
i7z is a CLI curses based monitoring tool for Intel Core i7 processors.

%prep
%setup -q -n %{name}-master
sed -i 's|-Wall|-Wall -Wl,--allow-multiple-definition|' Makefile

%build
make %{?_smp_mflags}

%install
install -Dpm 755 %{name} %{buildroot}%{_sbindir}/%{name}

%files
%doc README COPYING
%{_sbindir}/%{name}

%changelog
* Mon May 04 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.28git
- Rebuilt for Fedora
* Fri Sep 14 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.27.2-1
- Update to 0.27.2 (fix RHBZ #850585)
* Mon Sep 10 2012 Dan Horák <dan[at]danny.cz> - 0.27.1-2
- set ExclusiveArch
* Tue Jul 17 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.27.1-1
- Initial Release
