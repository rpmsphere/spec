Name: debreate
Summary: A tool to help in creating Debian packages
Version: 0.7.7
Release: 3.1
Group: Converted/Development
License: see /usr/share/doc/debreate/copyright
URL: http://debreate.sourceforge.net/
Source0: http://sourceforge.net/projects/debreate/files/current/%{name}_%{version}_all.deb
BuildArch: noarch
Requires: python2-wxpython

%description
Debreate aids developers who want to package their programs for Debian based
systems. It is mostly aimed at new programmers who are not as familiar with
console commands. Features:
- Easy to use GUI
- Tabbed interface
- Automated "control" file creation and .deb package naming
- Uses "dpkg -b" to build .deb package
- Options to make post install/uninstall scripts

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
mkdir -p %{buildroot}
tar xf data.tar.gz -C %{buildroot}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/launch.py

%files
%{_datadir}/%{name}
%{_datadir}/applications/Debreate.desktop
%{_datadir}/doc/%{name}
%{_datadir}/mime/text/%{name}.xml

%changelog
* Sun Jun 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.7
- Rebuilt for Fedora
