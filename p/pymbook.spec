%global debug_package %{nil}
Name:           pymbook
Version:        0.4
Release:        7.1
Summary:        A reader application for http://www.haodoo.net
Group:          Applications/Publishing
License:        GPLv3
URL:            http://code.google.com/p/pymbook
Source0:        http://pymbook.googlecode.com/files/%{name}_%{version}.0-0.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel gettext desktop-file-utils
Requires:       gtk2 desktop-file-utils

%description
pymbook is a project for reading haodoo .pdb files.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

%find_lang %{name}
rm -f $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/icon-theme.cache

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{_datadir}/icons/hicolor/*/*/%{name}*.svg
%{_datadir}/pixmaps/%{name}.png

%post
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :

%postun
gtk-update-icon-cache -qf %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Mon Jul 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
* Tue Oct 5 2010 Yan-ren Tsai <elleryq@gmail.com> 0.4-0
- Initial release for Fedora.
    Note that this specfile is tested.
