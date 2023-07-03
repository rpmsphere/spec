Name:		sugar-jumble
Version:	22
Release:	2.1
Summary:	Jumble for Sugar
Group:		Sugar/Activities
License:	LGPLv3
Source:		jumble-22.xo
BuildRequires:	python3, sugar-toolkit-gtk3
Requires:	sugar
BuildArch:	noarch
URL:		https://activities.sugarlabs.org/addon/4413

%description
In a jumble of 83 objects, the player has to locate 20.
Each deal is different. 

%prep
%setup -q -n Jumble.activity
sed -i 's|sugar|sugar3|' setup.py

%build
python3 setup.py build

%install
rm -rf %{buildroot}
python3 setup.py install --prefix=%{buildroot}%{_prefix}

sed -i 's|/usr/bin/env python$|/usr/bin/python3|' %{buildroot}%{_datadir}/sugar/activities/Jumble.activity/setup.py
sed -i 's|/usr/bin/python|/usr/bin/python3|' %{buildroot}%{_datadir}/sugar/activities/Jumble.activity/Jumble.py
sed -i 's|%{buildroot}||' %{buildroot}%{_datadir}/applications/*.activity.desktop

%clean
rm -rf %{buildroot}

%files
%{sugaractivitydir}/Jumble.activity
%{_datadir}/applications/*.activity.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 22
- Rebuilt for Fedora
