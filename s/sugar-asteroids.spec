Name:		sugar-asteroids
Version:	1
Release:	2.1
Summary:	Asteroids for Sugar
Group:		Sugar/Activities
License:	LGPLv3
Source:		asteroids-1.xo
BuildRequires:	python3, sugar-toolkit-gtk3
Requires:	sugar
BuildArch:	noarch

%description
Play the classic Asteroids game.

%prep
%setup -q -n asteroids.activity
sed -i -e 's|sugar|sugar3|' -e 's|"asteroids"||' setup.py
sed -i 's|service_name|bundle_id|' activity/activity.info

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --prefix=%{buildroot}%{_prefix}

sed -i 's|/usr/bin/env python$|/usr/bin/python3|' %{buildroot}%{_datadir}/sugar/activities/asteroids.activity/olpcgames/buildmanifest.py
sed -i 's|%{buildroot}||' %{buildroot}%{_datadir}/applications/*.activity.desktop

%clean
rm -rf %{buildroot}

%files
%{sugaractivitydir}/asteroids.activity
%{_datadir}/applications/*.activity.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
