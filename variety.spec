Name: variety
Summary: An automatic wallpaper changer, downloader and manager
Version: 0.4.20
Release: 3.3
Group: User Interface/Desktops
License: GPLv3
URL: http://peterlevi.com/variety/
Source0: https://launchpad.net/variety/trunk/%{version}/+download/%{name}_%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python2-devel
BuildRequires: python-distutils-extra
BuildRequires: python-setuptools
BuildRequires: intltool
Requires: python-pillow
Requires: python-configobj
Requires: python-beautifulsoup4
Requires: python-pycurl
Requires: python-lxml
Requires: python-httplib2
Requires: pyexiv2
Requires: pycairo
Requires: pywebkitgtk
Requires: dbus-python
Requires: ImageMagick
Requires: yelp
Requires: libnotify
BuildArch: noarch

%description
Variety changes the wallpaper on a regular interval using user-specified
or automatically downloaded images.

%prep
%setup -q -n %{name}
sed -i "s|__variety_data_directory__ =.*|__variety_data_directory__ = '%{_datadir}/%{name}'|" variety_lib/varietyconfig.py

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root=$RPM_BUILD_ROOT --prefix=%{_prefix}

%files
%doc COPYING AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python_sitelib}/*

%changelog
* Sat Sep 6 2014 Joshua Rich <joshua.rich@gmail.com> - 0.4.20
- Version bump.
* Tue May 6 2014 Joshua Rich <joshua.rich@gmail.com> - 0.4.17
- Add (Build)Requires
- Fix config path issue
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.13
- Rebuild for Fedora
