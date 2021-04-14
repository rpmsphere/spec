%undefine _debugsource_packages
Summary: Linux screen capture using pygtk, inspired by scrot
Name: escrotum
Version: 0.2.1git
Release: 6.1
Source0: %{name}-master.zip
License: GPLv3
Group: Utilities
BuildArch: noarch
BuildRequires: python2-devel
URL: https://github.com/Roger/escrotum

%description
Because scrot has glitches when selection is used in refreshing windows.
Features:
* fullscreen screenshots
* partial(selection) screenshots
* window screenshot(click to select)
* screenshot by xid
* store the image to the clipboard

%prep
%setup -q -n %{name}-master

%build
python2 setup.py build

%install
python2 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.rst LICENCE.txt
%{_bindir}/%{name}
%{python2_sitelib}/*

%changelog
* Tue Sep 12 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1git
- Rebuilt for Fedora
