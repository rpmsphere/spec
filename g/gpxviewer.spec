Name: gpxviewer
Summary: Views GPS traces collected in the GPX format
Version: 0.5.2
License: GPLv3
Release: 7.1
Group: misc
URL: https://andrewgee.org/blog/gpxviewer
Source0: https://andrewgee.org/downloads/%{name}/%{name}-%{version}.tar.gz
BuildRequires: python2
BuildRequires: python2-distutils-extra
BuildRequires: intltool
BuildArch: noarch

%description
This application allows the user to load a GPS trace, in the GPX file format,
and read it in a presentable way. You are shown a few statistics, such as the
duration or maximum speed. You are also shown the trace on an openstreetmap
map, where you can scroll around and zoom.

%prep
%setup -q -c

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
install -d %{buildroot}%{_datadir}/locale
cp -a build/mo/* %{buildroot}%{_datadir}/locale
install -d %{buildroot}%{_datadir}/applications
cp -a build/share/applications/gpxviewer.desktop %{buildroot}%{_datadir}/applications

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS CHANGELOG COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/pixmaps/%{name}.svg
%{python2_sitelib}/%{name}*

%changelog
* Fri Aug 18 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.2
- Rebuilt for Fedora
