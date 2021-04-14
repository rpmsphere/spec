Summary:        Improved Colored Difference Tool
Name:           icdiff
Version:        1.9.0
Release:        2.1
URL:            http://www.jefftk.com/icdiff
License:        PSF
Group: 		File tools
BuildRequires:  python2-devel
BuildArch:      noarch
Source0:        https://github.com/jeffkaufman/icdiff/archive/release-%{version}.tar.gz#/%{name}-release-%{version}.tar.gz

%description
Show differences between two files in a two column colored view.

%prep
%setup -q -n %{name}-release-%{version}

%build

%install
mkdir -p %buildroot%_bindir
install -p -m755 %name %buildroot%_bindir/%name
install -p -m755 git-%name %buildroot%_bindir/git-%name

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc README.md ChangeLog
%_bindir/%name
%_bindir/git-%name

%changelog
* Fri Jun 23 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.0
- Rebuilt for Fedora
* Tue Mar 01 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.3-alt2
- Moved from binaries from %%_sbindir to %%_bindir (ALT #31848)
* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.3-alt1
- New version
* Tue Dec 16 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 1.7.1-alt1
- Initial build for ALT
