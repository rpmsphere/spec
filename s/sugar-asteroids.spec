Name:		sugar-asteroids
Version:	1
Release:	1
Summary:	Asteroids for Sugar
Group:		Sugar/Activities
License:	LGPLv3
Source:		asteroids-1.xo
BuildRequires:	python, sugar-toolkit
Requires:	sugar
BuildArch:	noarch

%description
Play the classic Asteroids game.

%prep
%setup -q -n asteroids.activity

%build
python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --prefix=%{buildroot}%{_prefix}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/sugar/activities/asteroids.activity/olpcgames/buildmanifest.py

%clean
rm -rf %{buildroot}

%files
%{sugaractivitydir}/asteroids.activity

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1
- Rebuilt for Fedora
