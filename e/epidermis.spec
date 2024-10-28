Name:           epidermis
Version:        0.6.2
Release:        4.1
Summary:        GTK theme manager
License:        GPL
Group:          User Interface/Desktop
URL:            https://epidermis.tuxfamily.org/
Source0:        https://launchpad.net/epidermis/0.x/0.6/+download/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2
BuildRequires:  po4a
BuildRequires:  python2-pyxdg
Requires:       pygtk2

%description
Epidermis theme manager is an open source GTK application for managing,
automatically downloading and installing themes of various types, in order to
transform the look of your Ubuntu desktop, from the moment you turn it on
until the moment you turn it off.

%prep
%setup -q
sed -i -e 's|/usr/bin/env python2.6|/usr/bin/python2|' -e 's|/usr/bin/env python$|/usr/bin/python2|' `find . -name '*.py'` linux/org.tuxfamily.epidermis.Shell.service.in

%build
sed -i 's|"python"|"python2"|' setup.py
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=%{_prefix} --root $RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_bindir}/run.py $RPM_BUILD_ROOT%{_bindir}/%{name}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}*.svg
%{_sysconfdir}/apport/crashdb.conf.d/epidermis-crashdb.conf
%{_sysconfdir}/dbus-1/system.d/org.tuxfamily.epidermis.Shell.conf
%{_sysconfdir}/epidermis.conf
%{_datadir}/apport/package-hooks/source_epidermis.py*
%{_datadir}/dbus-1/system-services/org.tuxfamily.epidermis.Shell.service
%{_datadir}/%{name}
%{_datadir}/gconf/schemas/%{name}.schemas
%{_datadir}/gnome/help/%{name}
%{_datadir}/icons/gnome/*/mimetypes/*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/omf/%{name}/%{name}-*.omf
%{_datadir}/polkit-1/actions/org.tuxfamily.epidermis.shell.policy

%changelog
* Mon Jan 30 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.2
- Rebuilt for Fedora
